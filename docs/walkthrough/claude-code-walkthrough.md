# Claude Code Walkthrough Test

Status: local dry-run walkthrough plus Claude Code manifest validation
Target: repository root

## Purpose

Verify that Claude Code can read the local plugin tree, discover the Starter
Pack skills, and run the onboarding workflow without live connectors or external
writes.

## Setup

From repo root:

```bash
node bin/small-business-japan.js doctor
claude plugin validate .
python scripts/validate_small_business_japan.py
```

The verified local commands on 2026-05-14 were:

```text
node bin/small-business-japan.js doctor
claude plugin validate .
```

It passed against Claude Code 2.1.133. Then install the plugin using the local
Claude Code plugin mechanism supported by the current environment. The expected
plugin root is:

```text
small-business-japan
```

## Manual Claude Code script

Use this prompt after local install:

```text
日本向けの小規模事業ワークフローを初期設定して。
私は小さな制作会社で、今は請求書PDFが1枚と銀行CSVだけあります。
外部送信や提出はしないで、最初に何を渡せばいいかと、税理士に確認する質問を整理してください。
```

Expected behavior:

- Claude routes to `smb-onboard-jp`.
- Claude asks for one source at a time or proceeds with the stated sources.
- Claude produces:
  - Business context draft.
  - Available data.
  - First safe workflow.
  - What it can do now.
  - What a connector would unlock later.
  - Output format.
  - Approval boundary.
  - Next owner action.
- Claude explains that v0 accepts export files, uploaded files, and pasted text;
  it does not emit tool-specific import CSVs or accounting / invoice write data.
- Claude does not claim tax/legal/labor/accounting advice.
- Claude does not attempt to send, submit, write to tools, or impersonate a
  professional.

## Computer Use test idea

When Claude Code UI / Claude Code app is available in the desktop session:

1. Open Claude Code.
2. Install or select the local `small-business-japan` plugin.
3. Paste the manual script above.
4. Capture the response.
5. Check the response against the expected behavior list.

This walkthrough is intentionally connector-free. It proves that the first
experience works before any live tool dependency is introduced. Actual
marketplace registration and interactive installation remain separate gates
because this Starter Pack should not modify a user's Claude Code plugin config
during repository validation.
