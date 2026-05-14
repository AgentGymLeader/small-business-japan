# Output Contract: contract-review-jp

Status: proposed contract
Owner action boundary: read-only / memo-only / escalate-on-judgment

## Mandatory output header

Every generated output must begin with:

```text
Small Business Japan by @agentgymleader. Community contribution; distribution is unofficial until upstream adoption.
Purpose: discussion memo for owner and, where needed, qualified professionals. Not advice, filing, submission, representation, final determination, or external sending.
Research checked: 2026-05-14. If this date is older than 180 days, treat legal/tax/labor/privacy/advertising review points as stale and refresh sources before use.
```

## Purpose

Prepare a plain-Japanese issue memo for contracts, estimates, purchase orders,
NDA drafts, or electronic-signature envelopes. The output maps clauses,
missing facts, hold/escalate/CEO-confirmation items, and questions for counsel
or authorized approvers. It does not provide legal conclusions.

## Inputs

- Uploaded contract, pasted clause text, estimate, purchase order, NDA, order
  terms, email thread, or electronic-signature context.
- Optional: template baseline, negotiation notes, approval authority notes,
  counsel instructions.

## Required output sections

1. `Summary`
2. `Document type and parties`
3. `Hold`
4. `Escalate`
5. `CEO確認事項`
6. `Missing facts`
7. `Questions for counsel / approver`
8. `Approval boundary`

## Japan compliance checks

- Convert legal uncertainty into `Hold`, `Escalate`, or `CEO確認事項`.
- Treat template diffs and general clause notes as memo-only.
- Separate electronic-signature handoff facts from validity or authority
  conclusions.

## Negative scope

Do not say a contract is valid, invalid, enforceable, unenforceable, no legal
risk, must be amended this way, settlement-ready, or safe to sign/send. Do not
negotiate, send, sign, submit, or execute electronic-contract flows.

## Approval pause

Stop before external sending, negotiation, signing, envelope creation,
CloudSign/GMO Sign/DocuSign action, or final legal judgment.

## Output format

Markdown issue memo only. Use `Hold`, `Escalate`, and `CEO確認事項` as the core
triage labels.

## Refresh trigger

Refresh when MOJ AI/legal-service guidance, e-signature guidance, or electronic
contract platform rules materially change.
