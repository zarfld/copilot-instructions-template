#!/usr/bin/env python3
"""Generate a simple traceability matrix skeleton and orphan report.
Parses markdown files for ID patterns and produces:
 - reports/traceability-matrix.md (basic table placeholders)
 - reports/orphans.md (lists missing link elements)

Patterns recognized:
  StR-\d{3}
  REQ-(F|NF)-\d{3}
  ADR-\d{3}
  ARC-C-\d{3}
  QA-SC-\d{3}
  TEST-[A-Z0-9-]+ (any test id with prefix TEST-)

Heuristics (improve later):
 - If a REQ appears in architecture spec or ADR file, we assume linkage
 - Components appear if referenced in architecture spec or views
 - Scenarios appear if in architecture-quality-scenarios file

Exit code 0 even if orphans exist (validation script enforces later).
"""
from __future__ import annotations
import re, pathlib, os
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPORTS = ROOT / 'reports'
REPORTS.mkdir(exist_ok=True)

PATTERNS = {
    'stakeholder': re.compile(r'StR-\d{3}'),
    'requirement': re.compile(r'REQ-(?:F|NF)-\d{3}'),
    'adr': re.compile(r'ADR-\d{3}'),
    'component': re.compile(r'ARC-C-\d{3}'),
    'scenario': re.compile(r'QA-SC-\d{3}'),
    'test': re.compile(r'TEST-[A-Z0-9-]+'),
}

files = [p for p in ROOT.rglob('*.md') if 'node_modules' not in p.parts and 'reports' not in p.parts]
index: dict[str, set[str]] = {k: set() for k in PATTERNS}
occurrence: dict[str, dict[str, set[pathlib.Path]]] = {k: defaultdict(set) for k in PATTERNS}

for path in files:
    try:
        text = path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        continue
    for key, pat in PATTERNS.items():
        for match in pat.findall(text):
            index[key].add(match)
            occurrence[key][match].add(path)

# Simple linkage inference
req_links = defaultdict(set)  # requirement -> linked identifiers (adr/component/scenario/test)
for adr in index['adr']:
    # parse requirements referenced in ADR file names or contents
    for req in index['requirement']:
        for path in occurrence['adr'][adr]:
            if req in path.read_text(encoding='utf-8', errors='ignore'):
                req_links[req].add(adr)
for scen in index['scenario']:
    scen_text_files = occurrence['scenario'][scen]
    text = '\n'.join(p.read_text(encoding='utf-8', errors='ignore') for p in scen_text_files)
    for req in index['requirement']:
        if req in text:
            req_links[req].add(scen)
for comp in index['component']:
    comp_in_files = occurrence['component'][comp]
    text = '\n'.join(p.read_text(encoding='utf-8', errors='ignore') for p in comp_in_files)
    for req in index['requirement']:
        if req in text:
            req_links[req].add(comp)
for test in index['test']:
    # naive: if test id includes requirement id substring (rare) skip, else can't infer; placeholder
    pass

# Orphan detection
orphans = {
    'requirements_no_links': sorted([r for r in index['requirement'] if not req_links.get(r)]),
    'scenarios_no_req': sorted([
        s for s in index['scenario']
        if not any(s in links for links in req_links.values())
    ]),
    'components_no_req': sorted([
        c for c in index['component']
        if not any(c in links for links in req_links.values())
    ]),
    'adrs_no_req': sorted([
        a for a in index['adr']
        if not any(a in links for links in req_links.values())
    ]),
}

matrix_lines = [
    '# Traceability Matrix (Heuristic Draft)',
    '',
    '| Requirement | Linked Elements (ADR / Component / Scenario / Test) |',
    '|-------------|----------------------------------------------------|',
]
for req in sorted(index['requirement']):
    linked = ', '.join(sorted(req_links.get(req, []))) or '(none)'
    matrix_lines.append(f'| {req} | {linked} |')

(REPORTS / 'traceability-matrix.md').write_text('\n'.join(matrix_lines), encoding='utf-8')

orphan_lines = ['# Orphan Analysis', '']
for category, items in orphans.items():
    orphan_lines.append(f'## {category}')
    if not items:
        orphan_lines.append('- None')
    else:
        for item in items:
            orphan_lines.append(f'- {item}')
    orphan_lines.append('')
(REPORTS / 'orphans.md').write_text('\n'.join(orphan_lines), encoding='utf-8')

print('Generated reports/traceability-matrix.md and reports/orphans.md')
