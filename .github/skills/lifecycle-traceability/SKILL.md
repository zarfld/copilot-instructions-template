---
name: lifecycle-traceability
description: >
  Procedural steps for creating, linking, and validating GitHub Issues as
  lifecycle traceability artifacts. Use when creating any StR, REQ-F, REQ-NF,
  ADR, ARC-C, QA-SC, IMP, TEST, PROBE, BUG, EPIC, DOC, or HOUSEKEEPING issue,
  or when checking bidirectional traceability coverage.
triggers:
  - "create a requirement issue"
  - "create a test case"
  - "link issues"
  - "check traceability"
  - "trace to parent"
  - "verify traceability coverage"
  - "create ADR"
  - "create PROBE"
tools: ["githubRepo", "read", "search"]
---

# Skill: Lifecycle Traceability

## Purpose

Enforce bidirectional GitHub Issue traceability across all lifecycle phases.

## Canonical Traceability Contract

```markdown
# Upward link (REQ / ADR / ARC-C / IMP / PROBE / DOC use this)
## Traceability
- Traces to:  #123

# TEST issues use this (plain, NOT bold)
## Traceability
- Verifies: #45
```

**Rejected verbs** (never use in issue bodies): `Satisfies:`, `Links to:`, `Parent:`, `Tests:`, `Validates:`, `Related to:`, bold-Verifies (i.e. `- **Verifies**: #N` with asterisks — always use plain `- Verifies: #N`).

## Issue Prefix → Canonical Label Table

| Prefix | Label | Phase label |
|---|---|---|
| `[StR]` | `type:stakeholder-requirement` | `phase:01-stakeholder-requirements` |
| `[REQ-F]` | `type:requirement:functional` | `phase:02-requirements` |
| `[REQ-NF]` | `type:requirement:non-functional` | `phase:02-requirements` |
| `[ADR]` | `type:architecture:decision` | `phase:03-architecture` |
| `[ARC-C]` | `type:architecture:component` | `phase:03-architecture` |
| `[QA-SC]` | `type:architecture:quality-scenario` | `phase:03-architecture` |
| `[TEST]` | `type:test-case` | `phase:07-verification-validation` |
| `[IMP]` | `type:implementation` | `phase:05-implementation` |
| `[PROBE]` | `type:probe` | `phase:05-implementation` |
| `[BUG]` | `type:bug` | *(any)* |
| `[EPIC]` | `type:epic` | *(any)* |
| `[DOC]` | `type:documentation` | *(any)* |
| `[HOUSEKEEPING]` | `type:housekeeping` | *(any)* |

## Procedural Steps

### Creating an issue with correct traceability

1. Select the appropriate issue template from `.github/ISSUE_TEMPLATE/`.
2. Confirm the title starts with the bracketed prefix (e.g., `[REQ-F] `).
3. Confirm the `labels:` field contains the canonical `type:*` and `phase:*` labels.
4. In the **Traceability** section, add `- Traces to:  #N` for the parent issue (two spaces before `#`).
   - Exception: StR issues have no parent — skip this field.
   - Exception: TEST issues use `- Verifies: #N` instead of `Traces to:`.
5. Submit the issue. CI will validate the syntax automatically.

### Checking traceability coverage

1. Run `python scripts/github-traceability-report.py` to generate the matrix.
2. Check the "Requirements Without Tests" section — every REQ-F and REQ-NF should have at least one TEST with `Verifies: #N`.
3. Check the "Orphaned Requirements" section — every issue should trace upward to a StR.
4. Run `python scripts/github-orphan-check.py` for orphan detection.

### Fixing a broken traceability link

1. Identify the missing link type (upward `Traces to:` or `Verifies:`).
2. Edit the issue body to add the correct syntax.
3. CI will re-validate on the next `issues: edited` event.

## Acceptance Criteria

- [ ] Every REQ-F/REQ-NF contains `- Traces to:  #N` pointing to a valid StR
- [ ] Every ADR/ARC-C contains `- Traces to:  #N` pointing to a valid REQ
- [ ] Every TEST contains `- Verifies: #N` pointing to a valid REQ (plain, not bold)
- [ ] No issue body contains `Satisfies:`, bold-Verifies (with asterisks), or `Parent:` as traceability verbs
- [ ] `github-traceability-report.py` shows 0 orphaned requirements

## References

- [docs/github-issue-workflow.md](../../docs/github-issue-workflow.md)
- [docs/QUICK-START-github-issues.md](../../docs/QUICK-START-github-issues.md)
- Issue templates: `.github/ISSUE_TEMPLATE/`
- Validation script: `scripts/github-orphan-check.py`
- Traceability report: `scripts/github-traceability-report.py`
