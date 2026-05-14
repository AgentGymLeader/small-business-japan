---
name: business-pulse-jp
version: 0.1.0
description: >
  週次・月次の事業状況サマリーを作成するオーケストレーター。
  monday-brief-jp、friday-brief-jp、quarterly-review-jp を
  トリガーに応じて実行する。
---

# Business Pulse JP

## Quick start

事業の健全性指標を集約し、定期的な振り返りブリーフを作成する。
トリガーに応じて適切なスキルを呼び出す：
- 週のはじめ → `monday-brief-jp`
- 週の終わり → `friday-brief-jp`
- 四半期末 → `quarterly-review-jp`

## Workflow

1. **タイミングを確認する。** オーナーの質問から実行すべきブリーフを判断する：
   - 「週のはじめの確認」「今週の優先事項」「月曜のブリーフ」→ `monday-brief-jp`
   - 「今週の振り返り」「週末の確認」「金曜のふりかえり」→ `friday-brief-jp`
   - 「四半期の振り返り」「3ヶ月の総括」→ `quarterly-review-jp`

2. **対応するスキルを実行する。** 各スキルのワークフローに従って実行する。

## Approval gates

- **オーナーの明示的な承認なしに、外部サービス（freee・マネーフォワードクラウド等）へのデータ書き込みは行わない。**
- **帳簿の確定・締めはオーナーが税理士と確認してから行う。**

## Reference

- [monday-brief-jp](../monday-brief-jp/SKILL.md)
- [friday-brief-jp](../friday-brief-jp/SKILL.md)
- [quarterly-review-jp](../quarterly-review-jp/SKILL.md)
