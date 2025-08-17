# Requirements Document

## Introduction

《電馭寫作》是一個數位化寫作輔助工具，旨在將寫作流程系統化為七個明確階段：選題、發想、備料、標題、前言、主體、收尾。系統採用主專案包含多個子專案的架構，每個子專案代表一篇獨立的文章創作，都遵循相同的七階段寫作流程。每個階段都有特定目標、AI提詞工具和預期產出，幫助使用者更有效率地完成高品質文章創作。

## Requirements

### Requirement 1

**User Story:** 作為一個寫作者，我希望能夠按照七個階段的流程進行寫作，這樣我就能更有系統地完成文章創作。

#### Acceptance Criteria

1. WHEN 使用者開始新的寫作專案 THEN 系統 SHALL 顯示七個寫作階段的導航介面
2. WHEN 使用者選擇任一階段 THEN 系統 SHALL 顯示該階段的目標說明和操作介面
3. WHEN 使用者完成一個階段 THEN 系統 SHALL 自動保存進度並允許進入下一階段
4. WHEN 使用者想要回到之前的階段 THEN 系統 SHALL 允許自由切換並保留之前的內容

### Requirement 2

**User Story:** 作為一個寫作者，我希望每個階段都有專門的AI提詞助手，這樣我就能獲得針對性的創作建議。

#### Acceptance Criteria

1. WHEN 使用者進入「選題」階段 THEN 系統 SHALL 提供選題助手來幫助確定文章主題
2. WHEN 使用者進入「發想」階段 THEN 系統 SHALL 提供發想助手來協助產生創意點子
3. WHEN 使用者進入「備料」階段 THEN 系統 SHALL 提供備料助手來整理相關資料和素材
4. WHEN 使用者進入「標題」階段 THEN 系統 SHALL 提供《爆款文標題大師》來生成吸引人的標題
5. WHEN 使用者進入「前言」階段 THEN 系統 SHALL 提供前言助手來撰寫引人入勝的開頭
6. WHEN 使用者進入「主體」階段 THEN 系統 SHALL 提供主體助手來組織文章結構和內容
7. WHEN 使用者進入「收尾」階段 THEN 系統 SHALL 提供收尾助手來完成有力的結論

### Requirement 3

**User Story:** 作為一個寫作者，我希望能夠管理多個子專案，這樣我就能同時進行不同文章的創作，每個子專案都有獨立的資料夾結構。

#### Acceptance Criteria

1. WHEN 使用者創建新子專案 THEN 系統 SHALL 要求輸入專案名稱並在主專案下建立獨立的子資料夾
2. WHEN 使用者有多個子專案 THEN 系統 SHALL 在首頁顯示所有子專案列表及其進度狀態
3. WHEN 使用者選擇子專案 THEN 系統 SHALL 載入該子專案的七階段內容和進度
4. WHEN 使用者想要刪除子專案 THEN 系統 SHALL 要求確認並完全移除子專案資料夾
5. WHEN 系統建立子專案 THEN 系統 SHALL 自動建立七個階段對應的檔案結構

### Requirement 4

**User Story:** 作為一個寫作者，我希望系統能夠保存我的創作內容和進度，這樣我就不會遺失任何工作成果。

#### Acceptance Criteria

1. WHEN 使用者在任何階段輸入內容 THEN 系統 SHALL 自動保存到本地存儲
2. WHEN 使用者關閉應用程式後重新開啟 THEN 系統 SHALL 恢復之前的工作狀態
3. WHEN 使用者完成所有階段 THEN 系統 SHALL 提供匯出完整文章的功能
4. IF 系統發生錯誤 THEN 系統 SHALL 保護使用者資料不遺失

### Requirement 5

**User Story:** 作為一個寫作者，我希望介面簡潔直觀，這樣我就能專注於創作而不被複雜操作干擾。

#### Acceptance Criteria

1. WHEN 使用者首次使用 THEN 系統 SHALL 提供簡單的引導說明
2. WHEN 使用者在任何頁面 THEN 系統 SHALL 清楚顯示當前階段和整體進度
3. WHEN 使用者需要幫助 THEN 系統 SHALL 在每個階段提供使用提示
4. WHEN 使用者使用手機或平板 THEN 系統 SHALL 提供響應式設計適配不同螢幕

### Requirement 6

**User Story:** 作為一個寫作者，我希望能夠自訂AI提詞的風格和偏好，這樣我就能獲得更符合個人需求的建議。

#### Acceptance Criteria

1. WHEN 使用者進入設定頁面 THEN 系統 SHALL 允許調整AI助手的回應風格
2. WHEN 使用者設定寫作類型偏好 THEN 系統 SHALL 根據偏好調整各階段的建議
3. WHEN 使用者有特定的寫作習慣 THEN 系統 SHALL 允許自訂提詞模板
4. WHEN 使用者儲存設定 THEN 系統 SHALL 在所有專案中應用這些偏好設定
### R
equirement 7

**User Story:** 作為一個寫作者，我希望每個子專案都有標準化的資料夾結構，這樣我就能清楚地組織和管理每篇文章的創作素材。

#### Acceptance Criteria

1. WHEN 系統建立新子專案 THEN 系統 SHALL 建立包含七個階段資料夾的標準結構
2. WHEN 使用者進入任一階段 THEN 系統 SHALL 自動載入對應資料夾中的內容檔案
3. WHEN 使用者在階段中產生內容 THEN 系統 SHALL 將內容保存到對應的階段資料夾中
4. WHEN 使用者查看子專案 THEN 系統 SHALL 顯示每個階段資料夾的完成狀態
5. IF 子專案資料夾結構不完整 THEN 系統 SHALL 自動補齊缺失的階段資料夾

### Requirement 8

**User Story:** 作為一個寫作者，我希望能夠在檔案系統中直接查看和編輯子專案內容，這樣我就能使用其他工具配合寫作流程。

#### Acceptance Criteria

1. WHEN 使用者在檔案管理器中查看專案 THEN 系統 SHALL 使用清楚的資料夾命名和結構
2. WHEN 使用者直接編輯階段檔案 THEN 系統 SHALL 在下次載入時反映這些變更
3. WHEN 使用者複製子專案資料夾 THEN 系統 SHALL 能夠識別並載入複製的專案
4. WHEN 使用者備份專案 THEN 系統 SHALL 確保所有階段內容都包含在資料夾結構中