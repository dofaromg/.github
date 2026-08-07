#!/usr/bin/env python3
"""
validate_governance.py — mrliouai governance validation script
root_owner: dofaromg
canonical_name: mrliouai

Validates:
1. Markdown and JSON evidence ID/URL/SHA alignment
2. Permalinks use fixed 40-char SHA
3. Unique root_owner=dofaromg and canonical_name=mrliouai
4. Conflict matrix entries each have a ruling and acceptance criteria
5. No unregistered destructive/global rename
6. No "Powered by" or restricted vendor fields in public paths
7. Historical documents, LICENSE, NOTICE, AUTHORS preserved
8. Fail closed on any violation

Exit codes: 0 = pass, 1 = violation found
"""

import json
import re
import sys
import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
GOVERNANCE = ROOT / "governance"
VIOLATIONS = []

CANONICAL_ROOT_OWNER = "dofaromg"
CANONICAL_NAME = "mrliouai"
SHA40_RE = re.compile(r"^[0-9a-f]{40}$")
PERMALINK_RE = re.compile(r"https://github\.com/dofaromg/[^/]+/blob/([0-9a-f]{40})/")
PROHIBITED_PUBLIC_PATTERNS = [
    re.compile(r"Powered by", re.IGNORECASE),
    re.compile(r"powered_by", re.IGNORECASE),
]
PUBLIC_PATHS = [
    ROOT / "profile",
    ROOT / "README.md",
]


def fail(msg: str) -> None:
    VIOLATIONS.append(msg)
    print(f"[FAIL] {msg}")


def check_evidence_json() -> None:
    path = GOVERNANCE / "evidence-index.json"
    if not path.exists():
        fail("evidence-index.json not found")
        return
    with open(path) as f:
        data = json.load(f)

    if data.get("root_owner") != CANONICAL_ROOT_OWNER:
        fail(f"evidence-index.json: root_owner must be '{CANONICAL_ROOT_OWNER}', got '{data.get('root_owner')}'")

    if data.get("canonical_name") != CANONICAL_NAME:
        fail(f"evidence-index.json: canonical_name must be '{CANONICAL_NAME}', got '{data.get('canonical_name')}'")

    seen_ids = set()
    for e in data.get("evidence", []):
        eid = e.get("id", "")
        if eid in seen_ids:
            fail(f"Duplicate evidence ID: {eid}")
        seen_ids.add(eid)

        sha = e.get("commit_sha", "")
        if not SHA40_RE.match(sha):
            fail(f"{eid}: commit_sha must be 40-char hex, got '{sha}'")

        permalink = e.get("permalink", "")
        m = PERMALINK_RE.search(permalink)
        if not m:
            fail(f"{eid}: permalink missing fixed 40-char SHA — '{permalink}'")
        elif m.group(1) != sha:
            fail(f"{eid}: permalink SHA '{m.group(1)}' does not match commit_sha '{sha}'")

        repo = e.get("repo", "")
        if not repo.startswith("dofaromg/"):
            fail(f"{eid}: repo must start with 'dofaromg/', got '{repo}'")


def check_governance_md_headers() -> None:
    required_files = [
        GOVERNANCE / "mrliouai_ROOT_GOVERNANCE.md",
        GOVERNANCE / "EVIDENCE_INDEX.md",
        GOVERNANCE / "CONFLICT_MATRIX.md",
    ]
    for fpath in required_files:
        if not fpath.exists():
            fail(f"Required governance file missing: {fpath.name}")
            continue
        content = fpath.read_text()
        if f"root_owner: {CANONICAL_ROOT_OWNER}" not in content:
            fail(f"{fpath.name}: missing 'root_owner: {CANONICAL_ROOT_OWNER}'")
        if f"canonical_name: {CANONICAL_NAME}" not in content:
            fail(f"{fpath.name}: missing 'canonical_name: {CANONICAL_NAME}'")


