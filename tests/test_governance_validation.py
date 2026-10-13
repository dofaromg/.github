"""
tests/test_governance_validation.py
Test cases for mrliouai governance validation.
root_owner: dofaromg
canonical_name: mrliouai
"""

import json
import sys
import textwrap
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
import validate_governance as vg


# ── fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def reset_vg_state(tmp_path):
    """Save and restore validate_governance module-level state after every test."""
    orig_governance = vg.GOVERNANCE
    orig_violations = vg.VIOLATIONS
    orig_public_paths = vg.PUBLIC_PATHS
    yield tmp_path
    vg.GOVERNANCE = orig_governance
    vg.VIOLATIONS = orig_violations
    vg.PUBLIC_PATHS = orig_public_paths


def set_state(tmp_path):
    vg.GOVERNANCE = tmp_path
    vg.VIOLATIONS = []


# ── helpers ───────────────────────────────────────────────────────────────────

GOOD_SHA = "06dc98299897c09c63b77f23968e681e09e51362"
GOOD_PERMALINK = f"https://github.com/dofaromg/flow-tasks/blob/{GOOD_SHA}/some/file.md"

GOOD_EVIDENCE = {
    "$schema": "./evidence-index.schema.json",
    "schema_version": "1.0.0",
    "generated_at": "2026-08-07",
    "root_owner": "dofaromg",
    "canonical_name": "mrliouai",
    "completeness_status": "in-progress",
    "evidence": [
        {
            "id": "E001",
            "repo": "dofaromg/flow-tasks",
            "path": "some/file.md",
            "commit_sha": GOOD_SHA,
            "permalink": GOOD_PERMALINK,
            "category": "Root Authority Declaration",
            "summary": "Root authority declaration for dofaromg.",
            "claims_supported": ["root_identity"],
            "evidence_strength": "direct",
            "canonical": True,
            "conflict_status": "none",
        }
    ],
}


def make_index(overrides: dict) -> dict:
    data = json.loads(json.dumps(GOOD_EVIDENCE))
    data.update(overrides)
    return data


def make_entry(overrides: dict) -> dict:
    entry = json.loads(json.dumps(GOOD_EVIDENCE["evidence"][0]))
    entry.update(overrides)
    return entry


# ── test: normal index passes ─────────────────────────────────────────────────

def test_valid_index_passes(reset_vg_state):
    tmp_path = reset_vg_state
    (tmp_path / "evidence-index.json").write_text(json.dumps(GOOD_EVIDENCE))
    set_state(tmp_path)
    vg.check_evidence_json()
    assert vg.VIOLATIONS == [], f"Expected no violations, got: {vg.VIOLATIONS}"


# ── test: wrong SHA triggers fail ─────────────────────────────────────────────

def test_bad_sha_fails(reset_vg_state):
    tmp_path = reset_vg_state
    data = make_index({})
    data["evidence"][0] = make_entry({"commit_sha": "abc123"})
    (tmp_path / "evidence-index.json").write_text(json.dumps(data))
    set_state(tmp_path)
    vg.check_evidence_json()
    assert any("commit_sha" in v or "SHA" in v for v in vg.VIOLATIONS), vg.VIOLATIONS


# ── test: duplicate evidence ID triggers fail ─────────────────────────────────

def test_duplicate_evidence_id_fails(reset_vg_state):
    tmp_path = reset_vg_state
    data = make_index({})
    data["evidence"].append(json.loads(json.dumps(GOOD_EVIDENCE["evidence"][0])))
    (tmp_path / "evidence-index.json").write_text(json.dumps(data))
    set_state(tmp_path)
    vg.check_evidence_json()
    assert any("Duplicate" in v for v in vg.VIOLATIONS), vg.VIOLATIONS


# ── test: second root_owner triggers fail ─────────────────────────────────────

def test_second_root_fails(reset_vg_state):
    tmp_path = reset_vg_state
    data = make_index({"root_owner": "someoneelse"})
    (tmp_path / "evidence-index.json").write_text(json.dumps(data))
    set_state(tmp_path)
    vg.check_evidence_json()
    assert any("root_owner" in v for v in vg.VIOLATIONS), vg.VIOLATIONS


# ── test: wrong canonical_name triggers fail ──────────────────────────────────

def test_wrong_canonical_name_fails(reset_vg_state):
    tmp_path = reset_vg_state
    data = make_index({"canonical_name": "MrliouAI"})
    (tmp_path / "evidence-index.json").write_text(json.dumps(data))
    set_state(tmp_path)
    vg.check_evidence_json()
    assert any("canonical_name" in v for v in vg.VIOLATIONS), vg.VIOLATIONS


# ── test: unregistered rename prohibited ─────────────────────────────────────

def test_unregistered_rename_prohibited(reset_vg_state):
    tmp_path = reset_vg_state
    # Registry without the prohibition line
    (tmp_path / "NAMING_MIGRATION_REGISTRY.yml").write_text(
        "canonical_external_name: mrliouai\n"
    )
    set_state(tmp_path)
    vg.check_naming_registry()
    assert any("prohibited" in v.lower() or "destructive" in v.lower()
               for v in vg.VIOLATIONS), vg.VIOLATIONS


# ── test: public vendor leak triggers fail ────────────────────────────────────

def test_public_vendor_leak_fails(reset_vg_state):
    tmp_path = reset_vg_state
    readme = tmp_path / "README.md"
    readme.write_text("# App\nPowered by OpenAI\n")
    vg.PUBLIC_PATHS = [readme]
    set_state(tmp_path)
    vg.check_public_paths_for_vendor_leak()
    assert any("Powered by" in v or "vendor" in v.lower() for v in vg.VIOLATIONS), vg.VIOLATIONS


# ── test: conflict matrix must have ruling and acceptance criteria ─────────────

def test_conflict_matrix_missing_ruling_fails(reset_vg_state):
    tmp_path = reset_vg_state
    (tmp_path / "CONFLICT_MATRIX.md").write_text(
        textwrap.dedent("""\
        # Conflict Matrix
        root_owner: dofaromg
        canonical_name: mrliouai

        ## C001 — test
        | 嚴重度 | Low |
        | 驗收標準 | something |
        """)
    )
    set_state(tmp_path)
    vg.check_conflict_matrix()
    assert any("Canonical 裁定" in v for v in vg.VIOLATIONS), vg.VIOLATIONS


@pytest.mark.parametrize("mutation,expected", [("none", False), ("remove_mrl", True), ("replace_origin", True)])
def test_mrl_identity_policy(reset_vg_state, mutation, expected):
    tmp_path = reset_vg_state
    data = {"canonical_system_name": "MRL", "origin_signature": "MrLiouWord", "public_layer": {"allowed_brands": ["MRL", "mrliouai"], "allowed_origin_signature": "MrLiouWord"}}
    if mutation == "remove_mrl":
        data["public_layer"]["allowed_brands"] = ["mrliouai"]
    if mutation == "replace_origin":
        data["origin_signature"] = "MrliouAI"
    (tmp_path / "public-internal-boundary.json").write_text(json.dumps(data))
    (tmp_path / "NAMING_MIGRATION_REGISTRY.yml").write_text('canonical_system_name: "MRL"\norigin_signature: "MrLiouWord"\nrole: "canonical_world_model_system_name"\nscope: "public_and_internal"\n')
    set_state(tmp_path)
    vg.check_mrl_identity_policy()
    assert bool(vg.VIOLATIONS) == expected
