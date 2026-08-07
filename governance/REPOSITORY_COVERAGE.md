# Repository Coverage — mrliouai Governance Audit

```
root_owner: dofaromg
canonical_name: mrliouai
coverage_version: 1.0.0
generated_at: 2026-08-07
completeness_status: in-progress
```

> **完整性聲明**：GitHub API 有分頁（預設每頁 30 筆），code search 有結果上限（1000 筆）；本文件不宣稱已掃描帳號所有檔案。完整性狀態明確標為 `in-progress`，後續透過自動分頁及增量掃描補充。

---

## 1. 盤點方法

1. **GitHub REST API** — `GET /users/dofaromg/repos?per_page=100&page=N` 逐頁列出所有公開 repo。
2. **GitHub Code Search** — `user:dofaromg content:<keyword>` 搜尋核心關鍵詞（`mrliouai`、`root_owner`、`MrLiouWord`、`dofaromg`、`mrliou`、`authority`、`sovereignty`、`provenance`）。
3. **直接存取已知路徑** — 對問題描述中列出的 20 筆已知證據直接存取。
4. **後續增量掃描** — 使用 `.github/workflows/validate-governance.yml` 定期觸發增量掃描。

---

## 2. 已確認治理核心 Repo

| Repo | 治理角色 | 核心文件 | 狀態 |
|------|---------|---------|------|
| `dofaromg/.github` | 帳號頂層中央治理索引 | `governance/` 全目錄 | ✅ 已建立 |
| `dofaromg/----2` | 治理核心儲存庫 | SOVEREIGNTY.md, NAMING.md, SYSTEM_POSITIONING.md | ✅ 已索引 |
| `dofaromg/flow-tasks` | Root Law 原始立法紀錄 | MRL_ROOT_AUTHORITY_v1.md | ✅ 已索引 |
| `dofaromg/flow-tasks-01` | 技術實作 Authority Pack | AUTHORITY_ROOT.md, INTERNAL_GATE.yaml | ✅ 已索引 |
| `dofaromg/MRL_AI_SYSTEM` | 產品正名與材料附錄 | mrliouai_產品正名與材料附錄_v1.md | ✅ 已索引 |
| `dofaromg/particle-file-system` | 稽核層 Gate | MRL_SOURCE_GATE.yaml | ✅ 已索引 |
| `dofaromg/mrliouword-system` | Origin signature 系統 | deploy/.env.deploy, AI_PROVIDERS_README.md | ✅ 已索引（含衝突記錄） |
| `dofaromg/model-context-protocol-mcp-with-next-js` | 外部技術吸收邊界 | MRL_ABSORPTION.md | ✅ 已索引 |
| `dofaromg/500-ai-machine-learning-deep-learning-computer-vision-nlp-projects-with-code` | Fork（含 MRL 治理子目錄） | MRL_AI_SYSTEM/docs/MRL_DELIVERY_MANIFEST_20260531.md | ✅ 已索引（fork 降權） |

---

## 3. 待掃描 Repo

以下為已知存在但尚未完整掃描的分類：

| 分類 | 說明 | 優先度 |
|------|------|--------|
| `dofaromg` 帳號下其餘公開 repo | 受 API 分頁限制，尚未全部列出 | High |
| Fork/upstream 大型第三方 repo | 需降權評估，避免誤列普通程式碼為治理證據 | Medium |
| Private repo | 需 Root 授權後才能掃描 | Low |

---

## 4. Fork / Upstream / 歷史鏡像 / 自有產品分類規則

| 類型 | 判定規則 | 治理證據效力 |
|------|---------|------------|
| **自有原創 repo** | `dofaromg` 為建立者，無明顯上游 fork 關聯 | 全效力 |
| **Fork of 第三方** | GitHub fork 關係可查，或 README 明確說明來源 | 降權：只有 `MRL_*` / `mrliouai` 明確治理文件有效；一般程式碼符號不計 |
| **歷史鏡像** | 存在鏡像關係紀錄 | 降權：參照原始 repo commit 時間戳 |
| **自有產品 fork** | `dofaromg` 為上游，其他 repo fork 自此 | 全效力（以本 repo 為準） |

**關鍵原則**：
- 不憑 repo 名稱自行推斷治理效力。
- 證據只按內容與 commit 判定。
- fork/upstream 大型第三方 repo 中的普通 `provider`、`vendor`、`canonical_name` 符號不計為 mrliouai 治理證據。

---

## 5. 後續自動分頁與增量掃描方法

```bash
# 列出所有公開 repo（分頁）
curl -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/users/dofaromg/repos?per_page=100&page=1"

# Code search（每次最多 100 筆，總上限 1000 筆）
curl -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/search/code?q=mrliouai+user:dofaromg&per_page=100"
```

增量掃描由 `.github/workflows/validate-governance.yml` 定期觸發（schedule: weekly），
結果差異回報至 `governance/REPOSITORY_COVERAGE.md` 更新版本。
