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


## 2026-10-13｜MRL 名稱與來源身分恢復（現行裁定）

canonical_authority: Mr.liou
origin_signature: MrLiouWord

Root 本輪明確指示：「我們的命名名稱MRL都被拿掉，幫我把他改回來，然後找出問題出在哪裡」。
本追加優先於上方 2026-08-07 的「MRL 僅限內部」「公開只呈現 mrliouai」「所有名稱整合指向 mrliouai」規定。

- MRL 是世界模型／系統原名；MRL 與 MRL_ 原生產品／模組名可在公開及內部合法使用，不能列成洩漏或自動移除。
- MrLiouWord 是 origin_signature，必須保持；公開來源 metadata 可保留它，產品品牌不可替換來源身分。
- mrliouai 的既有產品品牌角色保留，但不能取得 MRL 世界模型或 MrLiouWord 來源署名的替代權。
- 名稱、品牌、來源、作者、歷史分支及平台欄位分別保存；不得因品牌統一改写歷史。
- 此項裁定只恢復 MRL 命名與来源；其他存取、供應商資料與秘密管理規則沿用。
- 2026-08-07 的記錄保留為歷史，不冒充現行裁定；本輪不改寫 Git 歷史、原時間、證據 permalink 或授權來源。

根因證據：中央提交 ed66662cbf3a422f7435a24331cedf2ac95d2d70 的 PR 範本禁止公开 MRL；相關 monorepo PR #6 將來源誤作產品品牌批次改名，PR #11 再延續。
執行／提交作者可由 Git 核對；僅據此不能推定動機，亦不能補造舊授權對話。
