# Small Business Japan Plugin

Small Business Japan は、Anthropic の open-source Small Business plugin の
日本向け companion です。本家と同じように、自然文で入る router、15個の
target workflow command、15個の output contract、starter executable skill、
そして「送信・投稿・支払・申請・更新・外部共有の前に必ず承認で止まる」
設計を持ちます。

日本版が扱うのは、日本の小さな会社で実際に起きるバックオフィス作業です。
会計export、銀行CSV、請求書PDF、メールスレッド、スクリーンショット、CRM
spreadsheet、そして税理士・社労士・行政書士・弁護士へ渡せる確認メモを前提に
します。

最初からlive connectorを使う必要はありません。まずは1つのファイル、1つの
export、1つの貼り付けたメールから始められます。plugin は「いま何ができるか」
と「次につなぐと便利なoptional connector」を分けて案内します。

> **重要**: この plugin は、ドラフト、チェックリスト、論点メモ、オーナー確認用
> の士業連携パケットを作るためのものです。金融・税務・法律・労務・人事・
> 行政書士業務の助言を提供するものではありません。代理、代行、提出、最終判断、
> 資格者表示、外部送信は行いません。外部に送るものは、必ずあなたの明示承認で
> 止まります。

## Installation

Small Business Japan は `@agentgymleader` による community contribution です。
upstream maintainerに採用されるまでは、配布経路は非公式です。

### Cowork

想定: companion packageとして、Codex Web UI Interface Plugin と同じ
prompt-driven `npx` helper flowでreadinessを確認し、hostにlocal plugin treeを読ませます。

### Claude Code

`npx` を一時的なcommand runnerとして使います。

```bash
npx @agentgymleader/small-business-japan doctor
npx @agentgymleader/small-business-japan print-claude-code-prompt
```

npm公開前のlocal developmentでは、同じ確認をrepo内のfileから実行します。

```bash
node bin/small-business-japan.js doctor
node bin/small-business-japan.js print-claude-code-prompt
```

出力されたpromptをClaude Codeへ貼り付けます。そのpromptは、Claude Code自身に
確認を実行させ、Small Business Japanをupstream採用前のcommunity contribution
として扱わせます。

connector-free local smoke test:

```bash
claude plugin validate .
python scripts/validate_small_business_japan.py
```

日本語の貼り付けpromptは `docs/install/claude-code-install-prompt.ja.md` にあります。

### Data privacy

このpackは銀行CSV、請求書PDF、顧客メール、貼り付けた事業contextから動きます。
それらには個人情報、顧客情報、機密情報が含まれることがあります。利用するLLMや
組織のdata policyに従い、不要な情報は削除し、secret、token、private repoの中身、
内部URLは貼り付けないでください。

## What you'll need to connect

`/smb-onboard-jp` を実行するか、Claude に「初期設定して」と頼んでください。

日本版では "connect" を、利用可能なlive connectorだけでなく、CSV export、
uploaded PDF、貼り付けた表、コピーしたemail threadを渡すことまで含めて扱います。
live connectorはoptionalです。

**Core tools** 最初につなぐ、またはexportを渡すと便利なもの:

- **会計export**: freee、Money Forward Cloud、弥生、その他の会計toolからの
  export。
- **銀行CSV・決済export**: 入出金、振込、カード決済、Stripe、PayPal、Square、
  STORES、AirPAYなど。
- **請求書file・請求一覧**: PDF、CSV、請求書folder、Misoca、Money Forward
  Cloud請求書、freee請求書、弥生、Stripe Invoicingなどからのexport。

**Marketing & communication:**

- **Gmail / Outlook**: 顧客メール、督促文面、契約の背景、クレーム返信のdraft。
- **Google Calendar / Outlook Calendar**: 週次予定、顧客follow-up、オーナーの
  reminder。
- **HubSpot、kintone、Salesforce、Notion、spreadsheet**: lead、CRM整理、
  campaign、顧客list。
- **Google Drive / OneDrive**: 請求書、領収書、契約書、template folder。
- **Slack / Chatwork**: host環境が対応している場合の社内briefやfollow-up note。

