#!/usr/bin/env python3
"""Validate spec YAML front matter against JSON Schemas.

Usage:
  python scripts/validate-spec-structure.py [path ...]
If no paths supplied, scans spec-kit-templates usage patterns & phase folders.

Exit codes:
 0 success
 1 validation errors
 2 internal error
"""
from __future__ import annotations
import sys, re, json, subprocess, pathlib, typing as t

try:
    import yaml  # type: ignore
except ImportError:
    print("Missing dependency pyyaml. Install with: pip install pyyaml jsonschema", file=sys.stderr)
    sys.exit(2)
try:
    import jsonschema  # type: ignore
except ImportError:
    print("Missing dependency jsonschema. Install with: pip install jsonschema", file=sys.stderr)
    sys.exit(2)

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / 'spec-kit-templates' / 'schemas'
SCHEMA_MAP = {
    'requirements': SCHEMA_DIR / 'requirements-spec.schema.json',
    'architecture': SCHEMA_DIR / 'architecture-spec.schema.json',
}

FRONT_MATTER_RE = re.compile(r'^---\n(.*?)\n---', re.DOTALL)

class ValidationIssue(t.NamedTuple):
    file: pathlib.Path
    message: str


def extract_front_matter(text: str) -> t.Optional[str]:
    m = FRONT_MATTER_RE.match(text)
    return m.group(1) if m else None


def parse_yaml_block(block: str) -> t.Optional[dict]:
    try:
        return yaml.safe_load(block) or {}
    except Exception as e:
        return None


def load_schema(spec_type: str) -> dict:
    p = SCHEMA_MAP.get(spec_type)
    if not p or not p.exists():
        raise FileNotFoundError(f"No schema for specType={spec_type}")
    return json.loads(p.read_text(encoding='utf-8'))


def validate_spec(path: pathlib.Path) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    text = path.read_text(encoding='utf-8', errors='ignore')
    fm_raw = extract_front_matter(text)
    if not fm_raw:
        issues.append(ValidationIssue(path, 'Missing YAML front matter (--- block)'))
        return issues
    meta = parse_yaml_block(fm_raw)
    if meta is None:
        issues.append(ValidationIssue(path, 'Invalid YAML front matter'))
        return issues
    spec_type = meta.get('specType')
    if not spec_type:
        issues.append(ValidationIssue(path, 'Missing specType in front matter'))
        return issues
    try:
        schema = load_schema(spec_type)
    except Exception as e:
        issues.append(ValidationIssue(path, f'Schema load error: {e}'))
        return issues
    validator = jsonschema.Draft7Validator(schema)
    for err in validator.iter_errors(meta):
        issues.append(ValidationIssue(path, f"Schema violation: {'/'.join(map(str, err.path)) or '<root>'}: {err.message}"))

    # Additional cross-field custom checks
    if spec_type == 'requirements':
        # Ensure at least one Functional (REQ-F-) or Non-Functional (REQ-NF-) ID present in body
        if not re.search(r'REQ-(F|NF)-\d{3}', text):
            issues.append(ValidationIssue(path, 'No REQ-* identifiers found in body'))
    if spec_type == 'architecture':
        # Ensure at least one ARC-C- or ADR reference
        if not re.search(r'ADR-\d{3}', text):
            issues.append(ValidationIssue(path, 'No ADR-XXX references found in architecture spec'))
    return issues


def discover_targets(explicit: list[str]) -> list[pathlib.Path]:
    if explicit:
        return [pathlib.Path(p).resolve() for p in explicit]
    candidates: list[pathlib.Path] = []
    for pattern in [
        '02-requirements/**/*.md',
        '03-architecture/**/*.md',
    ]:
        candidates.extend(ROOT.glob(pattern))
    return [c for c in candidates if c.is_file()]


def main(argv: list[str]) -> int:
    targets = discover_targets(argv[1:])
    if not targets:
        print('No spec files found to validate', file=sys.stderr)
        return 0
    all_issues: list[ValidationIssue] = []
    for path in targets:
        if path.name.startswith('README'):  # skip readmes
            continue
        issues = validate_spec(path)
        if issues:
            for issue in issues:
                print(f"❌ {issue.file.relative_to(ROOT)}: {issue.message}")
            all_issues.extend(issues)
        else:
            print(f"✅ {path.relative_to(ROOT)} valid")
    if all_issues:
        print(f"\nFailed: {len(all_issues)} validation issues across {len(set(i.file for i in all_issues))} files.")
        return 1
    print("All specs validated successfully.")
    return 0

if __name__ == '__main__':  # pragma: no cover
    sys.exit(main(sys.argv))
