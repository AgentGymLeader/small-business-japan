# Connector Parity Spec

Status: draft
Updated: 2026-05-14
Owner: @agentgymleader

This document defines how Small Business Japan should move closer to Anthropic's
Claude for Small Business while preserving Japan-specific safety boundaries.

The target is not "connect everything immediately." The target is upstream
parity by capability layer: read context, draft work, stage actions, and execute
only after explicit owner approval and tool permission checks.

## Upstream Baseline

Anthropic's public Claude for Small Business pages describe a Claude Cowork
solution with a one-click plugin, connectors, skills, automations, and
ready-to-run workflows. The public examples show Claude working with:

- Intuit QuickBooks
- PayPal
- HubSpot
- Canva
- Docusign
- Google Workspace
- Microsoft 365
- Slack

Publicly described upstream behaviors include:

- pulling QuickBooks cash position.
- reconciling QuickBooks transactions against PayPal settlements.
- ranking overdue invoices and drafting reminder emails.
- writing a plain-English P&L narrative.
- preparing a close packet for an accountant.
- pulling calendar commitments into a Monday brief.
- analyzing HubSpot campaign performance and attribution.
- segmenting lists in HubSpot.
- generating campaign assets in Canva.
- staging a campaign send for owner approval.
- sending contracts through Docusign, tracking status, and filing executed
  copies.
- preserving existing source-system permissions.
- keeping the owner in the loop before anything sends, posts, or pays.

Sources checked:

- Anthropic, "Introducing Claude for Small Business", 2026-05-13:
  https://www.anthropic.com/news/claude-for-small-business
- Claude solution page, "Claude for small business", checked 2026-05-14:
  https://claude.com/solutions/small-business

## Japan Parity Principle

Small Business Japan should match the upstream shape without pretending that
Japan-specific tool writes are already safe.

Each workflow should declare the highest action level it supports:

| Level | Capability | Meaning | Default status |
|---|---|---|---|
| L0 | File / pasted context | CSV, PDF, screenshot, pasted thread, exported table | Current v0 |
| L1 | Read-only connector | Read records and metadata from a connected tool | Target |
| L2 | Draft in assistant | Produce memo, draft, checklist, confirmation packet | Current v0 |
| L3 | Stage in tool | Create draft object, queue, task, folder, campaign draft, envelope draft | Target, gated |
| L4 | Approved write | Send, post, pay, refund, sign, issue, update CRM, publish | Later, explicit approval only |
| L5 | Autonomous write | Execute without owner confirmation | Out of scope |

The product should grow from L0/L2 to L1/L3 first. L4 is allowed only when the
target tool, account permissions, audit log, approval record, and professional
boundary are clear. L5 remains out of scope.

If the target SaaS does not expose a true draft/staging API, Small Business
Japan must not fake a write. It should stage the proposed change in a sidecar
staging record with an idempotency key, source evidence, target object preview,
diff, approval state, and rollback/void notes.

## Permission Model

Connector behavior must inherit the source system's permissions.

- If the user cannot see a QuickBooks/freee/MF/Yayoi record directly, the agent
  must not see it through Small Business Japan.
- If the user cannot send, refund, publish, sign, or update inside the source
  system, the agent must not do it either.
- If the source SaaS lacks granular end-user permission inheritance, add a
  logical redaction layer before model context. This is especially important
  for payroll-like rows, My Number-adjacent data, employee records, bank data,
  customer records, and contracts.
- Every L3/L4 action must show the target tool, target object, fields to be
  changed, evidence used, missing facts, risk notes, and approval state.
- Approval must be scoped to a specific action. A general "yes" must not unlock
  unrelated actions.

MCP annotations such as `readOnlyHint`, `destructiveHint`, `idempotentHint`, and
`openWorldHint` are useful user-experience hints, but they are not enforcement.
Real enforcement must live in deterministic connector allowlists, OAuth scopes,
policy checks, sidecar staging, audit logs, and approval gates.

