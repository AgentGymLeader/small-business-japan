# Output Contract: customer-pulse-jp

Status: proposed contract
Owner action boundary: read-only / memo-only

## Mandatory output header

Every generated output must begin with:

```text
Small Business Japan by @agentgymleader. Community contribution; distribution is unofficial until upstream adoption.
Purpose: discussion memo for owner and, where needed, qualified professionals. Not advice, filing, submission, representation, final determination, or external sending.
目的: オーナーおよび必要に応じて担当士業と確認するための整理メモです。助言・申請・代行・最終判断・外部送信は行いません。
Research checked: 2026-05-14. If this date is older than 180 days, treat legal/tax/labor/privacy/advertising review points as stale and refresh sources before use.
```

## Purpose

Summarize customer feedback, reviews, tickets, disputes, or email themes for a
Japanese small business. The output identifies themes, sentiment candidates,
operational issues, and follow-up questions; it does not reply to customers or
decide legal liability.

## Inputs

- Pasted reviews, tickets, email threads, survey rows, dispute notes, CRM export,
  or customer-support spreadsheet.
- Optional: order/payment export, refund policy, product notes, prior response
  templates.

## Required output sections

1. `Summary`
2. `Themes`
3. `Representative evidence`
4. `Operational follow-up candidates`
5. `Privacy / complaint review points`
6. `Escalation candidates`
7. `Approval boundary`

## Japan compliance checks

- Minimize personal data in summaries.
- Mark complaint, refund, correction, deletion, and disclosure requests as
  review candidates.
- Keep APPI use-purpose and third-party sharing questions visible where
  customer data is reused.

## Negative scope

Do not claim APPI compliance, consent, complaint resolution, liability status,
refund obligation, correction/deletion completion, or third-party provision
permission. Do not send replies or update records.

## Approval pause

Stop before replying to customers, issuing refunds, changing orders, updating
CRM/support systems, or sharing customer data externally.

## Output format

Markdown memo only. Use aggregate themes by default and include individual
examples only when necessary and minimized.

## Refresh trigger

Refresh when APPI, consumer-protection, complaint-handling, or platform dispute
guidance changes.
