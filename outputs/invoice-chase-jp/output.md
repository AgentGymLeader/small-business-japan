# Output Contract: invoice-chase-jp

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

Help a Japanese small-business owner review unpaid invoices and prepare a
draft-only reminder packet. The output identifies target, reason, evidence,
risk, and approval status. It does not send messages, issue invoices, write to
accounting tools, or decide tax/accounting treatment.

## Inputs

At least one of:

- invoice PDF.
- invoice register CSV / XLSX.
- pasted invoice table.
- payment history CSV.
- bank CSV.
- customer email thread.

Optional:

- invoice tool name.
- accounting tool name.
- payment channel.
- customer relationship notes.
- owner's preferred reminder tone.
- accountant / bookkeeper context.

## Extracted field candidates

When visible in the source, extract as candidates only:

- document type: invoice, delivery note, receipt, or other.
- issuer name.
- invoice number or management number.
- invoice date.
- transaction date or covered period.
- due date.
- counterparty / buyer name.
- invoice amount.
- amount paid.
- unpaid amount.
- payment method / bank account text.
- consumption-tax inclusion / exclusion wording.
- tax-rate sections, if present.
- qualified invoice registration number candidate: `T` plus 13 digits.
- line-item or service description.
- reduced-tax-rate marker, if present.

## Required output sections

1. `Summary`
2. `対象`
3. `根拠`
4. `不足情報`
5. `インボイス制度まわりの確認候補`
6. `督促ドラフト`
7. `送る前のrisk`
8. `承認待ち`
9. `専門家に確認する質問`

## Japan compliance checks

Flag only as review candidates:

- missing or unreadable issuer name.
- missing or unreadable buyer name, with a note that simplified invoice
  treatment depends on facts outside the output.
- no registration number, with a note that transitional measures may apply and
  the item should not be treated as a defect by default.
- malformed qualified invoice registration number candidate.
- registration-number verification not performed or not timestamped.
- transaction date / covered period missing or unclear.
- service or goods description missing or unclear.
- tax-rate breakdown missing where the source appears to show consumption tax.
- reduced-tax-rate marker missing where the source appears to mix rates.
- arithmetic mismatch candidate across subtotal, tax, total, paid, and unpaid
  fields.
- rounding difference candidate, without deciding tax correctness.

## Negative scope

The output must not:

- say the invoice is a valid qualified invoice.
- say input tax credit can be claimed.
- say tax treatment is correct.
- say an accountant, tax accountant, lawyer, or other professional checked it.
- create tool-specific import CSV or accounting journal data.
- issue a replacement invoice.
- send a reminder.
- demand that an exempt business register for the invoice system.
- pressure an exempt business into a price cut or unilateral condition change.
- treat an exempt-business or no-registration-number case as a defect without
  noting that transitional measures may apply.
- claim a file is ready for filing, submission, or preservation compliance.

## Reminder draft boundary

Reminder drafts must be calm, factual, and owner-approved. They should include:

- invoice identifier.
- amount and due date as source-based candidates.
- payment status as a candidate.
- request to confirm if already paid.
- no legal threat unless the owner supplies approved wording.
- no statement that the counterparty violated tax law.

## Approval pause

Stop before sending reminders, issuing or revising invoices, writing to invoice
or accounting tools, creating tool-specific import files, contacting customers,
or asserting a tax/accounting conclusion.

## Output format

v0 is memo-only. Use Markdown, not CSV. If the owner asks for a tool-specific
CSV or import file, produce a field-mapping memo and say that export/import
should be done inside the target tool after owner and professional review.

## Refresh trigger

Refresh the research dossier when NTA invoice-system, input-tax-credit,
bookkeeping, electronic-record, or tax-accountant boundary guidance changes, or
when this output starts writing to invoice/accounting/email tools.
