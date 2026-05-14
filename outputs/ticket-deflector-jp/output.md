# Output Contract: ticket-deflector-jp

Status: proposed contract
Owner action boundary: read-only / draft-only / memo-only

## Mandatory output header

Every generated output must begin with:

```text
Small Business Japan by @agentgymleader. Community contribution; distribution is unofficial until upstream adoption.
Purpose: discussion memo for owner and, where needed, qualified professionals. Not advice, filing, submission, representation, final determination, or external sending.
目的: オーナーおよび必要に応じて担当士業と確認するための整理メモです。助言・申請・代行・最終判断・外部送信は行いません。
Research checked: 2026-05-14. If this date is older than 180 days, treat legal/tax/labor/privacy/advertising review points as stale and refresh sources before use.
```

## Purpose

Prepare a customer-support or complaint response packet with context, draft
wording, missing facts, refund/order review points, and approval pause. It does
not send replies or decide consumer-law, refund, or chargeback outcomes.

## Inputs

- Complaint text, support ticket, email thread, order record, payment export,
  refund policy, shipping note, or pasted customer context.
- Optional: prior response template, product notes, manager policy.

## Required output sections

1. `Summary`
2. `Customer issue`
3. `Facts found / missing`
4. `Policy and rights review points`
5. `Draft reply`
6. `Risks before sending`
7. `Approval boundary`

## Japan compliance checks

- Separate empathy and factual confirmation from refund or liability decisions.
- Check whether terms, cancellation, return, final confirmation, and payment
  timing need human review.
- Treat chargeback and consumer-rights points as escalation candidates.

## Negative scope

Do not say refund is impossible, chargeback is illegal, cooling-off always
applies or never applies, representation is definitely accurate, or the reply
resolves the matter. Do not send, refund, cancel, or update orders.

## Approval pause

Stop before sending replies, issuing refunds, cancelling orders, escalating to
platforms, or changing customer records.

## Output format

Markdown memo, owner-review draft reply, and approval checklist only. Draft
replies must be clearly marked `承認前ドラフト`.

## Refresh trigger

Refresh when consumer, ecommerce, payment-dispute, or platform policy guidance
changes.
