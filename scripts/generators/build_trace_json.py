#!/usr/bin/env python3
"""Build Traceability JSON

Consumes build/spec-index.json and produces build/traceability.json capturing
forward and backward links for visualization or further QA tooling.
"""
from __future__ import annotations
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / 'build' / 'spec-index.json'
OUT = ROOT / 'build' / 'traceability.json'

PREFIX_ORDER = ['StR', 'REQ', 'ARC', 'ADR', 'QA', 'TEST']


def main() -> int:
    if not INDEX.exists():
        print('Missing spec-index.json; run spec_parser first')
        return 1
    data = json.loads(INDEX.read_text(encoding='utf-8'))
    items = data.get('items', [])
    by_id = {i['id']: i for i in items}

    forward = {i['id']: i.get('references', []) for i in items}
    backward = defaultdict(list)
    for src, refs in forward.items():
        for r in refs:
            backward[r].append(src)

    # Simple completeness metrics
    metrics = {}
    for prefix in PREFIX_ORDER:
        ids = [i['id'] for i in items if i['id'].startswith(prefix)]
        linked = [i for i in ids if any(b for b in forward[i])]
        metrics[prefix] = {
            'total': len(ids),
            'with_links': len(linked),
            'coverage_pct': (len(linked) / len(ids) * 100) if ids else 100.0,
        }

    OUT.write_text(
        json.dumps(
            {
                'items': items,
                'forward': forward,
                'backward': backward,
                'metrics': metrics,
            },
            indent=2,
        ),
        encoding='utf-8',
    )
    print(f"Wrote {OUT}")
    return 0

if __name__ == '__main__':
    import sys
    raise SystemExit(main())