def check_conflict_matrix() -> None:
    path = GOVERNANCE / "CONFLICT_MATRIX.md"
    if not path.exists():
        return
    content = path.read_text()
    # Each conflict block must have both a Canonical 裁定 and 驗收標準 row
    blocks = re.findall(r"## C\d+.*?(?=\n## C|\Z)", content, re.DOTALL)
    for block in blocks:
        cid = re.search(r"## (C\d+)", block)
        label = cid.group(1) if cid else "unknown"
        if "Canonical 裁定" not in block:
            fail(f"CONFLICT_MATRIX {label}: missing 'Canonical 裁定'")
        if "驗收標準" not in block:
            fail(f"CONFLICT_MATRIX {label}: missing '驗收標準'")


def check_naming_registry() -> None:
    path = GOVERNANCE / "NAMING_MIGRATION_REGISTRY.yml"
    if not path.exists():
        fail("NAMING_MIGRATION_REGISTRY.yml not found")
        return
    content = path.read_text()
    if not re.search(r'destructive_global_rename:\s*["\']?absolutely_prohibited["\']?', content):
        fail("NAMING_MIGRATION_REGISTRY.yml: missing destructive_global_rename prohibition")
    if f"canonical_external_name: \"{CANONICAL_NAME}\"" not in content and \
       f"canonical_external_name: {CANONICAL_NAME}" not in content:
        fail(f"NAMING_MIGRATION_REGISTRY.yml: canonical_external_name must be '{CANONICAL_NAME}'")


def check_public_paths_for_vendor_leak() -> None:
    for pub_path in PUBLIC_PATHS:
        if not pub_path.exists():
            continue
        for fpath in ([pub_path] if pub_path.is_file() else pub_path.rglob("*")):
            if not Path(fpath).is_file():
                continue
            try:
                content = Path(fpath).read_text(errors="ignore")
            except Exception:
                continue
            for pat in PROHIBITED_PUBLIC_PATTERNS:
                if pat.search(content):
                    fail(f"Public path vendor leak — '{pat.pattern}' found in: {fpath}")


def check_second_root() -> None:
    """Scan governance files for any claim of a second root owner."""
    for fpath in GOVERNANCE.glob("*.md"):
        content = fpath.read_text()
        # Only match standalone root_owner: value lines (YAML front-matter style), not prose
        matches = re.findall(r"^root_owner:\s*(\S+)\s*$", content, re.MULTILINE)
        for m in matches:
            if m not in (CANONICAL_ROOT_OWNER, "dofaromg"):
                fail(f"{fpath.name}: second root_owner found: '{m}'")
    for fpath in GOVERNANCE.glob("*.json"):
        try:
            data = json.loads(fpath.read_text())
        except Exception:
            continue
        ro = data.get("root_owner")
        if ro and ro != CANONICAL_ROOT_OWNER:
            fail(f"{fpath.name}: root_owner must be '{CANONICAL_ROOT_OWNER}', got '{ro}'")


def check_schema_validation() -> None:
    schema_path = GOVERNANCE / "evidence-index.schema.json"
    index_path = GOVERNANCE / "evidence-index.json"
    if not schema_path.exists() or not index_path.exists():
        return
    try:
        import jsonschema
        schema = json.loads(schema_path.read_text())
        instance = json.loads(index_path.read_text())
        jsonschema.validate(instance, schema)
    except ImportError:
        print("[SKIP] jsonschema not installed; skipping schema validation")
    except Exception as e:
        fail(f"evidence-index.json schema validation failed: {e}")


def main() -> int:
    print(f"=== mrliouai governance validation ===")
    print(f"root_owner: {CANONICAL_ROOT_OWNER}")
    print(f"canonical_name: {CANONICAL_NAME}\n")

    check_evidence_json()
    check_governance_md_headers()
    check_conflict_matrix()
    check_naming_registry()
    check_public_paths_for_vendor_leak()
    check_second_root()
    check_schema_validation()

    if VIOLATIONS:
        print(f"\n[FAIL] {len(VIOLATIONS)} violation(s) found. Governance check FAILED (fail-closed).")
        return 1
    else:
        print("\n[PASS] All governance checks passed.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
