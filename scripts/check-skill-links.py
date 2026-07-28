#!/usr/bin/env python3
"""
check-skill-links.py

Fails if any skill path referenced in AGENTS.md does not exist as a file.

Scans AGENTS.md for patterns like:
  `.github/skills/<name>/SKILL.md`
  `.github/instructions/<file>.instructions.md`

Exit codes:
  0 — All referenced skill/instruction paths exist
  1 — One or more referenced paths are missing
"""
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
AGENTS_MD = REPO_ROOT / "AGENTS.md"

if not AGENTS_MD.exists():
    print("⚠️  AGENTS.md not found — skipping skill link check")
    sys.exit(0)

text = AGENTS_MD.read_text(encoding="utf-8")

# Match backtick-quoted paths that look like skill or instruction file references
path_pattern = re.compile(r'`(\.github/(?:skills|instructions)/[^`]+\.md)`')

found = set(path_pattern.findall(text))

if not found:
    print("⚠️  No skill/instruction paths found in AGENTS.md — check routing table syntax")
    sys.exit(0)

failures = []
for rel_path in sorted(found):
    abs_path = REPO_ROOT / rel_path
    if abs_path.exists():
        print(f"✅  {rel_path}")
    else:
        failures.append(rel_path)

if failures:
    print("\nSkill link check FAILED — referenced paths do not exist:")
    for p in failures:
        print(f"  ❌  {p}")
    print(
        "\nFix: create the missing SKILL.md files or correct the path in AGENTS.md"
    )
    sys.exit(1)

print(f"\n✅ All {len(found)} skill/instruction links in AGENTS.md exist.")
