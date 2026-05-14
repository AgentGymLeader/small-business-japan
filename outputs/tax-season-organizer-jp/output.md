# Output Contract: tax-season-organizer-jp

Status: proposed contract
Owner action boundary: read-only / memo-only / professional-handoff only

## Mandatory output header

Every generated output must begin with:

```text
Small Business Japan by @agentgymleader. Community contribution; distribution is unofficial until upstream adoption.
Purpose: discussion memo for owner and, where needed, qualified professionals. Not advice, filing, submission, representation, final determination, or external sending.
Research checked: 2026-05-14. If this date is older than 180 days, treat legal/tax/labor/privacy/advertising review points as stale and refresh sources before use.
```

## Purpose

Prepare a tax-season document organizer and accountant handoff memo for a
Japanese small business. The output collects source candidates, missing items,
and questions; it does not create tax returns or answer tax consultation
questions.

## Inputs

- Accounting export, invoice register, bank CSV, receipt folder, contractor
  list, professional-fee records, fixed-asset memo, or owner notes.
- Optional: prior-year accountant request list, tax-office notices, invoice
  registration notes.

## Required output sections

1. `Summary`
2. `Documents to gather`
3. `Missing or unclear items`
4. `Tax-accountant question packet`
5. `Invoice / consumption-tax review points`
6. `Owner decisions still required`
7. `Approval boundary`

## Japan compliance checks

- Treat tax positions, deductions, credits, exemptions, special treatments, and
  registration decisions as questions for the owner or tax accountant.
- Do not calculate filing amounts, tax payable, or return fields.
- Include source and checked date for official references when cited.

## Negative scope

Do not prepare tax returns, calculate final tax, decide deduction or credit
eligibility, decide invoice registration, argue with a tax office, file,
submit, or imply tax-accountant review.

## Approval pause

Stop before sending material to a tax accountant or authority, uploading to tax
software, or making a tax-position decision.

## Output format

Markdown checklist and confirmation packet only. Do not create tax software
imports, return files, or submission-ready documents.

## Refresh trigger

Refresh when NTA tax-agent, invoice-system, bookkeeping, electronic-record, or
filing guidance changes.
