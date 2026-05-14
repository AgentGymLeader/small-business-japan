# Output Contract: smb-onboard-jp

Status: starter contract
Owner action boundary: read-only / draft-only / memo-only

## Mandatory output header

Every generated output must begin with:

```text
Small Business Japan by @agentgymleader. Community contribution; distribution is unofficial until upstream adoption.
Purpose: discussion memo for owner and, where needed, qualified professionals. Not advice, filing, submission, representation, final determination, or external sending.
Research checked: 2026-05-14. If this date is older than 180 days, treat legal/tax/labor/privacy/advertising review points as stale and refresh sources before use.
```

## Purpose

Help a Japanese small-business owner get the first useful result from one file,
export, pasted message, or live connector, then produce a reusable business
context draft and first-workflow recommendation.

## Inputs

At least one of:

- business description.
- current pain.
- CSV / XLSX / pasted table.
- invoice PDF / register.
- email thread.
- contract file.
- CRM / spreadsheet.
- screenshot.

Optional:

- accounting tool name.
- invoice tool name.
- payment channel.
- CRM / customer-list tool.
- professional advisor context.
- preferred handoff format.

## Required output sections

1. `Business context draft`
2. `Available data`
3. `First safe workflow`
4. `What I can do now`
5. `What a connector would unlock later`
6. `Japan compliance checks`
7. `Output format`
8. `Approval boundary`
9. `Next owner action`

## Japan compliance checks

- Identify whether inputs may contain personal data, customer data, employee or
  applicant data, contract terms, tax/accounting records, or filing-related
  information.
- Keep tax, legal, labor, accounting, HR, and administrative-scrivener issues as
  review questions.
- Explain that connectors are optional and owner-provided exports/pasted text
  are enough for the first safe workflow.

## Output format

Markdown onboarding memo only. The first output should include a business
context draft, available-data map, first-workflow recommendation, missing-data
section, approval boundary, and professional question packet.

## Negative scope

The output must not:

- claim legal, tax, labor, accounting, HR, or administrative-scrivener advice.
- represent the owner.
- submit filings.
- make final determinations.
- display or imply professional credentials.
- send, post, pay, refund, update CRM, edit accounting, or contact anyone.
- say a packet is complete, ready to file, or professionally checked.
- create tool-specific import CSV, invoice issuing data, accounting journal
  data, CRM update files, or send-ready email files in v0.

## Approval pause

If a next action touches money, customers, professional advisors, filings,
contracts, employee terms, customer refunds, CRM writes, or external messages,
the output must stop and ask for owner approval.

## Success criteria

- The owner knows the next safe step.
- The owner can start with one source.
- Missing data is named plainly.
- Professional handoff questions are separated from AI-generated drafts.
- No live connector is required for the first useful result.
- The output is a memo, draft, checklist, or professional confirmation packet,
  with extracted-field candidates only as sections inside those containers, not
  as an import file.

## Refresh trigger

Refresh the research dossier when upstream Small Business onboarding structure
changes, Japan-specific professional-boundary guidance changes, or onboarding
starts writing to tools.
