# Small Business Japan install guide

Small Business Japan は `@agentgymleader` による community contribution です。
upstream maintainerに採用されるまでは配布経路は非公式ですが、利用体験は公式採用を
想定して、`npx` helperとClaude Codeに貼り付けるpromptを入口にします。

## 推奨入口

```bash
npx @agentgymleader/small-business-japan doctor
npx @agentgymleader/small-business-japan print-claude-code-prompt
```

まだnpm packageとして公開していない開発中のrepoでは、同じ確認をlocal fileから
実行します。

```bash
node bin/small-business-japan.js doctor
node bin/small-business-japan.js print-claude-code-prompt
claude plugin validate .
python scripts/validate_small_business_japan.py
```

## なぜ marketplace install と分けるか

- upstream採用前の配布では、Claude plugin marketplaceの公式pluginに見せない。
- `npx` は一時的なcommand runnerとして使い、global installを前提にしない。
- readiness check、boundary説明、Claude Code paste promptを先に出す。
- 外部送信、提出、会計/CRM/請求書ツール書き込みは初期体験に含めない。

## Data privacy

銀行CSV、請求書PDF、顧客メール、貼り付けた事業contextには個人情報、顧客情報、
機密情報が含まれることがあります。利用するLLMや組織のdata policyに従い、不要な
情報は削除し、secret、token、private repoの中身、内部URLは貼り付けないでください。

## 出力方針

v0は memo-only です。Claude Codeから特定ツール向けimport CSV、請求書発行data、
会計仕訳data、CRM更新file、送信用email fileは出しません。

出してよいもの:

- 確認メモ
- ドラフト文面
- チェックリスト
- 抽出項目候補
- missing data
- risk / escalation note
- 税理士・社労士・行政書士・弁護士への確認パケット

出さないもの:

- 会計ソフト投入用CSV
- 請求書発行ソフトのimport file
- 仕訳data
- 申告・提出用file
- 送信済み扱いの督促メール
- 外部toolへのwrite planを承認なしで実行する手順
