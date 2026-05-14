# Output Contract: crm-maintenance-jp

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

Prepare a CRM hygiene memo: duplicate candidates, stale records, missing fields,
data-quality tasks, and owner-approved update suggestions. It does not write to
CRM systems or complete APPI rights requests.

## Inputs

- CRM export, spreadsheet, customer list, pipeline export, email/calendar
  context, or pasted records.
- Optional: field dictionary, use-purpose notice, update owner, retention rule,
  deletion/correction request log.

## Required output sections

1. `Summary`
2. `Duplicate candidates`
3. `Stale or missing-field candidates`
4. `Personal-data review points`
5. `Recommended owner tasks`
6. `Approval boundary`

## Japan compliance checks

- Mark correction, deletion, disclosure, third-party provision stop, and use
  purpose issues as owner/legal review candidates.
- Do not infer sensitive attributes.
- Minimize personal data in examples.

## Negative scope

Do not say correction, deletion, disclosure, third-party provision stop, consent,
or APPI compliance is completed. Do not delete, merge, update, enrich, export,
or upload records.

## Approval pause

Stop before CRM writes, deduplication, deletion, enrichment, external sharing,
email list export, or rights-request handling.

## Output format

Markdown memo only. Use record identifiers and field names, not full personal
data, when possible.

## Refresh trigger

Refresh when APPI, CRM platform, retention, or data-rights guidance changes.