**Optional** つなぐ、またはcontextを渡すと深くなるもの:

- Canva、Figma、Google Slides、newsletter tool、social tool は handoff 先として
  使えます。
- Small Business Japan は Japan-only Canva skill を必須にしません。本家 Small
  Business の Canva workflow が使える場合は、upstream alias または handoff 先と
  して扱います。
- 税理士、社労士、行政書士、弁護士、記帳代行、バックオフィスpartner。
- いつも相談している質問と、相手が好む形式: email、memo、spreadsheet、
  PDF packet、folder。

全部なくても始められます。最初の価値は、1つのexport、1つのuploaded file、
1つの貼り付けた文章から出るべきです。

## What it outputs

v0は memo-only です。Claude Codeから、特定tool向けimport CSV、請求書発行file、
会計仕訳data、CRM更新file、送信用email fileは出しません。

出してよいoutput container:

- 確認メモ。
- 承認前のドラフト文面。
- チェックリスト。
- 税理士・社労士・行政書士・弁護士への確認パケット。

抽出項目候補、missing data、risk / escalation note は、これらのcontainer内の
sectionとしてだけ出します。独立した成果物にはしません。

ownerが特定tool向けCSVを求めた場合は、CSVそのものではなくfield-mapping memoを
作り、importはownerと必要な専門家が確認した後にtarget tool内で行うよう案内します。

## How it works

3つのlayerで動きます。

1. **Skills** は building block です。資金繰りを見る、請求督促draftを作る、
   税理士向けmemoを作る、契約の論点listを作る、のように1つの仕事に集中します。

2. **Commands** は workflow です。複数のskillをつなぎ、途中で承認checkpointを
   置き、どの根拠を使ったかを見せながら次のactionを提案します。

3. **Router** は入口です。「税理士に何を渡せばいい?」「来月キャッシュ足りる?」
   「クレーム返信を書いて」「この契約書見て」のように自然文で言うと、Claude が
   近いworkflowを選び、最小限のinputを聞きます。

## All 15 commands

Commands は複数のskillをつなぐworkflowです。どれも外部actionの前に止まる設計
です。Starter Packで現在入れているのは入口skillとrouter skillの
`smb-onboard-jp` / `smb-router-jp` です。下のcommand tableは日本向けtarget setで、
public command nameは日本語です。ASCIIのskill slugはfilesystem上の内部識別子として
残します。`SKILL.md` がないcommandは実装前のroadmap entryとして扱います。

### Money & finance

| Command | English alias | What it does | Just say... | Skills used | Required | Optional |
|---|---|---|---|---|---|---|
| `/支払準備` | `plan-payroll-jp` | 30日のcashと支払予定の資料整理packet。未入金請求も見る。 | "来月の支払い資料を整理して", "cash is tight", "支払予定を確認したい" | `cash-flow-snapshot-jp`, `invoice-chase-jp` | 会計exportまたは銀行CSV | 支払日、請求一覧、Stripe / PayPal export |
| `/来月資金` | `month-heads-up-jp` | 次の30日の資金繰りと早期risk flag。 | "来月どう?", "資金繰り見て", "month-ahead cash" | `cash-flow-snapshot-jp` | 会計exportまたは銀行CSV | 請求一覧、決済processor CSV |
| `/月次締め準備` | `close-month-jp` | 税理士review向けの月次self-check memo。 | "月末締めたい", "税理士に確認するための資料準備を支援して" | `month-end-prep-jp` | 会計exportまたはledger CSV | 銀行CSV、請求書PDF、領収書folder |
| `/価格確認` | `price-check-jp` | 利益率と価格scenario。前提と判断を分ける。 | "値上げしていい?", "利益率見て", "pricing check" | `margin-analyzer-jp` | 売上 / 原価export | 商品list、store export、手数料list |
| `/税理士確認パケット` | `tax-prep-jp` | 税理士向け資料checklistと論点memo。 | "税理士に何を渡せばいい?", "消費税の確認資料を整理して" | `tax-season-organizer-jp` | 会計export | 請求一覧、外注先list、報酬支払記録 |

