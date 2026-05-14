# Output Contract: cash-flow-snapshot-jp

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

Prepare a Japanese small-business cash snapshot from bank, accounting, payment,
or invoice exports. The output shows source-based cash movement, receivables,
payables, near-term risks, missing records, and questions for the owner or
accountant. It does not decide tax, accounting, filing, financing, or payment
actions.

## Inputs

- Bank CSV, accounting export, payment export, invoice register, or pasted cash
  table.
- Optional: fixed-cost list, payroll date, tax payment memo, payment processor
  export, invoice PDFs, owner notes.

## Required output sections

1. `Summary`
2. `Source coverage`
3. `Cash movement candidates`
4. `Receivables / payables watch list`
5. `Missing or stale records`
6. `Risk notes`
7. `Questions for accountant / owner`
8. `Approval boundary`

## Japan compliance checks

- Mark tax categories, deductible expense treatment, consumption-tax treatment,
  and input-tax-credit status as unconfirmed.
- Treat invoice-system registration and qualified-invoice evidence as review
  candidates only.
- Separate observed cash movement from accounting or tax conclusions.
- Preserve source filename, period, and checked date when available.

## Negative scope

Do not calculate tax payable, decide expense deductibility, decide input tax
credit, classify accounting treatment as final, create journal entries, submit
or file documents, initiate bank transfers, or tell the owner a payment plan is
legally or financially sufficient.

## Approval pause

Stop before any payment, refund, collection action, accounting write, or message
to a customer, vendor, bank, tax office, or professional advisor.

## Output format

Markdown memo only. If the owner asks for a tool-specific CSV, produce a
field-mapping memo and say the import must be completed in the target tool after
owner and professional review.

## Refresh trigger

Refresh the research dossier when NTA invoice, bookkeeping, electronic-record,
or tax-accountant boundary guidance changes, or when this output starts writing
to accounting, banking, or invoice tools.
