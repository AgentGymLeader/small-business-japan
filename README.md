> 🇯🇵 **日本語で読む → [README.ja.md](README.ja.md)**
>
> 日本の中小企業・個人事業主向けの Claude Code プラグインです。15 のコマンド・15 のスキルを日本の商慣習と法令に準拠して収録しています。

🇺🇸 English version below.

# Small Business Japan Plugin

Small Business Japan is a Japan-local companion to Anthropic's open-source
Small Business plugin. It keeps the same basic shape: a plain-language router,
15 target workflow commands, 15 output contracts, starter executable skills, and
approval checkpoints before anything is sent, posted, paid, filed, updated, or
shared with someone else.

The Japan version focuses on how Japanese owners actually run back-office work:
accounting exports, bank CSVs, invoice PDFs, email threads, screenshots, CRM
spreadsheets, and handoff memos for accountants, labor and social insurance
attorneys, administrative scriveners, and counsel.

You do not need live connectors before starting. Start with one file, one
export, or one pasted thread. The plugin will tell you what it can do now and
which optional connector would unlock more later.

> **Important**: This plugin helps prepare drafts, checklists, issue memos, and
> owner-reviewed handoff packets. It does not provide financial, tax, legal,
> labor, HR, or administrative-scrivener advice. It does not represent you,
> submit filings, make final determinations, display professional credentials,
> or send anything externally without your explicit approval.

## Installation

Small Business Japan is a community contribution by `@agentgymleader`. Until
upstream maintainers adopt it, treat the distribution channel as unofficial.

### Cowork

Paste this prompt directly into Cowork:

```
Please set up Small Business Japan on this machine.

Use this package name:
@agentgymleader/small-business-japan

This is a community contribution by @agentgymleader and has not been adopted into the marketplace yet.

Check node/npm/npx, run doctor, and run a connector-free dry run.

Do not send, file, post, pay, update CRM, or submit anything to an external service.
Do not print tokens, API keys, private repo contents, customer data, or internal URLs.
```

### Claude Code

Paste the same prompt into Claude Code, or use the Japanese prompt in
`docs/install/claude-code-install-prompt.ja.md`.

For manual installation:

```bash
npx @agentgymleader/small-business-japan doctor
npx @agentgymleader/small-business-japan print-claude-code-prompt
```

Then paste the printed prompt into Claude Code.

### Data privacy

This pack works from bank CSVs, invoice PDFs, customer emails, and pasted
business context. Those inputs may contain personal data, customer data, or
confidential business information. Follow your organization's AI/data policy,
redact unnecessary details, and do not paste passwords, API keys, private
repository contents, or internal URLs.

## What you'll need to connect

Run `/smb-onboard-jp` or ask Claude to set you up.

In this Japan-local version, "connect" includes live connectors where available
and file-based paths such as CSV exports, uploaded PDFs, pasted tables, and
copied email threads. Live connectors are optional.

**Core tools** connect or export these first for the best experience:

- **Accounting exports** from freee, Money Forward Cloud, Yayoi, or another
  accounting tool.
- **Bank CSVs and payment exports** for cash, deposits, transfers, card
  payments, Stripe, PayPal, Square, STORES, AirPAY, or similar services.
- **Invoice files and registers** such as PDFs, CSVs, invoice folders, or lists
  exported from Misoca, Money Forward Cloud Invoice, freee invoices, Yayoi,
  Stripe Invoicing, or another tool.

**Marketing & communication:**

- **Gmail / Outlook** for pasted or connected customer threads, payment
  reminders, contract context, and complaint drafts.
- **Google Calendar / Outlook Calendar** for weekly commitments, customer
  follow-ups, and owner reminders.
- **HubSpot, kintone, Salesforce, Notion, or spreadsheets** for leads, CRM
  hygiene, campaigns, and customer lists.
- **Google Drive / OneDrive** for folders of invoices, receipts, contracts, and
  templates.
