#!/usr/bin/env python3
"""
check-agent-context-size.py

Fails if AGENTS.md or .github/copilot-instructions.md exceed configured line limits.
Run in CI to prevent always-loaded context from growing back to a doctrine dump.

Exit codes:
  0 — All files within limits
  1 — One or more files exceed their limit
"""
import pathlib
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

LIMITS = {
    "AGENTS.md":                              150,
    ".github/copilot-instructions.md":        1000,  # copilot-instructions is allowed to be larger
}

failures = []

for rel_path, max_lines in LIMITS.items():
    path = REPO_ROOT / rel_path
    if not path.exists():
        print(f"⚠️  {rel_path} not found — skipping")
        continue
    lines = path.read_text(encoding="utf-8").splitlines()
    count = len(lines)
    if count > max_lines:
        failures.append(f"❌  {rel_path}: {count} lines (limit: {max_lines})")
    else:
        print(f"✅  {rel_path}: {count} lines (limit: {max_lines})")

if failures:
    print("\nContext size check FAILED:")
    for msg in failures:
        print(f"  {msg}")
    print("\nTo fix: move long procedures to .github/skills/<name>/SKILL.md")
    sys.exit(1)

print("\n✅ All agent context files within size limits.")
