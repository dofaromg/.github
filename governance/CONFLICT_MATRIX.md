# Conflict Matrix — mrliouai Governance

```
root_owner: dofaromg
canonical_name: mrliouai
matrix_version: 1.0.0
generated_at: 2026-08-07
```

每項衝突提供：嚴重度、來源、現況、canonical 裁定、非破壞性修正、驗收標準。

---

## C001 — 命名整合：MRL / mRLiouAI / MRLiouAI / MrLiou AI / MrLiouWord → mrliouai（對外）

| 欄位 | 值 |
|------|----|
| 嚴重度 | Medium |
| 來源 | 多個儲存庫的歷史拼寫與命名演進 |
| 現況 | 多種拼寫並存於不同 repo 與文件中；Root 裁定 `mrliouai` 為唯一對外產品一致性名稱 |
| Canonical 裁定 | 唯一對外產品名稱為 `mrliouai`（大小寫完全一致）；其他拼寫均為內部資料，保留不更改，僅整合統一；`MRL` 保留為內部縮寫；`MrLiouWord` 保留為 origin signature；`mRLiouAI`、`MRLiouAI`、`MrLiou AI` 為內部歷史用法，保留 |
| 非破壞性修正 | 內部文件不更改；新對外文件使用 `mrliouai`；透過 `NAMING_MIGRATION_REGISTRY.yml` 整合登錄 |
| 驗收標準 | 所有對外公開文件使用 `mrliouai`；內部文件保留不變；所有名稱均在 Registry 登錄；自動驗證通過 |

**各名稱角色與整合方向：**

| 名稱 | 角色 | 整合方向 |
|------|------|---------|
| `mrliouai` | 唯一對外產品名稱（canonical） | ← 所有對外使用指向此處 |
| `mRLiouAI` | 內部拼寫（保留） | 保留為內部資料；不用於對外 |
| `MRLiouAI` | 內部拼寫（保留） | 保留為內部資料；不用於對外 |
| `MrLiou AI` | 內部拼寫（保留） | 保留為內部資料；不用於對外 |
| `MrLiouWord` | origin signature（保留） | 保留為 signature；不作為對外產品名稱 |
| `MRL` | 內部縮寫（保留） | 保留為內部識別；不作為對外品牌 |

---

## C002 — Single Source of Truth 層級：dofaromg/----2 vs. flow-tasks Root Law vs. flow-tasks-01 Authority Pack

| 欄位 | 值 |
|------|----|
| 嚴重度 | High |
| 來源 | `dofaromg/----2 main`、`dofaromg/flow-tasks` Root Law、`dofaromg/flow-tasks-01` Authority Pack 各自聲明治理基準 |
| 現況 | 三個儲存庫各有不同層次的 Root／Authority 聲明，可能引起哪個是「唯一真實來源」的混淆 |
| Canonical 裁定 | **層級裁定**：`dofaromg/.github`（本儲存庫）為整個帳號的頂層中央治理索引；`dofaromg/----2` 為治理核心儲存庫（包含 SOVEREIGNTY、NAMING 等）；`flow-tasks` Root Law 為原始立法紀錄；`flow-tasks-01` Authority Pack 為技術實作層。三者不互相矛盾，而是不同層次的互補文件。唯一 Root 仍為 `@dofaromg`。 |
| 非破壞性修正 | 在各儲存庫的 README／治理文件中加入指向 `dofaromg/.github` 的參考；不刪除各 repo 的現有治理文件 |
| 驗收標準 | 各儲存庫治理文件均明確標示其層次定位；無文件聲稱自己是唯一全域最終來源而無視其他層次 |

---

## C003 — AUTHORITY_ROOT.md repo-scope 限制 vs. 全域 Root 主張

| 欄位 | 值 |
|------|----|
| 嚴重度 | Low |
| 來源 | `dofaromg/flow-tasks-01/AUTHORITY_ROOT.md` 明確聲明「不主張其他外部系統」 |
| 現況 | 該文件 scope 限定為 `flow-tasks-01`，但 `@dofaromg` 的全域 Root 主張涵蓋整個帳號 |
| Canonical 裁定 | `AUTHORITY_ROOT.md` 的 repo-scope 限制是技術上的謹慎聲明（避免聲稱對 GitHub 平台或他人資產的控制），不等於否定 `@dofaromg` 在其帳號範圍內的全域 Root 身分。兩者不矛盾。 |
| 非破壞性修正 | 無需修改原文件；在本 CONFLICT_MATRIX 中記錄此區分即可 |
| 驗收標準 | 任何新治理文件引用此限制時，必須同時說明此區分；不得將 repo-scope 限制誤解為否定全域 Root |

---

## C004 — 外部來源「保存 provenance」vs.「不得在公開產品顯化」

