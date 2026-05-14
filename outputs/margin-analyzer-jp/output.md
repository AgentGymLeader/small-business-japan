# Output Contract: margin-analyzer-jp

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

Prepare margin and pricing scenarios from sales, cost, fee, shipping, labor, or
inventory exports. The output separates observed numbers, assumptions, and
owner decisions. It does not decide legal price adequacy, tax treatment, or
accounting profit.

## Inputs

- Sales export, cost export, product list, platform fee table, shipping cost
  table, subcontractor cost memo, or pasted pricing table.
- Optional: competitor notes, supplier increase notice, labor-cost memo,
  campaign plan.

## Required output sections

1. `Summary`
2. `Source coverage`
3. `Margin candidates`
4. `Scenario assumptions`
5. `Price-change talking points`
6. `Legal / tax / accounting review points`
7. `Approval boundary`

## Japan compliance checks

- Keep consumption-tax inclusion/exclusion explicit.
- Label accounting profit and tax income as unconfirmed.
- Treat labor-cost, raw-material, and energy-cost pass-through as negotiation
  context, not a legal conclusion.
- Separate pricing recommendation drafts from final owner decision.

## Negative scope

Do not claim a price is legally appropriate, competition-law compliant,
tax/accounting-final, guaranteed profitable, or accepted by a counterparty. Do
not create invoices, quotes, purchase orders, or system import data.

## Approval pause

Stop before sending price notices, changing live product prices, issuing quotes,
or writing to ecommerce, accounting, or CRM tools.

## Output format

Markdown memo only. Use tables for scenarios, and mark every scenario as
assumption-based.

## Refresh trigger

Refresh when pricing, competition, subcontracting, tax, or accounting guidance
materially changes.
