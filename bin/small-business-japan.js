#!/usr/bin/env node
import { existsSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const ROOT = dirname(dirname(fileURLToPath(import.meta.url)));

function readJson(path) {
  return JSON.parse(readFileSync(path, "utf8"));
}

function commandExists(name, args = ["--version"]) {
  const result = spawnSync(name, args, { encoding: "utf8" });
  return result.status === 0;
}

function doctor() {
  const manifestPath = join(ROOT, ".claude-plugin", "plugin.json");
  const mcpPath = join(ROOT, ".mcp.json");
  const promptPath = join(ROOT, "docs", "install", "claude-code-install-prompt.ja.md");
  const failures = [];

  if (!existsSync(manifestPath)) {
    failures.push("missing .claude-plugin/plugin.json");
  }
  if (!existsSync(mcpPath)) {
    failures.push("missing .mcp.json");
  }
  if (!existsSync(promptPath)) {
    failures.push("missing docs/install/claude-code-install-prompt.ja.md");
  }

  if (existsSync(manifestPath)) {
    const manifest = readJson(manifestPath);
    if (manifest.name !== "small-business-japan") {
      failures.push("plugin manifest name must be small-business-japan");
    }
    if (manifest.license !== "Apache-2.0") {
      failures.push("plugin manifest license must be Apache-2.0");
    }
  }

  if (existsSync(mcpPath)) {
    const mcp = readJson(mcpPath);
    if (JSON.stringify(mcp.mcpServers) !== "{}") {
      failures.push("starter pack must not require MCP servers");
    }
  }

  console.log("Small Business Japan doctor");
  console.log(`- node: ${process.version}`);
  console.log(`- npm/npx: ${commandExists("npm") ? "found" : "not found"}`);
  console.log(`- claude: ${commandExists("claude") ? "found" : "not found"}`);
  console.log("- distribution: @agentgymleader community contribution; unofficial until upstream adoption");
  console.log("- output policy: memo/draft/checklist only; no tool-specific import CSV in v0");

  if (failures.length) {
    console.error("\nFAIL");
    for (const failure of failures) console.error(`- ${failure}`);
    return 1;
  }

  console.log("\nPASS");
  console.log("Run `small-business-japan print-claude-code-prompt` for the paste prompt.");
  return 0;
}

function printClaudeCodePrompt() {
  const promptPath = join(ROOT, "docs", "install", "claude-code-install-prompt.ja.md");
  console.log(readFileSync(promptPath, "utf8"));
  return 0;
}

function help() {
  console.log(`Small Business Japan

Usage:
  small-business-japan doctor
  small-business-japan print-claude-code-prompt

This is an @agentgymleader npx helper for a connector-free Claude Code workflow pack.
It is unofficial until upstream adoption and does not send, file,
write, or connect to business tools by itself.`);
  return 0;
}

const command = process.argv[2] || "help";
const status = command === "doctor"
  ? doctor()
  : command === "print-claude-code-prompt"
    ? printClaudeCodePrompt()
    : help();

process.exit(status);
