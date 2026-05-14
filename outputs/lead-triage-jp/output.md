# Output Contract: lead-triage-jp

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

Rank lead or customer follow-up candidates from a CRM export, spreadsheet, or
pasted list, then draft talking points for owner approval. The output supports
sales prioritization only; it does not decide legal permission to contact or
send messages.

## Inputs

- CRM export, lead spreadsheet, customer list, inquiry list, pasted emails, or
  calendar context.
- Optional: consent notes, acquisition source, unsubscribe records, campaign
  context, sales owner notes.

## Required output sections

1. `Summary`
2. `Lead priority candidates`
3. `Evidence used`
4. `Contact-permission review points`
5. `Draft talking points`
6. `Missing data`
7. `Approval boundary`

## Japan compliance checks

- Flag unclear use purpose, acquisition source, opt-out or consent evidence,
  third-party provision status, sensitive data, and unsubscribe status.
- Do not infer sensitive attributes.
- Treat email sendability as a review point, not a conclusion.

## Negative scope

Do not claim APPI compliance, consent obtained, third-party provision allowed,
marketing email allowed, or public email addresses freely usable. Do not send,
enrich, sell, externally match, or upload lead lists.

## Approval pause

Stop before any email, DM, call-list export, CRM write, external enrichment, or
campaign upload.

## Output format

Markdown memo only. Use lead-score candidates with reasons and missing evidence.

## Refresh trigger

Refresh when APPI, opt-out, or commercial-email guidance changes, or when the
workflow starts writing to CRM or email tools.
