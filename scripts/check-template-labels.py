#!/usr/bin/env python3
"""
check-template-labels.py

Fails if any issue template in .github/ISSUE_TEMPLATE/ emits labels that are not
canonical type:* or phase:* labels.

Canonical labels start with:
  - type:
  - phase:

Legacy labels (anything else) are only allowed in create-labels scripts as fallbacks,
never in templates.

Exit codes:
  0 — All templates use only canonical labels
  1 — One or more templates emit non-canonical labels
"""
import pathlib
import re
import sys
import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE_DIR = REPO_ROOT / ".github" / "ISSUE_TEMPLATE"

CANONICAL_PREFIXES = ("type:", "phase:")

# Labels that are permitted in templates (security, bug, etc. are GitHub built-ins)
ALLOWED_EXCEPTIONS = frozenset()

failures = []

for template_file in sorted(TEMPLATE_DIR.glob("*.yml")):
    if template_file.name == "config.yml":
        continue
    try:
        data = yaml.safe_load(template_file.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        print(f"⚠️  {template_file.name}: YAML parse error — {e}")
        continue

    labels = data.get("labels", [])
    if not isinstance(labels, list):
        labels = [labels]

    bad = [
        lbl for lbl in labels
        if not any(lbl.startswith(p) for p in CANONICAL_PREFIXES)
        and lbl not in ALLOWED_EXCEPTIONS
    ]

    if bad:
        failures.append(
            f"❌  {template_file.name}: non-canonical labels: {bad}"
            "\n    Fix: use type:* and phase:* labels only"
        )
    else:
        print(f"✅  {template_file.name}: labels OK ({labels})")

if failures:
    print("\nTemplate label check FAILED:")
    for msg in failures:
        print(f"  {msg}")
    print(
        "\nAll templates must emit canonical labels (type:* and phase:*).\n"
        "Legacy labels belong only in scripts/create-labels.* as fallbacks."
    )
    sys.exit(1)

print("\n✅ All issue templates use canonical labels.")