- **Slack / Chatwork** for internal brief delivery or follow-up notes, where the
  host environment supports it.

**Optional** adds depth when connected or provided:

- Canva, Figma, Google Slides, newsletter tools, and social tools can be used as
  handoff destinations.
- Small Business Japan does not require a Japan-only Canva skill. If the
  original Small Business Canva workflow is available, this plugin can treat it
  as an upstream alias or handoff target.
- Your accountant, labor and social insurance attorney, administrative
  scrivener, lawyer, or back-office partner context.
- The questions you usually send professionals and the format they prefer:
  email, memo, spreadsheet, PDF packet, or folder.

You do not need all of these to start. The first useful path should work from a
single export, uploaded file, or pasted message.

## What it outputs

v0 is memo-only. Claude Code should not produce tool-specific import CSVs,
invoice-issuing files, accounting journal data, CRM update files, or send-ready
mail files.

Allowed output containers:

- review memo.
- draft wording for owner approval.
- checklist.
- accountant / labor and social insurance attorney / administrative scrivener /
  lawyer confirmation packet.

Extracted-field candidates, missing-data lists, and risk / escalation notes may
appear only as sections inside those containers, not as standalone deliverables.

If the owner asks for a CSV for a specific tool, produce a field-mapping memo
and tell them to complete the import inside the target tool after owner and
professional review.

## How it works

Three layers work together:

1. **Skills** are the building blocks. Each skill does one focused job, such as
   summarizing cash flow, drafting invoice reminders, preparing an accountant
   memo, or making a contract issue list.

2. **Commands** are workflows. They chain skills into practical owner tasks,
   pause at checkpoints, and show what evidence was used before recommending
   the next step.

3. **The router** is the front door. You can ask in plain Japanese or English:
   "税理士に何を渡せばいい?", "cash is tight", "this customer is angry", or
   "review this contract." Claude picks the closest workflow and asks for the
   minimum useful input.

## All 15 commands

Commands are workflows that chain skills together. Each one is designed to pause
before external action. Public command names are Japanese; ASCII skill slugs
remain internal filesystem identifiers. All 15 commands have a corresponding
`SKILL.md` and are ready to use.

### Money & finance

| Command | English alias | What it does | Just say... | Skills used | Required | Optional |
|---|---|---|---|---|---|---|
| `/支払準備` | `plan-payroll-jp` | 30-day cash and payroll documentation review packet with overdue invoice review. | "来月の支払い資料を整理して", "cash is tight", "支払予定を確認したい" | `cash-flow-snapshot-jp`, `invoice-chase-jp` | accounting export or bank CSV | payroll date, invoice register, Stripe / PayPal exports |
| `/来月資金` | `month-heads-up-jp` | Next 30-day cash outlook with early risk flags and missing-data notes. | "来月どう?", "資金繰り見て", "month-ahead cash" | `cash-flow-snapshot-jp` | accounting export or bank CSV | invoice register, payment processor CSV |
| `/月次締め準備` | `close-month-jp` | Month-end self-check memo for accountant review. | "月末締めたい", "税理士に確認するための資料準備を支援して" | `month-end-prep-jp` | accounting export or ledger CSV | bank CSV, invoice PDFs, receipt folder |
| `/価格確認` | `price-check-jp` | Margin and pricing scenario packet with assumptions separated from decisions. | "値上げしていい?", "利益率見て", "pricing check" | `margin-analyzer-jp` | sales / cost export | product list, store export, fee list |
| `/税理士確認パケット` | `tax-prep-jp` | Owner-prepared tax-accountant document checklist and issue memo. | "税理士に何を渡せばいい?", "消費税の確認資料を整理して" | `tax-season-organizer-jp` | accounting export | invoice register, contractor list, professional fee records |

### Sales & marketing

