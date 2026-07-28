#!/bin/bash
# GitHub Repository Label Configuration Script
# Purpose: Create all labels needed for GitHub Issues-based requirements tracking
# Standards: ISO/IEC/IEEE 29148:2018 (Requirements Engineering)

# ── Canonical Type Labels (type:*) ──────────────────────────────────────────
gh label create "type:stakeholder-requirement"      --description "StR: Business context and stakeholder needs" --color "0E8A16"
gh label create "type:requirement:functional"        --description "REQ-F: Functional system requirements" --color "1D76DB"
gh label create "type:requirement:non-functional"    --description "REQ-NF: Quality attributes and constraints" --color "5319E7"
gh label create "type:architecture:decision"         --description "ADR: Architecture decision record" --color "F9D0C4"
gh label create "type:architecture:component"        --description "ARC-C: Architecture component specification" --color "FBCA04"
gh label create "type:architecture:quality-scenario" --description "QA-SC: ATAM quality attribute scenario" --color "D4C5F9"
gh label create "type:test-case"                     --description "TEST: Verification and validation test case" --color "C5DEF5"
gh label create "type:test-plan"                     --description "TEST-PLAN: Test plan document" --color "BFD4F2"
gh label create "type:implementation"                --description "IMP: Implementation task" --color "0075CA"
gh label create "type:documentation"                 --description "DOC: Documentation task" --color "0075CA"
gh label create "type:housekeeping"                  --description "HOUSEKEEPING: Cleanup/refactoring task" --color "E4E669"
gh label create "type:epic"                          --description "EPIC: Epic grouping multiple issues" --color "3E4B9E"
gh label create "type:bug"                           --description "BUG: Defect or unexpected behavior" --color "B60205"
gh label create "type:probe"                         --description "PROBE: HIL hardware probe/fixture capture" --color "FF6F00"

# ── Canonical Phase Labels (phase:NN-name) ───────────────────────────────────
gh label create "phase:01-stakeholder-requirements"  --description "Phase 01: Stakeholder Requirements" --color "D93F0B"
gh label create "phase:02-requirements"              --description "Phase 02: Requirements Analysis" --color "E99695"
gh label create "phase:03-architecture"              --description "Phase 03: Architecture Design" --color "F9D0C4"
gh label create "phase:04-design"                    --description "Phase 04: Detailed Design" --color "FEF2C0"
gh label create "phase:05-implementation"            --description "Phase 05: Implementation" --color "BFD4F2"
gh label create "phase:06-integration"               --description "Phase 06: Integration" --color "C2E0C6"
gh label create "phase:07-verification-validation"   --description "Phase 07: Verification & Validation" --color "5319E7"
gh label create "phase:08-transition"                --description "Phase 08: Transition/Deployment" --color "1D76DB"
gh label create "phase:09-operation-maintenance"     --description "Phase 09: Operation & Maintenance" --color "0E8A16"

# ── Canonical Status Labels (status:*) ──────────────────────────────────────
gh label create "status:draft"      --description "Draft state - work in progress" --color "EDEDED"
gh label create "status:ready"      --description "Ready for implementation" --color "C2E0C6"
gh label create "status:blocked"    --description "Blocked - waiting on dependency" --color "B60205"
gh label create "status:in-review"  --description "Under review" --color "FBCA04"
gh label create "status:backlog"    --description "In backlog, not yet scheduled" --color "EDEDED"

# ── Canonical Priority Labels (priority:*) ──────────────────────────────────
gh label create "priority:p0" --description "P0: Critical priority - blocking" --color "B60205"
gh label create "priority:p1" --description "P1: High priority" --color "D93F0B"
gh label create "priority:p2" --description "P2: Medium priority" --color "FBCA04"
gh label create "priority:p3" --description "P3: Low priority" --color "0E8A16"

# ── Integrity Level Labels (IEEE 1012-2016) ──────────────────────────────────
gh label create "integrity-1" --description "Integrity Level 1: Highest criticality" --color "B60205"
gh label create "integrity-2" --description "Integrity Level 2: High criticality" --color "D93F0B"
gh label create "integrity-3" --description "Integrity Level 3: Medium criticality" --color "FBCA04"
gh label create "integrity-4" --description "Integrity Level 4: Low criticality" --color "0E8A16"

# ── Verification Method Labels ───────────────────────────────────────────────
gh label create "verify-inspection"   --description "Verification by inspection/review" --color "C5DEF5"
gh label create "verify-analysis"     --description "Verification by analysis" --color "BFD4F2"
gh label create "verify-demonstration" --description "Verification by demonstration" --color "5319E7"
gh label create "verify-test"         --description "Verification by testing" --color "1D76DB"

# ── Legacy labels (kept for classifier fallback only; not used in templates) ─
gh label create "stakeholder-requirement"   --description "[LEGACY] Use type:stakeholder-requirement" --color "DDDDDD"
gh label create "functional-requirement"    --description "[LEGACY] Use type:requirement:functional" --color "DDDDDD"
gh label create "non-functional-requirement" --description "[LEGACY] Use type:requirement:non-functional" --color "DDDDDD"
gh label create "architecture-decision"     --description "[LEGACY] Use type:architecture:decision" --color "DDDDDD"
gh label create "architecture-component"    --description "[LEGACY] Use type:architecture:component" --color "DDDDDD"
gh label create "quality-scenario"          --description "[LEGACY] Use type:architecture:quality-scenario" --color "DDDDDD"
gh label create "test-case"                 --description "[LEGACY] Use type:test-case" --color "DDDDDD"
gh label create "phase-01" --description "[LEGACY] Use phase:01-stakeholder-requirements" --color "DDDDDD"
gh label create "phase-02" --description "[LEGACY] Use phase:02-requirements" --color "DDDDDD"
gh label create "phase-03" --description "[LEGACY] Use phase:03-architecture" --color "DDDDDD"
gh label create "phase-04" --description "[LEGACY] Use phase:04-design" --color "DDDDDD"
gh label create "phase-05" --description "[LEGACY] Use phase:05-implementation" --color "DDDDDD"
gh label create "phase-06" --description "[LEGACY] Use phase:06-integration" --color "DDDDDD"
gh label create "phase-07" --description "[LEGACY] Use phase:07-verification-validation" --color "DDDDDD"
gh label create "phase-08" --description "[LEGACY] Use phase:08-transition" --color "DDDDDD"
gh label create "phase-09" --description "[LEGACY] Use phase:09-operation-maintenance" --color "DDDDDD"
gh label create "priority-critical" --description "[LEGACY] Use priority:p0" --color "DDDDDD"
gh label create "priority-high"     --description "[LEGACY] Use priority:p1" --color "DDDDDD"
gh label create "priority-medium"   --description "[LEGACY] Use priority:p2" --color "DDDDDD"
gh label create "priority-low"      --description "[LEGACY] Use priority:p3" --color "DDDDDD"
gh label create "status-draft"      --description "[LEGACY] Use status:draft" --color "DDDDDD"
gh label create "status-ready"      --description "[LEGACY] Use status:ready" --color "DDDDDD"
gh label create "status-blocked"    --description "[LEGACY] Use status:blocked" --color "DDDDDD"
gh label create "status-in-review"  --description "[LEGACY] Use status:in-review" --color "DDDDDD"

echo "✅ All labels created successfully!"
echo "ℹ️  Canonical: 14 type + 9 phase + 5 status + 4 priority labels"
echo "ℹ️  Legacy labels created as grey fallbacks for backward compatibility"
