#!/usr/bin/env python3
"""Validate traceability coverage thresholds.

Reads build/traceability.json and enforces minimum linkage coverage for
requirements (REQ-*). Fails with non-zero exit code if below threshold.

Usage:
  python scripts/validate-trace-coverage.py --min-req 90
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACE_JSON = ROOT / 'build' / 'traceability.json'

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('--min-req', type=float, default=90.0, help='Minimum percent of REQ-* with at least one link')
    return ap.parse_args()

def main() -> int:
    args = parse_args()
    if not TRACE_JSON.exists():
        print('traceability.json missing; ensure spec-generation job ran first', file=sys.stderr)
        return 1
    data = json.loads(TRACE_JSON.read_text(encoding='utf-8'))
    metrics = data.get('metrics', {})
    req_metrics = metrics.get('REQ') or metrics.get('REQ-') or {}
    coverage = req_metrics.get('coverage_pct')
    if coverage is None:
        print('No REQ metrics found in traceability.json', file=sys.stderr)
        return 1
    if coverage < args.min_req:
        print(f"❌ Requirement linkage coverage {coverage:.2f}% < threshold {args.min_req:.2f}%")
        return 2
    print(f"✅ Requirement linkage coverage {coverage:.2f}% >= threshold {args.min_req:.2f}%")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