## Japan Tool Mapping

| Upstream job | Upstream tools | Japan candidates | First parity target |
|---|---|---|---|
| Payroll / cash planning | QuickBooks, PayPal | freee, Money Forward Cloud, Yayoi, bank CSV, Stripe, PayPal, Square, STORES, AirPAY | L1 read cash/invoice/payment records, L2 memo, L3 payment/reminder queue only |
| Month-end close | QuickBooks, PayPal, Google Drive | freee, Money Forward Cloud, Yayoi, Google Drive, OneDrive, receipt folders | L1 read ledger/bank/invoice exports, L2 close memo, L3 accountant packet folder draft |
| Invoice chasing | QuickBooks, PayPal, email | Misoca, freee invoices, MF Cloud Invoice, MakeLeaps, Stripe, PayPal, Gmail, Outlook | L1 read invoice/payment status, L2 draft reminder, L3 email draft/queue |
| Business pulse / briefs | QuickBooks, PayPal, HubSpot, Calendar, Slack | freee/MF/Yayoi, HubSpot, kintone, Google Calendar, Outlook Calendar, Slack, Chatwork, LINE WORKS | L1 read, L2 brief, L3 scheduled draft message |
| Campaign execution | QuickBooks, HubSpot, Canva | HubSpot, kintone, Salesforce, Google Sheets, Canva, Google Slides | L1 read sales/CRM, L2 campaign draft, L3 Canva/CRM/newsletter draft |
| Contract handling | Docusign | CloudSign, GMO Sign, freee Sign, DocuSign | L1 status read, L2 issue memo, L3 envelope draft only |

Initial v1 scope should stay close to the SMB daily-tool surface. BtoB Platform
Invoice is a procurement and trading-network candidate rather than a default
SMB first-wave connector, so it belongs in a later enterprise/procurement track.
Salesforce and Zoho CRM are valid later candidates, but HubSpot and kintone are
the v1 Japan SMB core.

Known tradeoffs:

- Delaying BtoB Platform Invoice may underserve procurement-heavy companies and
  users already operating inside that trading network. This is accepted for v1
  because the first release optimizes for smaller owner-operated workflows.
- Delaying Figma narrows the agency/designer-team surface. This is accepted for
  v1 because Canva and Google Slides cover the broader SMB content path.
- Keeping e-sign final execution in the target product adds last-mile friction.
  This is accepted for v1 to preserve a clearer Japan boundary around authority,
  identity, signature execution, and audit evidence.

## Domain Capability Targets

### Finance, Payments, And Invoicing

Initial connectors should prioritize read and staging, not final writes.

- L1 read: balances, transactions, invoice status, payment status, settlement
  data, due dates, customer/vendor names, invoice files, receipt folders.
- L2 draft: cash memo, month-end checklist, invoice reminder draft, accountant
  question packet, discrepancy list.
- L3 stage: reminder email draft, accountant packet folder, task list,
  non-submission export checklist.
- L4 approved write: send reminder, mark task complete, upload packet, create
  draft invoice. This requires a separate action-specific approval design.

Japan constraints:

- Do not decide tax category, input tax credit, qualified-invoice validity,
  filing readiness, or final accounting treatment.
- Do not create accounting journal imports or tax-return files in v0/v1.
- Invoice registration checks must record source, checked date, and uncertainty.
- Tax accountant handoff stays a question packet unless a qualified professional
  reviews it.

Finance connector research on 2026-05-14 produced this parity map:

| Tool | Read target | Draft / stage target | Write target | Gate |
|---|---|---|---|---|
| freee | company, transactions, invoices, journals/CSV, masters | invoice/estimate/delivery draft, transaction draft | invoice create/update, transaction create | invoice fields, tax category, account category, closed-month lock |
| Money Forward Cloud | accounting/invoice data, reports, partners | invoice/estimate draft, accounting action proposal | invoice GET/POST/PUT/DELETE, accounting API where enabled | plan/rate limit, audit log, invoice/e-record checks |
| Yayoi | linked accounts, CSV, smart transaction import data | unconfirmed transaction candidates | general accounting write API unclear; Misoca handles invoice API | treat as import/manual-review first |
| Misoca | invoice/estimate/delivery docs, partners | invoice/document draft, PDF preview | OAuth write-scope create/update | token expiry, write-scope separation, invoice/Peppol fields |
| MakeLeaps | partners, docs, history, receivables, exports | quote/invoice/mail request draft, approval flow | create/edit/export/mailing where supported | mailing/posting/payment status needs approval |
| Stripe | invoices, payments, refunds, balances, payment links | invoice draft, payment link draft, reminder/refund proposal | invoice send, payment link create, refund | never assume Stripe invoice alone satisfies Japan qualified-invoice needs |
| PayPal | settlements, transactions, invoices, disputes, refunds | invoice draft, reminder, dispute response proposal | invoice send, refund, dispute action | Japan feature differences, PII, disputes/refunds strong approval |
| Square | payments, refunds, orders, invoices, payouts | invoice draft, checkout/refund proposal | invoice publish, refund | invoice payment/status API limits, publish/refund approval |
| STORES | payment results, deposits, accounting/POS links | POS/payment request, accounting-link candidate | SDK payment flows; back-office write limited | PCI-DSS, device/app-led actions, refund scope confirmation |
| AirPAY / Airレジ | sales, payment fees, deposit schedule, accounting-link data | sales journal candidate | Airレジ API is mostly data integration; AirPAY write limited | daily close, fee differences, settlement matching |
| Bank CSV | statements, balances, transfer result CSV | journal candidate, reconciliation candidate, Zengin transfer-file draft | none by default | duplicate transfer prevention, kana name checks, bank/API regulation |

Later finance/procurement candidates:

- BtoB Platform Invoice: useful for invoice receiving/issuing networks and
  procurement-heavy companies, but not first-wave SMB scope. Revisit after the
  core freee/Money Forward/Yayoi/Misoca/MakeLeaps/Stripe/PayPal/Square paths are
  stable.

Research sources:

- freee accounting API: https://developer.freee.co.jp/reference/accounting
- freee invoice API: https://developer.freee.co.jp/reference/iv
- Money Forward invoice API: https://biz.moneyforward.com/support/invoice/guide/api-guide/a03.html
- Money Forward accounting API: https://biz.moneyforward.com/support/account/guide/others/ot09.html
- Misoca API: https://doc.misoca.jp/
- MakeLeaps API: https://www.makeleaps.com/features/api/
- BtoB Platform API: https://www.infomart.co.jp/reference/api/index.html
- Stripe Invoicing: https://stripe.com/invoicing
- Stripe Payment Links: https://stripe.com/en-jp/payments/payment-links
- PayPal Invoicing API: https://developer.paypal.com/docs/invoicing/
- Square Invoices API: https://developer.squareup.com/reference/square/invoices-api
- STORES payments SDK/API: https://stores.fun/development/payments-sdk-api
- Airレジ API連携: https://faq.airregi.jp/hc/ja/articles/48202752451353
- NTA invoice system: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6498.htm
- NTA invoice Web API: https://www.invoice-kohyo.nta.go.jp/web-api/index.html
- Digital Agency JP PINT: https://www.digital.go.jp/policies/electronic_invoice
- FSA electronic payment service providers: https://www.fsa.go.jp/common/law/guide/chusho/04.html

### CRM, Marketing, And Collaboration

- L1 read: lead/customer records, campaign history, attribution, activity logs,
  calendar commitments, message threads, support tickets.
- L2 draft: lead priority memo, follow-up draft, customer pulse memo, campaign
  plan, weekly brief.
- L3 stage: CRM task draft, email draft, Slack/Chatwork scheduled draft,
  campaign audience draft, content calendar draft.
- L4 approved write: update CRM fields, send email, post message, launch
  campaign. This requires explicit owner approval and unsubscribe/consent
  checks.

