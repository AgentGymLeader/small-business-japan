---
name: tax-prep-jp
version: 0.1.0
description: >
  申告シーズンに向けたフルチェックを実行するオーケストレーター。
  month-end-prep-jp と tax-season-organizer-jp を連続実行し、
  税理士との最終確認に備える。
---

# Tax Prep JP

## Quick start

月次締め準備と税理士確認パケット作成を順番に実行し、
申告準備を一括で完了させるオーケストレータースキル。

## Workflow

### Step 1 — 月次データの最終整理 (month-end-prep-jp)

`month-end-prep-jp` スキルを実行する：
1. 未分類取引・証憑抜けの検出
2. 未収・未払いの最終確認
3. 固定費の計上漏れチェック

Step 1 の結果をオーナーに提示する。重大な未処理項目がある場合は、
Step 2 に進む前にオーナーの確認を得る。

### Step 2 — 税理士確認パケットの作成 (tax-season-organizer-jp)

`tax-season-organizer-jp` スキルを実行する：
1. インボイス・消費税の確認
2. 税理士への確認事項リストアップ
3. 確認パケット（メモ）の作成

### Step 3 — 統合サマリーの出力

両スキルの結果を統合してサマリーを作成する：

```
申告準備サマリー — {事業年度}

【データ整理状況】
{month-end-prepの結果サマリー}

【税理士確認事項】
{tax-season-organizerの確認事項リスト}

【次のステップ】
1. 未処理項目の対応（{件数}件）
2. 税理士との確認ミーティング設定
3. 申告期限の確認（{日付}）
```

## Approval gates

各ステップのApproval gatesに従う。
- **申告書の作成・送信・提出は行わない。**
- **税務判断は税理士に相談するよう促す。**
- オーナーの明示的な承認なしに、Step 2 以降の処理は実行しない（Step 1 で重大な未処理項目が残っている場合）。
- オーナーの明示的な承認なしに、電子申告システムへのデータ送信・申告書の提出は行わない。

## Reference

- [month-end-prep-jp](../month-end-prep-jp/SKILL.md)
- [tax-season-organizer-jp](../tax-season-organizer-jp/SKILL.md)