| 欄位 | 值 |
|------|----|
| 嚴重度 | High |
| 來源 | 治理要求同時保存外部來源 provenance 紀錄（供應鏈追蹤）且禁止供應商名稱出現在公開展示層 |
| 現況 | 可能在同一 repo 或文件中，既有來源紀錄（符合要求），又有對外可見的供應商名稱（違反要求） |
| Canonical 裁定 | **兩層並存**：受控內部資料層保存完整 provenance 與供應鏈紀錄（必須保留）；公開展示層只呈現 `mrliouai`，禁止供應商名稱、`Powered by`、provider metadata（絕對禁止）。治理透明指變更、核准、證據與稽核透明，不表示公開內部供應商資料。 |
| 非破壞性修正 | 審查現有公開 API/README，將供應商資料移至內部資料層或 `.gitignore`/private 路徑；不刪除內部來源紀錄 |
| 驗收標準 | 自動驗證通過：公開路徑不含 `Powered by` 或受限制供應商欄位；內部資料層保存完整 provenance |

---

## C005 — 現有公開 API/README 中供應商名稱洩漏風險

| 欄位 | 值 |
|------|----|
| 嚴重度 | High |
| 來源 | `dofaromg/mrliouword-system/AI_PROVIDERS_README.md`（E020）及其他可能存在供應商名稱的公開文件 |
| 現況 | `AI_PROVIDERS_README.md` 記錄供應商資訊；尚需確認此文件是否位於公開路徑 |
| Canonical 裁定 | 若此文件可公開存取，須評估是否需要移入受控內部資料層或加密；供應商名稱不得出現在公開 UI、API 回應或對外 README |
| 非破壞性修正 | 不刪除文件；評估可見性後，以 `public-internal-boundary.json` 中的路徑規則控管；必要時移入私有目錄 |
| 驗收標準 | 自動掃描公開路徑不含 `Powered by`、provider endpoint 或明確受限制供應商欄位；`AI_PROVIDERS_README.md` 可見性已確認並合規 |

---

## C006 — 既有獨立 Verifier／雙 Gate vs. 唯一 Root 最終裁決

| 欄位 | 值 |
|------|----|
| 嚴重度 | Medium |
| 來源 | `INTERNAL_GATE.yaml`（E008）、`ACCEPTANCE_GATE.yaml`（E009）等技術 Gate 獨立運作 |
| 現況 | 技術 Gate 可能在 Root 未明確參與的情況下自動核准或拒絕變更 |
| Canonical 裁定 | 技術 Gate 是 Root 授權的執行機制，不是獨立的核准權威；Gate 的「核准」等同於 Root 預授權的範圍；Gate 拒絕的項目停止並回報；超出 Gate 規則的情況必須回交 Root 決定；Gate 不能創建新例外或修改自身規則 |
| 非破壞性修正 | 在 Gate YAML 中加入說明，明確標示 Gate 是 Root 授權的執行層，不是最終決策者 |
| 驗收標準 | Gate 文件明確記載其執行層地位；無 Gate 可自行修改自身規則或創建例外 |

---

## C007 — .env.deploy 中 NEXT_PUBLIC_APP_NAME=MRLiouAI（內部拼寫）整合說明

| 欄位 | 值 |
|------|----|
| 嚴重度 | Low |
| 來源 | `dofaromg/mrliouword-system/deploy/.env.deploy`（E019）：`NEXT_PUBLIC_APP_NAME=MRLiouAI` |
| 現況 | `MRLiouAI` 為內部拼寫，依新裁定保留為內部資料；若此值影響公開 UI 顯示，則須更新為 `mrliouai` |
| Canonical 裁定 | `MRLiouAI` 屬於內部識別符，保留不強制更改；若 `NEXT_PUBLIC_APP_NAME` 的值會直接顯示於對外公開介面，則需更新為 `mrliouai`；若僅為內部部署識別，則登錄為已知內部用法，無需強制遷移 |
| 非破壞性修正 | 不直接改寫歷史 commit；在 `NAMING_MIGRATION_REGISTRY.yml` 登錄；待下次部署時由 Root 決定是否更新 |
| 驗收標準 | 已登錄；公開介面若顯示此值需確認為 `mrliouai`；歷史 commit 保留不改寫 |

---

## C008 — 歷史內部拼寫保留 vs. 對外名稱統一

| 欄位 | 值 |
|------|----|
| 嚴重度 | Low |
| 來源 | 歷史文件中大量內部拼寫，對外需統一為 `mrliouai` |
| 現況 | 內部文件有多種拼寫，對外文件要求使用 `mrliouai` |
| Canonical 裁定 | 非破壞性整合規則：①不更改內部文件；②不刪除任何歷史文件；③新對外文件使用 `mrliouai`；④所有名稱均在 `NAMING_MIGRATION_REGISTRY.yml` 登錄；⑤若有歧義，加注說明指向 `mrliouai` |
| 非破壞性修正 | 遵循上述五點規則即可 |
| 驗收標準 | 無歷史文件被刪除；無強制全域批次 rename；`NAMING_MIGRATION_REGISTRY.yml` 涵蓋所有已知名稱 |
