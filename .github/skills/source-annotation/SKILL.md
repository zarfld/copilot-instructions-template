---
name: source-annotation
description: >
  Rules and procedural steps for adding @implements and @verifies traceability
  annotations to source code and test files. Use when writing new source files,
  adding test functions, or auditing existing code for missing traceability.
triggers:
  - "add traceability annotation"
  - "annotate source file"
  - "add @implements"
  - "add @verifies"
  - "source traceability"
  - "code header traceability"
  - "missing traceability annotation"
tools: ["read", "search", "edit"]
---

# Skill: Source Annotation

## Purpose

Every production source file and test file must reference the GitHub Issues it implements or verifies. This creates bidirectional traceability from code back to requirements.

## Required Annotation Forms

All four forms are valid and must be recognized by scanners:

```python
# @implements #123 REQ-F-XYZ-001
# @implements REQ-F-XYZ-001 (#123)
# @verifies #456 REQ-F-XYZ-001
# @verifies REQ-F-XYZ-001 (#456)
```

**Orphan annotations (missing `#N`) must fail CI scanner:**
```python
# @implements REQ-F-XYZ-001          ← FAIL: no #N
# @verifies REQ-NF-PERF-001          ← FAIL: no #N
```

## Production File Header (Required)

Every source module must have a top-of-file annotation block.

**Python:**
```python
"""
<Module description>

Implements: #45 REQ-F-AUTH-001: User Login
Implements: #46 REQ-NF-SECU-002: Session Security
Architecture: #78 ADR-SECU-001: JWT Authentication

See: https://github.com/<owner>/<repo>/issues/45
"""
```

**TypeScript/JavaScript:**
```typescript
/**
 * <Module description>
 *
 * @implements #45 REQ-F-AUTH-001: User Login
 * @implements #46 REQ-NF-SECU-002: Session Security
 * @architecture #78 ADR-SECU-001: JWT Authentication
 *
 * @see https://github.com/<owner>/<repo>/issues/45
 */
```

**C/C++:**
```c
/*
 * <Module description>
 *
 * @implements #45 REQ-F-CTRL-001: Channel status query
 * @verifies   #89 TEST-CTRL-STATUS-001
 */
```

## Test File Annotation (Required)

Every test function must reference the requirement it verifies.

**Python:**
```python
"""
Verifies: #45 REQ-F-AUTH-001: User Login
"""

def test_login_success():
    """
    Verifies: #45 REQ-F-AUTH-001
    Scenario: Given valid credentials → auth token returned
    """
    ...
```

**TypeScript (Jest):**
```typescript
describe('User Login', () => {
  /**
   * @verifies #45 REQ-F-AUTH-001: User Login
   */
  it('should authenticate with valid credentials', async () => {
    ...
  });
});
```

## Procedural Steps

### Adding annotations to a new source file

1. Identify the REQ issues (from the IMP or design task) this file implements.
2. Add `@implements #N REQ-ID` at the top of the file for each requirement.
3. If the file is a test file, use `@verifies` instead of `@implements`.
4. For HIL fixture-backed tests, also add `# Fixture source: PROBE #N`.

### Auditing an existing file for missing annotations

1. Run `grep -rn "@implements\|@verifies\|Implements:\|Verifies:" <path>` to find annotated files.
2. For files with no annotation, identify the relevant requirement from git blame, PR history, or issue tracker.
3. Add the annotation. If no requirement exists, create one before annotating.
4. Verify that every `@implements REQ-ID` and `@verifies REQ-ID` includes `#N`.

### Detecting orphan annotations

An annotation is an orphan if it has a REQ ID but no `#N`. These must be resolved:

```bash
# Detect orphans: @implements REQ-F-... without (#N) or #N
grep -rn "@implements REQ-\|@verifies REQ-" src/ tests/ | grep -v "#[0-9]"
```

Any match is a CI failure. Fix by adding the issue number.

## Acceptance Criteria

- [ ] Every production source file has at least one `@implements #N` or `Implements: #N` annotation
- [ ] Every test file has at least one `@verifies #N` or `Verifies: #N` annotation
- [ ] No annotation has a REQ-ID without a corresponding `#N`
- [ ] HIL fixture-backed tests include `# Fixture source: PROBE #N`
- [ ] Scanner recognizes all four annotation forms listed above

## References

- [.github/instructions/phase-05-implementation.instructions.md](../instructions/phase-05-implementation.instructions.md)
- [.github/prompts/test-validate.prompt.md](../prompts/test-validate.prompt.md)
- [scripts/build-traceability.py](../../scripts/build-traceability.py)