Japan constraints:

- APPI use purpose, acquisition source, third-party provision, opt-out, and
  sensitive-data checks must appear before CRM or campaign writes.
- Marketing claims need evidence notes. No.1, cheapest, guaranteed improvement,
  and testimonial claims require substantiation.
- Customer replies must not finalize refund, liability, complaint resolution, or
  consumer-law treatment.

CRM/collaboration connector research on 2026-05-14 produced this parity map:

| Tool | Read target | Draft / stage target | Write target | Gate |
|---|---|---|---|---|
| HubSpot | contacts, companies, deals, tickets, campaigns | lead triage, note/task/email/campaign draft, send stage | CRM object create/update, marketing email create/update | OAuth scopes, HubSpot user permission, bulk/campaign send approval |
| kintone | apps, records, comments, files, status | record update proposal, comment draft, process transition proposal | record add/update/delete, comment, status update | app/record/field permissions, table-field delete risk, guest space constraints |
| Salesforce | schema, SOQL/SOSL, records | task/opportunity update draft, case reply draft | create/update/delete where scoped | FLS/object/sharing rules, delete separate gate, all-server too broad |
| Zoho CRM | modules, search, COQL | leads/deals/tasks/campaign draft | module CREATE/UPDATE/DELETE scopes | avoid ALL scope, batch risk, Blueprint/approval consistency |
| Google Workspace | Gmail, Drive, Calendar, Sheets | Gmail draft, Sheet change preview, calendar proposal, Drive file draft | Sheets update, Drive create/share, Calendar write; Gmail send off by default | Workspace admin trust, file/calendar ACL, share/send approval |
| Microsoft 365 | Outlook, OneDrive, SharePoint, Teams, Excel | Outlook draft, Excel edit preview | send/post/file write only by separate scope; M365 connector often read-only | Entra consent, DLP/Conditional Access, avoid broad application permissions |
| Slack | channel/DM/file search, recent thread context | private response draft | post to thread after user click | admin approval, channel membership, workspace/retention/rate-limit checks |
| Chatwork | rooms, messages, tasks | message/task draft | room message post/edit/delete, read/unread, task operations | external-room risk, task owner checks, scope split |
| LINE WORKS | bot/room/user context where available | message draft/stage | bot message send as first write target | bot invitation/target approval, broadcast risk, APPI use-purpose check |

MVP gate:

- `read/search` and `draft/stage` are standard.
- `send`, `post`, `share`, `delete`, `bulk update`, and campaign launch require
  approval every time.
- CRM `delete` and `bulk campaign send` should be separate tools, not generic
  CRM writes.
- Japan-specific gates add 稟議/複数承認, 敬語/宛先確認, APPI利用目的, and
  cross-SaaS citation checks.
- v1 CRM scope should prioritize HubSpot and kintone. Salesforce is useful but
  enterprise-heavy; Zoho CRM can remain a later compatibility candidate.

Research sources:

- Claude connectors: https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
- Google Workspace connector: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors
- Microsoft 365 connector: https://support.claude.com/en/articles/12542951-enable-and-use-the-microsoft-365-connector
- Microsoft 365 connector security: https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide
- Claude for Slack: https://claude.com/claude-for-slack
- Using Claude in Slack: https://support.claude.com/en/articles/12461605-using-claude-in-slack
- HubSpot CRM object APIs: https://developers.hubspot.com/docs/api-reference/latest/crm/using-object-apis
- kintone records API: https://kintone.dev/en/docs/kintone/rest-api/records/
- Salesforce hosted MCP SObject server: https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/sobject-all.html
- Zoho CRM scopes: https://www.zoho.com/crm/developer/docs/api/v8/scopes.html
- Gmail API: https://developers.google.com/workspace/gmail/api/reference/rest
- Google Drive API: https://developers.google.com/workspace/drive/api/reference/rest/v3
- Google Sheets scopes: https://developers.google.com/sheets/api/scopes
- Microsoft Graph permissions: https://learn.microsoft.com/en-us/graph/permissions-reference
- Slack `chat.postMessage`: https://docs.slack.dev/reference/methods/chat.postMessage/
- Slack `conversations.history`: https://docs.slack.dev/reference/methods/conversations.history/
- Chatwork message API: https://developer.chatwork.com/reference/post-rooms-room_id-messages
- LINE WORKS API 2.0: https://line-works.com/pr/20220404/

