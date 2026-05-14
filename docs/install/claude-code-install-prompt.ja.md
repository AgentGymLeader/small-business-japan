# Claude Code install prompt

Small Business Japan は `@agentgymleader` による community contribution です。
upstream maintainerに採用されるまでは配布経路は非公式です。まず `npx` helper と
貼り付けpromptでreadinessを確認します。

`npx` は npm の一時的なcommand runnerです。global installを先に要求しない代わりに
npm packageのcodeを実行するため、package名が違う、Node.js / npm 権限が足りない、
または公開前packageが見つからない場合はそこで止めます。

## Paste this into Claude Code

```text
Small Business Japanをこのマシンで確認してください。

前提:
- Small Business Japanは`@agentgymleader`による日本向けcommunity contributionです。
- upstream maintainerに採用されるまでは配布経路は非公式です。
- Claude plugin marketplaceの公式pluginとして扱わないでください。
- 外部送信、提出、会計ツールへの書き込み、CRM更新、請求書発行、支払、返金はしないでください。
- 提出はしないでください。
- token、cookie、private repoの中身、顧客データ、内部URLを出力しないでください。
- `npx` はこのpackage用の一時的なcommand runnerとしてだけ使ってください。

手順:
1. Node.js、npm/npx、Claude Codeが使えるか確認してください。
2. 公開packageが利用可能なら `npx @agentgymleader/small-business-japan doctor` を実行してください。
3. このrepo内で確認する場合は `node bin/small-business-japan.js doctor` を実行してください。
4. `claude plugin validate .` が使える環境なら実行してください。
5. `python scripts/validate_small_business_japan.py` を実行してください。
6. 失敗したらそこで止まり、失敗理由と次の安全な確認だけを説明してください。
7. 成功したら、Small Business Japanが受け取る入力はexport file / uploaded file / pasted textであり、v0の出力はメモ、ドラフト、チェックリスト、士業確認パケットだけだと説明してください。
8. 特定ツール向けのimport CSV、請求書発行データ、会計仕訳データ、送信用メール、提出用ファイルは作らないでください。

最後に、次のサンプルをconnectorなしでdry-runしてください。

「日本向けの小規模事業ワークフローを初期設定して。私は小さな制作会社で、今は請求書PDFが1枚と銀行CSVだけあります。外部送信や提出はしないで、最初に何を渡せばいいかと、税理士に確認する質問を整理してください。」
```
