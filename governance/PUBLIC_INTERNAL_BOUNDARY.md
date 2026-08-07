# Public / Internal Boundary Policy — mrliouai

```
root_owner: dofaromg
canonical_name: mrliouai
policy_version: 1.0.0
generated_at: 2026-08-07
```

> 本文件定義 `mrliouai` 系統的公開展示層與受控內部資料層的邊界。
> 機器可讀版本見 `public-internal-boundary.json`。

---

## 1. 公開展示層（Public Layer）

### 允許出現的內容

- 品牌名稱 `mrliouai`
- `root_owner: dofaromg`（治理文件中）
- 功能描述（不含供應商資訊）
- 使用者介面文字
- 一般 API 文件（不含供應商 endpoint 細節）

### 禁止出現的內容（絕對禁止）

- 供應商名稱（任何 AI 模型、API 或平台供應商）
- `Powered by <vendor>` 或任何形式的供應商歸屬聲明
- Provider endpoint URL 或供應商專屬 API 路徑
- 模型版本號（若該版本號可識別供應商）
- 供應商授權金鑰、token 或憑證（任何形式）
- 供應商合約、定價或採購資訊

### 公開路徑定義

以下路徑視為「公開」，適用上述限制：

- `README.md`（各 repo 根目錄）
- `profile/` 目錄
- `docs/` 目錄（除非明確標記為 `[INTERNAL]`）
- 公開 API endpoint 回應內容
- GitHub Pages 及任何對外網站
- 任何對外公開的 GitHub Action 輸出日誌

---

## 2. 受控內部資料層（Internal Layer）

### 允許存在的內容

- 供應商名稱、模型清單、API endpoint
- `Powered by` 備注（僅限內部文件）
- 採購、合約、定價資訊
- 供應商授權金鑰（加密儲存，不得明文提交）
- 供應鏈追蹤紀錄（provenance）
- 技術整合細節

### 內部路徑定義

以下路徑視為「內部」：

- `deploy/.env*`（不得提交明文密鑰）
- `internal/` 目錄
- `private/` 目錄
- 標記為 `[INTERNAL]` 的文件
- `.gitignore` 排除的路徑

---

## 3. 治理透明原則

治理透明指：

- **允許公開**：變更記錄、核准決策、證據索引、衝突裁定、稽核軌跡
- **不要求公開**：供應商清單、模型版本、API 細節、採購資訊

透明度不等於公開內部供應商資料。

---

## 4. 違規處理

- 自動驗證腳本（`scripts/validate_governance.py`）掃描公開路徑。
- 發現違規時：CI fail-closed，不得自動修復。
- 必須由 `@dofaromg` 核准修正方案後才能解除。

---

## 5. 邊界更新

邊界定義只能由 `@dofaromg` 核准變更。
變更時須同步更新本文件與 `public-internal-boundary.json`。