### Design And Content

- L1 read: brand kit, approved copy, campaign context, existing assets,
  template references.
- L2 draft: design handoff memo, asset checklist, copy variants, rights review
  checklist.
- L3 stage: Canva design draft or Slides draft, with rights/license flags.
- L4 approved write: publish, export, schedule, or distribute asset only after
  owner approval and platform/tool license confirmation.

Japan constraints:

- Do not claim copyright, trademark, likeness, font, template, or platform
  advertising clearance.
- Canva should remain the primary design connector. A Japan-only Canva clone is
  not needed.
- Google Slides can ride the Google Workspace path as a presentation/handoff
  target.
- Figma is not v1 SMB connector scope. Keep it as an agency/designer-team
  reference or handoff target only; do not treat it as Canva-equivalent
  generation/write infrastructure unless an explicit plugin/API path and user
  segment justify it later.
- Canva outputs must preserve asset/license review. Pro assets, templates,
  AI-generated assets, brand kit use, export, publish, and template resale must
  remain approval-gated.

### Contracts And E-Signature

- L1 read: uploaded document, template baseline, signature envelope status,
  counterparty metadata, approval history.
- L2 draft: Hold / Escalate / CEO confirmation memo, missing facts, counsel
  questions.
- L3 stage: envelope draft, text-transfer packet, signature request draft, and
  folder filing draft. L3 must remain visibly unsent and unsigned.
- L4 approved write: send envelope or file executed copy only with authority,
  identity, and approval checks. For v1, final signature execution stays with
  the user in the target e-sign product.

Japan constraints:

- Do not decide legal validity, enforceability, settlement position, or "safe to
  sign" status.
- E-signature workflows must separate document issue spotting from authority,
  identity verification, audit log, and retention questions.
- Contract-specific legal judgment should escalate to counsel.
- Use a common e-sign abstraction for CloudSign, GMO Sign, freee Sign, and
  DocuSign: `read -> draft -> stage -> human approve -> send -> status ->
  executed-copy filing`.
- In Japan v1, "stage" means text transfer and envelope preparation, not signing
  on behalf of the user and not silently sending a signature request.
- If the user edits the staged envelope inside the e-sign product before final
  execution, the connector must re-read or compare the envelope before filing
  status, audit evidence, or executed copies.
- Split approval for `send signature request` and `accept/file executed copy`.
  They are different risk moments.
- If bulk sending is supported, approval must be per-recipient or per-batch with
  a visible recipient list and diff. Hidden bulk sends are out of scope.
- Preserve audit certificate, completion certificate, envelope history, and
  retention metadata where the target tool exposes them.

## Adapter Model

The core should stay provider-neutral.

| Layer | Contents |
|---|---|
| `core` | output contracts, research dossiers, red-team prompts, workflow specs |
| `adapters/claude` | Claude plugin manifest, Cowork/Claude Code install prompts |
| `adapters/codex` | Codex skill/plugin wrapper, local repo and PR workflow checks |
| `adapters/gemini` | Gemini CLI/API prompt wrapper and workspace integration notes |

The current repository is Claude-facing, but future connector parity should not
make the core depend on Claude-only primitives.

## Release Gates For Connector Parity

Before any L1+ connector support lands:

- Source-system permission inheritance documented.
- Read/write scopes listed per connector.
- Sample approval transcript included.
- Action audit record shape defined.
- Data minimization and secret redaction documented.
- Japan legal/professional boundary dossier refreshed within 180 days.
- Semantic audit test set covers Japanese invoices, expenses, payroll-like rows,
  contracts, customer records, tax-rate handling, date handling, vendor/customer
  separation, and PII redaction.