| Command | English alias | What it does | Just say... | Skills used | Required | Optional |
|---|---|---|---|---|---|---|
| `/営業連絡リスト` | `call-list-jp` | Top customers or leads to contact today with talking points. | "今日誰に連絡する?", "hot leads", "営業リスト作って" | `lead-triage-jp` | CRM export or spreadsheet | Gmail, calendar, Slack / Chatwork |
| `/キャンペーン準備` | `run-campaign-jp` | Sales context to campaign brief, Japanese draft copy, and owner-approved send plan. | "キャンペーン作って", "売上落ちてる", "何を告知する?" | `content-strategy-jp`, `lead-triage-jp` | content brief | CRM, sales CSV, newsletter / social tools, upstream Canva workflow |
| `/売上ブリーフ` | `sales-brief-jp` | Top / bottom sellers and a two-week promotion brief. | "何が売れてる?", "何を推す?", "sales brief" | `content-strategy-jp` | sales export | payment export, inventory notes |

### Customers & operations

| Command | English alias | What it does | Just say... | Skills used | Required | Optional |
|---|---|---|---|---|---|---|
| `/顧客の声確認` | `customer-pulse-check-jp` | Customer feedback and complaint themes with response templates. | "お客さん何て言ってる?", "レビュー見て", "complaints" | `customer-pulse-jp`, `ticket-deflector-jp` | pasted reviews / tickets / email | HubSpot, Gmail, PayPal / Stripe |
| `/クレーム返信準備` | `handle-complaint-jp` | Complaint response packet: context, draft, options, and operational fix. | "クレーム返信を書いて", "angry customer", "返金すべき?" | `ticket-deflector-jp`, `customer-pulse-jp` | pasted complaint | order / payment export |
| `/CRM整理` | `crm-cleanup-jp` | CRM hygiene packet: stale deals, duplicates, missing fields, and approved fixes. | "CRM整理して", "HubSpotが散らかってる" | `crm-maintenance-jp` | CRM export | Gmail, calendar |
| `/契約論点確認` | `review-contract-jp` | Plain-Japanese contract / estimate / purchase-order issue memo. | "この契約書見て", "NDA確認して", "発注書レビュー" | `contract-review-jp` | uploaded file | CloudSign / GMO Sign / DocuSign, email thread |

### Business intelligence

| Command | English alias | What it does | Just say... | Skills used | Required | Optional |
|---|---|---|---|---|---|---|
| `/月曜ブリーフ` | `monday-brief-jp` | Monday owner brief: cash, receivables, customer issues, professional tasks, and top decisions. | "今週何から?", "Monday brief", "今週の経営メモ" | `business-pulse-jp` | none | accounting, invoices, calendar, email, Slack / Chatwork |
| `/金曜ふりかえり` | `friday-brief-jp` | End-of-week pulse: revenue, collections, wins, watch items, and next-week reminders. | "今週どうだった?", "Friday recap" | `business-pulse-jp` | one data source | sales, CRM, calendar |
| `/四半期レビュー` | `quarterly-review-jp` | Quarterly narrative for owner, accountant, or advisor review. | "四半期レビュー", "QBR", "振り返り作って" | `business-pulse-jp` | accounting or sales export | CRM, payment export |

## All 15 skills

Skills are atomic building blocks. The table below is the complete Small Business
Japan skill surface. All 15 skills ship executable `SKILL.md` files and are
ready to use.

### Money & finance

| Skill | What it does | Just say... | Required | Optional |
|---|---|---|---|---|
| **cash-flow-snapshot-jp** | 30 / 60 / 90-day cash view with confidence notes, payment-cycle risk, and missing-data questions. | "資金繰り資料を整理して", "runway", "来月の支払予定を見たい" | accounting export, bank CSV, or payment export | invoice register, fixed cost list |
| **invoice-chase-jp** | Draft-only overdue invoice reminder packet with target, reason, evidence, risk, and approval pause. | "未入金を追いたい", "who owes me money" | invoice PDF / CSV or invoice register | email thread, payment history |
| **margin-analyzer-jp** | Unit economics and pricing scenarios with consumption-tax inclusion / exclusion made explicit. | "利益率見て", "値上げ判断材料" | sales / cost export | platform fees, shipping, subcontractor costs |
| **month-end-prep-jp** | Month-end close packet for accountant review: gaps, receipts, uncategorized items, and questions. | "月次締め", "経理資料整理" | accounting export or ledger CSV | bank CSV, invoice folder, receipt folder |
| **tax-season-organizer-jp** | Tax-season and year-end document checklist plus accountant handoff memo. | "税理士パケット作って", "年末資料" | accounting export | contractor list, invoice register, professional fee records |