### Sales & marketing

| Command | English alias | What it does | Just say... | Skills used | Required | Optional |
|---|---|---|---|---|---|---|
| `/営業連絡リスト` | `call-list-jp` | 今日連絡すべき顧客 / lead とtalking point。 | "今日誰に連絡する?", "hot leads", "営業リスト作って" | `lead-triage-jp` | CRM exportまたはspreadsheet | Gmail、calendar、Slack / Chatwork |
| `/キャンペーン準備` | `run-campaign-jp` | 売上contextからcampaign brief、日本語copy draft、承認付きsend planへ。 | "キャンペーン作って", "売上落ちてる", "何を告知する?" | `content-strategy-jp`, `lead-triage-jp` | content brief | CRM、売上CSV、newsletter / social tool、本家Canva workflow |
| `/売上ブリーフ` | `sales-brief-jp` | 売れているもの / 落ちているものと2週間promotion brief。 | "何が売れてる?", "何を推す?", "sales brief" | `content-strategy-jp` | 売上export | 決済export、在庫memo |

### Customers & operations

| Command | English alias | What it does | Just say... | Skills used | Required | Optional |
|---|---|---|---|---|---|---|
| `/顧客の声確認` | `customer-pulse-check-jp` | 顧客feedbackとcomplaint theme、返信template。 | "お客さん何て言ってる?", "レビュー見て", "complaints" | `customer-pulse-jp`, `ticket-deflector-jp` | review / ticket / email貼り付け | HubSpot、Gmail、PayPal / Stripe |
| `/クレーム返信準備` | `handle-complaint-jp` | クレーム返信packet。context、draft、option、運用fix。 | "クレーム返信を書いて", "angry customer", "返金すべき?" | `ticket-deflector-jp`, `customer-pulse-jp` | complaint貼り付け | 注文 / 決済export |
| `/CRM整理` | `crm-cleanup-jp` | 古いdeal、重複、欠損field、承認付きupdate plan。 | "CRM整理して", "HubSpotが散らかってる" | `crm-maintenance-jp` | CRM export | Gmail、calendar |
| `/契約論点確認` | `review-contract-jp` | 契約・見積・発注・NDAの平易な日本語論点memo。 | "この契約書見て", "NDA確認して", "発注書レビュー" | `contract-review-jp` | uploaded file | CloudSign / GMO Sign / DocuSign、email thread |

### Business intelligence

| Command | English alias | What it does | Just say... | Skills used | Required | Optional |
|---|---|---|---|---|---|---|
| `/月曜ブリーフ` | `monday-brief-jp` | cash、未入金、顧客issue、士業task、top decisionの月曜brief。 | "今週何から?", "Monday brief", "今週の経営メモ" | `business-pulse-jp` | なし | 会計、請求、calendar、email、Slack / Chatwork |
| `/金曜ふりかえり` | `friday-brief-jp` | 週末pulse。売上、回収、wins、watch item、翌週reminder。 | "今週どうだった?", "Friday recap" | `business-pulse-jp` | 1 data source | 売上、CRM、calendar |
| `/四半期レビュー` | `quarterly-review-jp` | オーナー、税理士、advisor向け四半期narrative。 | "四半期レビュー", "QBR", "振り返り作って" | `business-pulse-jp` | 会計または売上export | CRM、決済export |

## All 15 skills

Skills はatomicなbuilding blockです。下の表はoutput contractに裏付けられた日本版の
target skill surfaceです。このstarterで実行可能な `SKILL.md` として入れているのは
`smb-onboard-jp` と `smb-router-jp` で、それ以外は実装前のcontractとして扱います。

### Money & finance

