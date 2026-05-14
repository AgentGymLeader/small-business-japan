# Output Contract: month-end-prep-jp

Status: proposed contract
Owner action boundary: read-only / memo-only

## Mandatory output header

Every generated output must begin with:

```text
Small Business Japan by @agentgymleader. Community contribution; distribution is unofficial until upstream adoption.
Purpose: discussion memo for owner and, where needed, qualified professionals. Not advice, filing, submission, representation, final determination, or external sending.
Research checked: 2026-05-14. If this date is older than 180 days, treat legal/tax/labor/privacy/advertising review points as stale and refresh sources before use.
```

## Purpose

Prepare a month-end review packet for a Japanese small business: source list,
missing documents, uncategorized items, invoice and receipt candidates, and
questions for the owner or accountant. It does not close books or approve
journal entries.

## Inputs

- Accounting export, ledger CSV, bank CSV, invoice folder, receipt folder,
  electronic-transaction files, or pasted month-end list.
- Optional: inventory memo, contract folder, payroll summary, accountant's
  requested format.

## Required output sections

1. `Summary`
2. `Documents found`
3. `Missing or unclear records`
4. `Uncategorized review list`
5. `Invoice / receipt preservation checks`
6. `Questions for accountant`
7. `Approval boundary`

## Japan compliance checks

- Treat bookkeeping and preservation requirements as checklist items only.
- Mark electronic-record, invoice-system, and account-classification status as
  unconfirmed.
- Keep source period, filename, and checked date visible.
- Separate record collection from accounting close or tax filing.

## Negative scope

Do not approve journal entries, decide account categories, finalize financial
statements, guarantee electronic-record preservation compliance, prepare filing
data, or claim accountant review.

## Approval pause

Stop before writing to accounting tools, renaming or deleting source files,
submitting data, or sending packets to an accountant.

## Output format

Markdown checklist and memo only. Do not create accounting import CSV, journal
data, or filing files.

## Refresh trigger

Refresh when NTA bookkeeping, preservation, invoice-system, or
electronic-record guidance changes.
