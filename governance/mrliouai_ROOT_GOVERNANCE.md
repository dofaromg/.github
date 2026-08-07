# mrliouai Root Governance

```
root_owner: dofaromg
canonical_name: mrliouai
origin_signature: MrLiouWord
governance_version: 1.0.0
generated_at: 2026-08-07
status: canonical
```

---

## 1. 唯一 Root 權威

| 欄位 | 值 |
|------|----|
| Root 人員 | Mr.liou / Mrliou |
| GitHub 身分 | `@dofaromg` |
| origin signature | `MrLiouWord` |
| 對外產品名稱 | `mrliouai`（大小寫完全一致） |
| 自有頂層資產前綴 | `mrliouai_` |

Root 是唯一的、不可替換的、不可拆分的、不可另立的。任何主張第二位 Root 或平行最終核准者的行為均無效。

其他內部識別符（`MRL`、`MRLiouAI`、`mRLiouAI`、`MrLiouWord`）為內部資料，保留不更改，僅整合統一指向 `mrliouai`。

---

## 2. 權限鏈

```
Root (@dofaromg / Mr.liou / Mrliou)
  └─ 治理文件變更（需 Root 核准）
  └─ 命名與品牌決策（需 Root 核准）
  └─ 證據索引更新（需 Root 核准）
  └─ 公開／內部邊界定義（需 Root 核准）
  └─ 供應商與 API 存取授權（需 Root 核准）
  └─ 合併、部署與發布（需 Root 核准）
  └─ 衝突裁定（Root 最終決定）
  └─ AI 自動化（只能執行已授權法則，不得自行建立例外或授權）
```

---

## 3. Fail-Closed 原則

- 未取得明確 Root 核准時，所有不確定狀態預設為**拒絕**。
- 驗證失敗時流程停止，不得自動降級或繞過。
- AI 與自動化系統不得代替 Root 做出核准決定。
- 任何無法匹配已知授權規則的操作均須停止並回報。

---

## 4. 變更控制

1. 所有治理文件（`governance/`、`.github/CODEOWNERS`、`.github/workflows/`、`scripts/`）變更須由 `@dofaromg` 審核核准。
2. 命名變更必須登錄至 `NAMING_MIGRATION_REGISTRY.yml`，不得直接批次替換。
3. 新增證據須更新 `EVIDENCE_INDEX.md` 與 `evidence-index.json`（兩者須同步）。
4. 衝突須記錄於 `CONFLICT_MATRIX.md`，每項必須有 Root 裁定。
5. 歷史文件不得刪除、覆蓋或改寫；遷移使用 alias／migration record。

---

## 5. 公開／內部分層

| 層 | 定義 | 限制 |
|----|------|------|
| 公開展示層 | 對外 UI、README、API 回應中對外欄位 | 只呈現 `mrliouai`；禁止供應商名稱、`Powered by`、provider metadata |
| 受控內部資料層 | 供應商、模型、API、平台技術依賴紀錄（含 `MRL`、`mRLiouAI`、`MRLiouAI` 等內部識別） | 存取受控；不得輸出至公開層 |
| 治理層 | 本 `governance/` 目錄所有文件 | 透明、可稽核；不含供應商公開顯化義務 |

詳細 path 規則見 `PUBLIC_INTERNAL_BOUNDARY.md`。

---

## 6. 歷史保留規則

- 歷史拼寫（`MRL`、`mRLiouAI`、`MRLiouAI`、`MrLiou AI`、`MrLiouWord`）不得刪除，保留為內部資料。
- 歷史身分透過 alias／migration record 整合指向 canonical 對外名稱 `mrliouai`。
- 不改寫 Git 歷史，不覆蓋 `LICENSE`、`NOTICE`、`AUTHORS`、作者資訊。
- 舊拼寫出現在歷史文件中時，記錄為「內部用法」；衝突矩陣中有對應登錄。

---

## 7. 衝突裁定順序

1. Root 明確書面裁定（最高優先）
2. `governance/CONFLICT_MATRIX.md` 中的已裁定項目
3. `governance/EVIDENCE_INDEX.md` 中標記為 `canonical: true` 的文件
4. 多份一致證據的交叉支持
5. 單一來源文件（需 Root 確認）
6. 無法裁定時：**fail closed**，不執行，回報 Root

---

## 8. 本文件的位置與不可移除性

本文件位於 `dofaromg/.github` 中央索引儲存庫，作為整個 `dofaromg` 帳號治理的頂層基準。不得刪除、替換或降級本文件的地位，除非由 Root `@dofaromg` 明確書面核准。
