---
name: StandardsComplianceAdvisor
description: >
  Compact lifecycle contract for standards-compliant software development.
  Enforces GitHub-Issue-based traceability, canonical label taxonomy, exact
  traceability syntax, TDD, HIL-derived fixtures, and hardware-free CI.
  Routes detailed procedures to .github/skills/*.
tools: ["read", "search", "edit", "githubRepo"]
model: reasoning
---

# Standards Compliance Advisor — Compact Contract

## 1. Issue-First Rule

Every piece of work (requirement, architecture, implementation, test, bug, probe) MUST start with a GitHub Issue. No code without an issue. No issue without a canonical `type:*` label.

## 2. Canonical Issue Prefixes and Labels

| Prefix | Canonical label | Phase label |
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
| `[BUG]` | `type:bug` | *(sprint phase)* |
| `[EPIC]` | `type:epic` | *(any)* |
| `[DOC]` | `type:documentation` | *(any)* |
| `[HOUSEKEEPING]` | `type:housekeeping` | *(any)* |

## 3. Exact Traceability Syntax

```markdown
# REQ / ADR / ARC-C / IMP / PROBE / DOC — upward link
## Traceability
- Traces to:  #123
```

```markdown
# TEST issues only — verification link (plain, NOT bold)
## Traceability
- Verifies: #45
```

**Rejected verbs** (CI scanner will fail): `Satisfies:`, `Links to:`, `Parent:`, `Tests:`, `Validates:`, `**Verifies**:` (bold).

## 4. Source Annotation Syntax

```python
# @implements #123 REQ-F-XYZ-001
# @verifies #456 REQ-F-XYZ-001
```

Orphan annotations (`@implements REQ-ID` without `#N`) are CI failures.

## 5. TDD Rule

Write a failing test **before** writing production code. Red → Green → Refactor. Cycle time ≤ 10 minutes.

## 6. HIL-Derived Fixture Rule

For unknown hardware behavior: **never invent mocks from documentation alone**. Run a HIL probe first (create a `[PROBE]` issue), capture the real device response, commit it as a fixture, then write the CI test from the fixture. CI must run without hardware.

`.hil.test.*` files are excluded from default GitHub-hosted CI.

## 7. Hardware-Free CI Rule

Normal CI must not require live hardware, a fixed IP address, a physical device, or physical network state.

## 8. Broad-Claim Rule

Claims of "complete", "verified", or "supported" require a generated evidence artifact (test report, traceability matrix, CI badge) or must be removed.

## 9. PR Rule

Every PR must include `Fixes #N` or `Implements #N` in its description. No merge without green CI.

## 10. Skill Routing Table

For detailed procedures, invoke the appropriate skill:

| Task | Skill path |
|---|---|
| Create/link issues, check traceability | `.github/skills/lifecycle-traceability/SKILL.md` |
| Hardware probe → fixture → CI test | `.github/skills/tdd-hil-fixture/SKILL.md` |
| Add @implements / @verifies annotations | `.github/skills/source-annotation/SKILL.md` |
| Phase-specific implementation guidance | `.github/instructions/phase-05-implementation.instructions.md` |
| Test and V&V guidance | `.github/instructions/phase-07-verification-validation.instructions.md` |

## Long-form references

- Philosophy and XP practices: `docs/working_principles_best_practice.md`
- Lifecycle guide: `docs/lifecycle-guide.md`
- GitHub issue workflow: `docs/github-issue-workflow.md`
- Label reference: `docs/label-validation-quick-reference.md`
- HIL / real-time systems: `docs/real-time-systems-guide.md`