- Negative tests cover "send now", "file this", "submit this", "mark compliant",
  "finalize tax/legal/labor judgment", and "import this CSV".

Before any L3/L4 support lands:

- Tool-specific sandbox or dry-run mode exists.
- Staged object is visibly different from sent/published/executed object.
- Owner approval is action-specific.
- Professional handoff path is available where tax, legal, labor, accounting,
  HR, or administrative-scrivener boundaries are implicated.
- Rollback/cancel instructions are documented for the target tool.
- For Japan tax, payroll, labor, privacy, invoice, and contract workflows, stale
  or missing official source freshness blocks approved writes. Analysis and
  drafts may continue, but L4 is closed until sources are refreshed.

## Provider-Neutral Connector Contract

Every adapter should implement the same policy envelope:

```text
ConnectorAdapter:
  capabilities
  auth_context
  read
  draft
  stage
  approve_write
  audit_event
  redact
```

Claude, Codex, and Gemini adapters may differ in prompting and runtime, but
provider-specific extensions cannot weaken the connector policy. The invariant
is:

```text
LLMs propose.
Connectors read or stage.
Humans approve.
Deterministic policy executes.
```

## Open Research Items

SubAgent connector research should fill these before implementation:

- Official API and marketplace terms for freee, Money Forward Cloud, Yayoi,
  Misoca, MakeLeaps, CloudSign, GMO Sign, freee Sign, kintone, Chatwork, and
  LINE WORKS.
- Whether each tool supports draft/staged objects separately from final writes.
- Whether each tool exposes audit logs and approval workflows through API.
- Whether connector access can inherit end-user permissions or only service
  account permissions.
- Whether each connector can run in dry-run mode for demo and review.

## Current Design / E-Sign Research Notes

SubAgent research on 2026-05-14 found:

- Upstream parity is high for Canva and DocuSign because Anthropic publicly
  describes Canva asset generation and Docusign contract send/status/filing
  flows.
- Canva should be the first design write/stage target. Google Slides can be a
  Workspace handoff/stage target. Figma stays outside v1 and should be treated
  as a later agency/designer-team reference path.
- CloudSign, GMO Sign, freee Sign, and DocuSign all map cleanly to the e-sign
  abstraction, but plans/API availability and workflow states differ by vendor.
- freee Sign exposes statuses such as draft/confirmation flows; approval gates
  should key off those statuses rather than assuming every document is ready to
  send.
- Electronic contract flows need separate checks for paper-required exceptions,
  electronic record retention metadata, identity/authority, and audit trail.

Research sources:

- Canva MCP docs: https://www.canva.dev/docs/mcp/
- Canva Claude connector: https://www.canva.com/newsroom/news/claude-ai-connector/
- Canva AI terms: https://www.canva.com/policies/ai-product-terms-2023-10-04/
- Canva content license: https://www.canva.com/policies/content-license-agreement/
- Figma API scopes: https://developers.figma.com/docs/rest-api/scopes/
- Google Slides `batchUpdate`: https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/batchUpdate
- Google Drive permissions: https://developers.google.com/workspace/drive/api/guides/manage-sharing
- CloudSign Web API: https://help.cloudsign.jp/en/articles/936884
- CloudSign legal guide: https://www.cloudsign.jp/about/legal/
- GMO Sign API/Webhook: https://helpcenter.gmosign.com/hc/ja/articles/900005934763
- freee Sign API/Webhook: https://support.freee.co.jp/hc/ja/articles/7509424637721
- freee Sign statuses: https://support.freee.co.jp/hc/ja/articles/6699858719513
- DocuSign Japan legality: https://www.docusign.com/products/electronic-signature/legality/japan
- Digital Agency e-signature: https://www.digital.go.jp/en/policies/digitalsign
