#!/usr/bin/env python3
"""
check-traceability-syntax.py

Scans normative files (prompts, instructions, issue templates) for forbidden
traceability verb substitutes that would break CI parsers or mislead agents.

Forbidden patterns in normative files:
  - **Verifies**: (bold — use plain Verifies:)
  - Satisfies:   (use Traces to: for ADR/ARC-C)
  - Links to:    (use Traces to:)
  - Parent:      (use Traces to:)
  - Tests:       (use Verifies: in TEST issues)
  - Validates:   (use Verifies: in TEST issues)
  - Related to:  (not a traceability verb)

Exit codes:
  0 — No forbidden patterns found
  1 — Forbidden patterns found
"""
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

SCAN_DIRS = [
    ".github/prompts",
    ".github/instructions",
    ".github/ISSUE_TEMPLATE",
    ".github/skills",
]

# Skip old backup files — those are scheduled for deletion
SKIP_SUFFIXES = (".old",)

# (pattern, description)
FORBIDDEN = [
    (re.compile(r'\*\*Verifies\*\*\s*:', re.IGNORECASE),
     "bold **Verifies**: — use plain `Verifies:`"),
    (re.compile(r'(?<!\w)Satisfies\s*:\s*#\d+'),
     "Satisfies: #N — use `Traces to:  #N` for ADR/ARC-C"),
    (re.compile(r'(?<!\w)Links\s+to\s*:\s*#\d+'),
     "Links to: #N — use `Traces to:  #N`"),
    (re.compile(r'(?<!\w)Parent\s*:\s*#\d+'),
     "Parent: #N — use `Traces to:  #N`"),
    (re.compile(r'(?<!\w)Tests\s*:\s*#\d+'),
     "Tests: #N — use `Verifies: #N` in TEST issues"),
    (re.compile(r'(?<!\w)Validates\s*:\s*#\d+'),
     "Validates: #N — use `Verifies: #N` in TEST issues"),
    (re.compile(r'(?<!\w)Related\s+to\s*:\s*#\d+'),
     "Related to: #N — not a valid traceability verb"),
]

failures = []

for rel_dir in SCAN_DIRS:
    scan_dir = REPO_ROOT / rel_dir
    if not scan_dir.exists():
        continue
    for f in sorted(scan_dir.rglob("*")):
        if not f.is_file():
            continue
        if any(f.name.endswith(s) for s in SKIP_SUFFIXES):
            continue
        if f.suffix not in (".md", ".yml", ".yaml"):
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        lines_list = text.splitlines()
        for line_no, line in enumerate(lines_list, start=1):
            # Skip negative-example lines (❌ marker means "this is wrong, don't do it")
            if "❌" in line:
                continue
            # Strip inline code spans before checking — don't flag backtick-quoted examples
            clean = re.sub(r'`[^`\n]*`', '', line)
            for pattern, description in FORBIDDEN:
                if pattern.search(clean):
                    rel = f.relative_to(REPO_ROOT)
                    failures.append(f"  ❌  {rel}:{line_no}  [{description}]")

if failures:
    print("Traceability syntax check FAILED — forbidden verb substitutes found:\n")
    for msg in failures:
        print(msg)
    print(
        "\nFix: replace forbidden verbs with canonical forms:\n"
        "  Upward link → `- Traces to:  #N`\n"
        "  TEST verify → `- Verifies: #N`  (plain, no bold)"
    )
    sys.exit(1)

print("✅ No forbidden traceability syntax found.")
