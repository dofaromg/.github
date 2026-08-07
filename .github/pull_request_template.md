## Pull Request Checklist — mrliouai Governance

請在提交前確認以下每一項。未完成項目須說明原因。

### 1. Root 與身分
- [ ] 本次變更不影響唯一 Root `@dofaromg` 的地位或權限
- [ ] 未建立第二 Root、平行核准流程或例外授權
- [ ] AI 或自動化未自行建立授權

### 2. Canonical 名稱
- [ ] 對外公開內容使用 `mrliouai`（全小寫，大小寫完全一致）
- [ ] 未在公開層使用內部識別符（`MRL`、`mRLiouAI`、`MRLiouAI`、`MrLiouWord`）
- [ ] 若有新命名需求，已登錄至 `governance/NAMING_MIGRATION_REGISTRY.yml`

### 3. 公開／內部邊界
- [ ] 公開路徑不含供應商名稱、`Powered by` 或 provider metadata
- [ ] 供應商與 API 資料僅存在受控內部資料層
- [ ] `governance/PUBLIC_INTERNAL_BOUNDARY.md` 範圍未受影響，或已同步更新

### 4. Evidence Index
- [ ] 未新增治理證據，或已更新 `governance/EVIDENCE_INDEX.md` 與 `governance/evidence-index.json`（兩者同步）
- [ ] 所有新增 evidence 使用固定 40 字元 SHA permalink

### 5. Conflict Matrix
- [ ] 未引入新命名衝突，或已在 `governance/CONFLICT_MATRIX.md` 新增對應衝突項目
- [ ] 每項衝突均有 canonical 裁定與驗收標準

### 6. 歷史保留
- [ ] 未刪除任何歷史文件、`LICENSE`、`NOTICE`、`AUTHORS`
- [ ] 未改寫 Git 歷史
- [ ] 未執行未登錄的全域批次 rename

### 7. 驗證
- [ ] CI 驗證通過（`validate-governance.yml`）
- [ ] 無 fail-closed 觸發未解除

---

**影響範圍摘要**（請填寫）：

> 本次 PR 影響：

**衝突狀態**（請填寫）：

> 無衝突 / 已在 CONFLICT_MATRIX 登錄：
