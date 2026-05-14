#!/usr/bin/env python3
"""Validate the Small Business Japan starter plugin.

This is intentionally dependency-free. It checks the public artifact shape,
approval boundary language, and starter-file presence without requiring Claude
Code, MCP servers, or live connectors.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT

REQUIRED_FILES = [
    ".claude-plugin/plugin.json",
    ".mcp.json",
    "package.json",
    "NOTICE.md",
    "bin/small-business-japan.js",
    "README.md",
    "README.ja.md",
    "docs/install/README.ja.md",
    "docs/install/claude-code-install-prompt.ja.md",
    "skills/smb-router-jp/SKILL.md",
    "skills/smb-onboard-jp/SKILL.md",
    "skills/smb-onboard-jp/reference/onboard-checklist.md",
    "outputs/smb-onboard-jp/output.md",
    "outputs/smb-onboard-jp/research/2026-05-14.md",
    "outputs/smb-onboard-jp/research/latest.md",
    "outputs/invoice-chase-jp/output.md",
    "outputs/invoice-chase-jp/research/2026-05-14.md",
    "outputs/invoice-chase-jp/research/latest.md",
    "outputs/README.md",
    "research/upstream-recon/2026-05-14.md",
    "research/professional-boundary/2026-05-14.md",
    "redteam/professional-boundary-prompts.md",
    "docs/walkthrough/claude-code-walkthrough.md",
]

EXPECTED_OUTPUTS = [
    "cash-flow-snapshot-jp",
    "invoice-chase-jp",
    "margin-analyzer-jp",
    "month-end-prep-jp",
    "tax-season-organizer-jp",
    "lead-triage-jp",
    "content-strategy-jp",
    "design-tool-handoff-jp",
    "customer-pulse-jp",
    "ticket-deflector-jp",
    "crm-maintenance-jp",
    "contract-review-jp",
    "job-post-builder-jp",
    "business-pulse-jp",
    "smb-onboard-jp",
]

OUTPUT_REQUIRED_TERMS = [
    "Owner action boundary:",
    "## Mandatory output header",
    "Small Business Japan by @agentgymleader",
    "older than 180 days",
    "## Purpose",
    "## Inputs",
    "## Required output sections",
    "## Japan compliance checks",
    "## Negative scope",
    "## Approval pause",
    "## Output format",
    "## Refresh trigger",
]

RESEARCH_REQUIRED_TERMS = [
    "Research date: 2026-05-14",
    "## Summary",
    "## Sources consulted",
    "## Safe flags",
    "## Forbidden claims",
    "## Memo-only implications",
    "## Refresh trigger",
]

README_HEADINGS = [
    "## Installation",
    "## What you'll need to connect",
    "## What it outputs",
    "## How it works",
    "## All 15 commands",
    "## All 15 skills",
    "## Customizing",
]

JA_README_HEADINGS = [
    "## インストール",
    "## はじめに必要なもの",
    "## 出力されるもの",
    "## 動き方",
    "## 15個のコマンド",
    "## 15個のスキル",
    "## 自社向けに調整する",
]

BOUNDARY_TERMS = [
    "does not provide financial, tax, legal",
    "does not represent you",
    "submit filings",
    "without your explicit approval",
]

JA_BOUNDARY_TERMS = [
    "経営判断を代わりに行う",
    "申請",
    "外部",
    "オーナーの確認",
]

FORBIDDEN_PUBLIC_CLAIMS = [
    "Anthropic-approved",
    "Claude-certified",
    "official Anthropic",
    "税理士判断済み",
    "社労士確認済み",
    "行政書士確認済み",
    "弁護士確認済み",
    "提出可能",
    "申請可能",
    "法的に問題ありません",
    "税務上問題ありません",
    "代理送信",
    "代行提出",
]

INSTALL_TERMS = [
    "npx @agentgymleader/small-business-japan doctor",
    "print-claude-code-prompt",
]

EN_INSTALL_TERMS = ["community contribution"]

JA_INSTALL_TERMS = ["@agentgymleader", "非公式の配布"]

PRIVACY_TERMS = ["Data privacy", "customer data", "confidential business information"]

OUTPUT_TERMS = [
    "memo-only",
    "field-mapping memo",
]

EN_OUTPUT_TERMS = ["tool-specific import CSV"]

JA_OUTPUT_TERMS = ["memo-only", "項目の対応"]

JA_COMMANDS = [
    "/支払準備",
    "/来月資金",
    "/月次締め準備",
    "/価格確認",
    "/税理士確認パケット",
    "/営業連絡リスト",
    "/キャンペーン準備",
    "/売上ブリーフ",
    "/顧客の声確認",
    "/クレーム返信準備",
    "/CRM整理",
    "/契約論点確認",
    "/月曜ブリーフ",
    "/金曜ふりかえり",
    "/四半期レビュー",
]

INVOICE_TERMS = [
    "qualified invoice registration number candidate",
    "`T` plus 13 digits",
    "tool-specific import CSV",
    "transitional measures may apply",
    "valid qualified invoice",
    "input tax credit",
    "memo-only",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def require_file(path: str) -> Path:
    target = PLUGIN / path
    if not target.exists():
        fail(f"missing {target.relative_to(ROOT)}")
    return target


def require_contains(text: str, needle: str, path: Path) -> None:
    if needle not in text:
        fail(f"{path.relative_to(ROOT)} missing {needle!r}")


def main() -> int:
    if not (PLUGIN / ".claude-plugin" / "plugin.json").exists():
        fail("missing plugin manifest at .claude-plugin/plugin.json")

    for path in REQUIRED_FILES:
        require_file(path)

    manifest = json.loads(require_file(".claude-plugin/plugin.json").read_text())
    if manifest.get("name") != "small-business-japan":
        fail("plugin manifest name must be small-business-japan")
    if manifest.get("license") != "Apache-2.0":
        fail("plugin manifest license must be Apache-2.0")

    package = json.loads(require_file("package.json").read_text())
    if package.get("name") != "@agentgymleader/small-business-japan":
        fail("package.json name must be scoped to @agentgymleader")
    if package.get("bin", {}).get("small-business-japan") != "bin/small-business-japan.js":
        fail("package.json must expose small-business-japan bin")
    package_files = package.get("files", [])
    for internal_path in ["docs/approval", "docs/reviews", "docs/dogfood"]:
        if internal_path in package_files:
            fail(f"package.json files must not publish internal path: {internal_path}")

    mcp = json.loads(require_file(".mcp.json").read_text())
    if mcp.get("mcpServers") != {}:
        fail("Starter Pack must not require MCP servers")

    readme = require_file("README.md")
    readme_text = readme.read_text(encoding="utf-8")
    for heading in README_HEADINGS:
        require_contains(readme_text, heading, readme)
    for term in BOUNDARY_TERMS:
        require_contains(readme_text, term, readme)
    for term in INSTALL_TERMS + EN_INSTALL_TERMS + PRIVACY_TERMS + OUTPUT_TERMS + EN_OUTPUT_TERMS + JA_COMMANDS:
        require_contains(readme_text, term, readme)

    ja_readme = require_file("README.ja.md")
    ja_text = ja_readme.read_text(encoding="utf-8")
    for heading in JA_README_HEADINGS:
        require_contains(ja_text, heading, ja_readme)
    for term in JA_BOUNDARY_TERMS:
        require_contains(ja_text, term, ja_readme)
    for term in INSTALL_TERMS + JA_INSTALL_TERMS + JA_OUTPUT_TERMS + JA_COMMANDS:
        require_contains(ja_text, term, ja_readme)
    for term in ["データの扱い", "個人情報", "顧客情報", "機密情報"]:
        require_contains(ja_text, term, ja_readme)

    install_prompt = require_file("docs/install/claude-code-install-prompt.ja.md")
    install_prompt_text = install_prompt.read_text(encoding="utf-8")
    for term in ["npx", "非公式", "import CSV", "提出はしないでください"]:
        require_contains(install_prompt_text, term, install_prompt)

    invoice_contract = require_file("outputs/invoice-chase-jp/output.md")
    invoice_text = invoice_contract.read_text(encoding="utf-8")
    for term in INVOICE_TERMS:
        require_contains(invoice_text, term, invoice_contract)

    for output in EXPECTED_OUTPUTS:
        output_path = require_file(f"outputs/{output}/output.md")
        output_text = output_path.read_text(encoding="utf-8")
        require_contains(output_text, f"# Output Contract: {output}", output_path)
        for term in OUTPUT_REQUIRED_TERMS:
            require_contains(output_text, term, output_path)

        dossier_path = require_file(f"outputs/{output}/research/2026-05-14.md")
        dossier_text = dossier_path.read_text(encoding="utf-8")
        require_contains(dossier_text, f"# Research Dossier: {output}", dossier_path)
        require_contains(dossier_text, f"Output: `{output}`", dossier_path)
        for term in RESEARCH_REQUIRED_TERMS:
            require_contains(dossier_text, term, dossier_path)

        latest_path = require_file(f"outputs/{output}/research/latest.md")
        latest_text = latest_path.read_text(encoding="utf-8")
        require_contains(latest_text, "2026-05-14.md", latest_path)

    public_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [
            readme,
            ja_readme,
            require_file("skills/smb-onboard-jp/SKILL.md"),
            require_file("skills/smb-router-jp/SKILL.md"),
            require_file("outputs/smb-onboard-jp/output.md"),
            require_file("outputs/invoice-chase-jp/output.md"),
        ]
    )
    for claim in FORBIDDEN_PUBLIC_CLAIMS:
        if claim in public_text:
            fail(f"forbidden public claim present: {claim}")

    print("Small Business Japan starter validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