| Skill | What it does | Just say... | Required | Optional |
|---|---|---|---|---|
| **cash-flow-snapshot-jp** | 30 / 60 / 90日のcash view。confidence note、支払cycle risk、missing-data question付き。 | "資金繰り資料を整理して", "runway", "来月の支払予定を見たい" | 会計export、銀行CSV、または決済export | 請求一覧、固定費list |
| **invoice-chase-jp** | 未入金請求のdraft-only督促packet。対象、理由、根拠、risk、承認pauseを出す。 | "未入金を追いたい", "who owes me money" | 請求書PDF / CSVまたは請求一覧 | email thread、支払履歴 |
| **margin-analyzer-jp** | 利益率と価格scenario。税込 / 税抜の前提を明示。 | "利益率見て", "値上げ判断材料" | 売上 / 原価export | platform fee、送料、外注費 |
| **month-end-prep-jp** | 税理士review向け月次packet。gap、領収書、未分類、質問。 | "月次締め", "経理資料整理" | 会計exportまたはledger CSV | 銀行CSV、請求書folder、領収書folder |
| **tax-season-organizer-jp** | 税務時期・年末向け資料checklistと税理士handoff memo。 | "税理士パケット作って", "年末資料" | 会計export | 外注先list、請求一覧、報酬支払記録 |

### Sales & marketing

| Skill | What it does | Just say... | Required | Optional |
|---|---|---|---|---|
| **lead-triage-jp** | 顧客 / leadを優先度とfitで並べ、日本語follow-up draftを作る。 | "誰に連絡する?", "営業優先順位" | CRM exportまたはspreadsheet | Gmail、calendar |
| **content-strategy-jp** | 売上・顧客signalからcampaign briefと日本語copy angleを作る。 | "何を告知する?", "投稿案" | 売上exportまたはbrief | CRM、newsletter / social tool |
| **design-tool-handoff-jp** | design handoff memo と asset checklistを作り、必要なら本家Small Business Canva workflowへ渡す。 | "Canvaに渡せる形にして" | 承認済みcontent brief | Canva、Figma、Slides、designer |

### Customers & operations

| Skill | What it does | Just say... | Required | Optional |
|---|---|---|---|---|
| **customer-pulse-jp** | review、ticket、dispute、email sentimentをthemeとnext actionにまとめる。 | "顧客の声まとめて" | review / ticket / email貼り付け | HubSpot、Gmail、決済export |
| **ticket-deflector-jp** | order / payment context付きで顧客返信draftとapproval checklistを作る。 | "返信ドラフト", "返金案" | complaint貼り付け | 注文 / 決済export |
| **crm-maintenance-jp** | 古いrecord、重複、欠損field、承認付きCRM update planを出す。 | "CRM掃除して" | CRM export | Gmail、calendar |
| **contract-review-jp** | 契約、見積、発注書、NDA、注文書の平易な日本語issue memo。 | "契約レビュー", "発注書確認" | uploaded fileまたはpasted text | email thread、電子契約envelope |

### Hiring

| Skill | What it does | Just say... | Required | Optional |
|---|---|---|---|---|
| **job-post-builder-jp** | 求人票、interview guide、scoring rubric、offer checklist、社労士への質問を作る。 | "採用したい", "求人票作って" | role description | Drive folder、過去求人 |

### Business intelligence & onboarding

| Skill | What it does | Just say... | Required | Optional |
|---|---|---|---|---|
| **business-pulse-jp** | cash、未入金、売上、顧客、今週、士業task、top decisionの1-page owner snapshot。 | "経営の現状見て", "weekly summary" | なし。graceful degradation | 会計、CRM、email、calendar |
| **smb-onboard-jp** | tool、file、事業context、困りごと、最初のworkflow、weekly check-inを整理する入口。 | "初期設定して", "set me up" | なし | すべてのconnectorとfile |

## Customizing

これらのworkflowは出発点です。あなたの事業に合わせるほど使いやすくなります。

- **事業contextを足す**: 業種、商品、顧客type、支払cycle、請求慣行、定期vendor、
  顧問士業。
- **thresholdを調整する**: 最低cash buffer、督促timing、顧客follow-up cadence、
  review threshold。
- **connectorを差し替える**: いま使っている会計、請求、CRM、決済、calendar、
  file toolを使う。
- **handoff formatを選ぶ**: email memo、checklist、spreadsheet packet、PDF folder、
  pasted summary。
- **承認gateを守る**: send、post、refund、CRM write、契約変更、給与判断、申請、
  士業連絡はowner approvalの下に置く。