### Sales & marketing

| Skill | What it does | Just say... | Required | Optional |
|---|---|---|---|---|
| **lead-triage-jp** | Rank customers / leads by urgency and fit, with Japanese follow-up drafts. | "誰に連絡する?", "営業優先順位" | CRM export or spreadsheet | Gmail, calendar |
| **content-strategy-jp** | Turn sales and customer signals into a bounded campaign brief and Japanese copy angles. | "何を告知する?", "投稿案" | sales export or brief | CRM, newsletter / social tools |
| **design-tool-handoff-jp** | Prepare a design handoff memo and asset checklist; optionally route to the upstream Small Business Canva workflow. | "Canvaに渡せる形にして" | approved content brief | Canva, Figma, Slides, designer |

### Customers & operations

| Skill | What it does | Just say... | Required | Optional |
|---|---|---|---|---|
| **customer-pulse-jp** | Synthesize reviews, tickets, disputes, and email sentiment into themes and next actions. | "顧客の声まとめて" | pasted reviews / tickets / email | HubSpot, Gmail, payment exports |
| **ticket-deflector-jp** | Draft customer replies with order / payment context and approval checklist. | "返信ドラフト", "返金案" | pasted complaint | order / payment export |
| **crm-maintenance-jp** | Identify stale records, duplicates, missing fields, and owner-approved CRM update plans. | "CRM掃除して" | CRM export | Gmail, calendar |
| **contract-review-jp** | Plain-Japanese issue memo for contracts, estimates, purchase orders, NDAs, and order forms. | "契約レビュー", "発注書確認" | uploaded file or pasted text | email thread, e-signature envelope |

### Hiring

| Skill | What it does | Just say... | Required | Optional |
|---|---|---|---|---|
| **job-post-builder-jp** | Hiring packet with job post, interview guide, scoring rubric, offer checklist, and questions for a labor professional. | "採用したい", "求人票作って" | role description | Drive folder, prior job posts |

### Business intelligence & onboarding

| Skill | What it does | Just say... | Required | Optional |
|---|---|---|---|---|
| **business-pulse-jp** | One-page owner snapshot: cash, receivables, sales, customers, week ahead, professional tasks, and top decisions. | "経営の現状見て", "weekly summary" | none; degrades gracefully | accounting, CRM, email, calendar |
| **smb-onboard-jp** | Front-door setup: tools, files, business context, pain points, first workflow, and weekly check-in suggestion. | "初期設定して", "set me up" | none | all connectors and files |

## Customizing

These workflows are starting points. They become more useful when you localize
them to your business:

- **Add business context**: industry, products, customer types, payment cycles,
  invoice practices, recurring vendors, and professional advisors.
- **Adjust thresholds**: minimum cash buffer, late-payment timing, customer
  follow-up cadence, and review thresholds.
- **Swap connectors**: use the accounting, invoice, CRM, payment, calendar, and
  file tools you already have.
- **Choose handoff formats**: email memo, checklist, spreadsheet packet, PDF
  folder, or pasted summary.
- **Keep approval gates**: sends, posts, refunds, CRM writes, contract changes,
  payroll decisions, filings, and professional communications stay under owner
  approval.

## Contributing

If you find an error, an outdated regulation, or a missing use case, contributions
are welcome. Open an issue or pull request at
https://github.com/AgentGymLeader/small-business-japan
