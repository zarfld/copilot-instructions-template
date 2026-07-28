# GitHub Repository Label Configuration Script (PowerShell with GitHub API)
# Purpose: Create all labels needed for GitHub Issues-based requirements tracking
# Standards: ISO/IEC/IEEE 29148:2018 (Requirements Engineering)
# Requires: GITHUB_TOKEN environment variable

$token = $env:GITHUB_TOKEN
if (-not $token) {
    Write-Host "ERROR: GITHUB_TOKEN environment variable not set" -ForegroundColor Red
    Write-Host "Please set with: `$env:GITHUB_TOKEN = 'your_token_here'" -ForegroundColor Yellow
    exit 1
}

$repo = "zarfld/copilot-instructions-template"  # Update if different
$apiUrl = "https://api.github.com/repos/$repo/labels"

$headers = @{
    "Authorization" = "Bearer $token"
    "Accept" = "application/vnd.github+json"
    "X-GitHub-Api-Version" = "2022-11-28"
}

# Define all labels
$labels = @(
    # ── Canonical Type Labels (type:*) ──────────────────────────────────────
    @{ name = "type:stakeholder-requirement";      description = "StR: Business context and stakeholder needs"; color = "0E8A16" }
    @{ name = "type:requirement:functional";        description = "REQ-F: Functional system requirements"; color = "1D76DB" }
    @{ name = "type:requirement:non-functional";    description = "REQ-NF: Quality attributes and constraints"; color = "5319E7" }
    @{ name = "type:architecture:decision";         description = "ADR: Architecture decision record"; color = "F9D0C4" }
    @{ name = "type:architecture:component";        description = "ARC-C: Architecture component specification"; color = "FBCA04" }
    @{ name = "type:architecture:quality-scenario"; description = "QA-SC: ATAM quality attribute scenario"; color = "D4C5F9" }
    @{ name = "type:test-case";                     description = "TEST: Verification and validation test case"; color = "C5DEF5" }
    @{ name = "type:test-plan";                     description = "TEST-PLAN: Test plan document"; color = "BFD4F2" }
    @{ name = "type:implementation";                description = "IMP: Implementation task"; color = "0075CA" }
    @{ name = "type:documentation";                 description = "DOC: Documentation task"; color = "0075CA" }
    @{ name = "type:housekeeping";                  description = "HOUSEKEEPING: Cleanup/refactoring task"; color = "E4E669" }
    @{ name = "type:epic";                          description = "EPIC: Epic grouping multiple issues"; color = "3E4B9E" }
    @{ name = "type:bug";                           description = "BUG: Defect or unexpected behavior"; color = "B60205" }
    @{ name = "type:probe";                         description = "PROBE: HIL hardware probe/fixture capture"; color = "FF6F00" }

    # ── Canonical Phase Labels (phase:NN-name) ───────────────────────────────
    @{ name = "phase:01-stakeholder-requirements";  description = "Phase 01: Stakeholder Requirements"; color = "D93F0B" }
    @{ name = "phase:02-requirements";              description = "Phase 02: Requirements Analysis"; color = "E99695" }
    @{ name = "phase:03-architecture";              description = "Phase 03: Architecture Design"; color = "F9D0C4" }
    @{ name = "phase:04-design";                    description = "Phase 04: Detailed Design"; color = "FEF2C0" }
    @{ name = "phase:05-implementation";            description = "Phase 05: Implementation"; color = "BFD4F2" }
    @{ name = "phase:06-integration";               description = "Phase 06: Integration"; color = "C2E0C6" }
    @{ name = "phase:07-verification-validation";   description = "Phase 07: Verification & Validation"; color = "5319E7" }
    @{ name = "phase:08-transition";                description = "Phase 08: Transition/Deployment"; color = "1D76DB" }
    @{ name = "phase:09-operation-maintenance";     description = "Phase 09: Operation & Maintenance"; color = "0E8A16" }

    # ── Canonical Status Labels (status:*) ───────────────────────────────────
    @{ name = "status:draft";     description = "Draft state - work in progress"; color = "EDEDED" }
    @{ name = "status:ready";     description = "Ready for implementation"; color = "C2E0C6" }
    @{ name = "status:blocked";   description = "Blocked - waiting on dependency"; color = "B60205" }
    @{ name = "status:in-review"; description = "Under review"; color = "FBCA04" }
    @{ name = "status:backlog";   description = "In backlog, not yet scheduled"; color = "EDEDED" }

    # ── Canonical Priority Labels (priority:*) ───────────────────────────────
    @{ name = "priority:p0"; description = "P0: Critical priority - blocking"; color = "B60205" }
    @{ name = "priority:p1"; description = "P1: High priority"; color = "D93F0B" }
    @{ name = "priority:p2"; description = "P2: Medium priority"; color = "FBCA04" }
    @{ name = "priority:p3"; description = "P3: Low priority"; color = "0E8A16" }

    # ── Integrity Level Labels (IEEE 1012-2016) ──────────────────────────────
    @{ name = "integrity-1"; description = "Integrity Level 1: Highest criticality"; color = "B60205" }
    @{ name = "integrity-2"; description = "Integrity Level 2: High criticality"; color = "D93F0B" }
    @{ name = "integrity-3"; description = "Integrity Level 3: Medium criticality"; color = "FBCA04" }
    @{ name = "integrity-4"; description = "Integrity Level 4: Low criticality"; color = "0E8A16" }

    # ── Verification Method Labels ───────────────────────────────────────────
    @{ name = "verify-inspection";    description = "Verification by inspection/review"; color = "C5DEF5" }
    @{ name = "verify-analysis";      description = "Verification by analysis"; color = "BFD4F2" }
    @{ name = "verify-demonstration"; description = "Verification by demonstration"; color = "5319E7" }
    @{ name = "verify-test";          description = "Verification by testing"; color = "1D76DB" }

    # ── Legacy labels (fallback only; not used in templates) ─────────────────
    @{ name = "stakeholder-requirement";    description = "[LEGACY] Use type:stakeholder-requirement"; color = "DDDDDD" }
    @{ name = "functional-requirement";     description = "[LEGACY] Use type:requirement:functional"; color = "DDDDDD" }
    @{ name = "non-functional-requirement"; description = "[LEGACY] Use type:requirement:non-functional"; color = "DDDDDD" }
    @{ name = "architecture-decision";      description = "[LEGACY] Use type:architecture:decision"; color = "DDDDDD" }
    @{ name = "architecture-component";     description = "[LEGACY] Use type:architecture:component"; color = "DDDDDD" }
    @{ name = "quality-scenario";           description = "[LEGACY] Use type:architecture:quality-scenario"; color = "DDDDDD" }
    @{ name = "test-case";                  description = "[LEGACY] Use type:test-case"; color = "DDDDDD" }
    @{ name = "phase-01"; description = "[LEGACY] Use phase:01-stakeholder-requirements"; color = "DDDDDD" }
    @{ name = "phase-02"; description = "[LEGACY] Use phase:02-requirements"; color = "DDDDDD" }
    @{ name = "phase-03"; description = "[LEGACY] Use phase:03-architecture"; color = "DDDDDD" }
    @{ name = "phase-04"; description = "[LEGACY] Use phase:04-design"; color = "DDDDDD" }
    @{ name = "phase-05"; description = "[LEGACY] Use phase:05-implementation"; color = "DDDDDD" }
    @{ name = "phase-06"; description = "[LEGACY] Use phase:06-integration"; color = "DDDDDD" }
    @{ name = "phase-07"; description = "[LEGACY] Use phase:07-verification-validation"; color = "DDDDDD" }
    @{ name = "phase-08"; description = "[LEGACY] Use phase:08-transition"; color = "DDDDDD" }
    @{ name = "phase-09"; description = "[LEGACY] Use phase:09-operation-maintenance"; color = "DDDDDD" }
    @{ name = "priority-critical"; description = "[LEGACY] Use priority:p0"; color = "DDDDDD" }
    @{ name = "priority-high";     description = "[LEGACY] Use priority:p1"; color = "DDDDDD" }
    @{ name = "priority-medium";   description = "[LEGACY] Use priority:p2"; color = "DDDDDD" }
    @{ name = "priority-low";      description = "[LEGACY] Use priority:p3"; color = "DDDDDD" }
    @{ name = "status-draft";      description = "[LEGACY] Use status:draft"; color = "DDDDDD" }
    @{ name = "status-ready";      description = "[LEGACY] Use status:ready"; color = "DDDDDD" }
    @{ name = "status-blocked";    description = "[LEGACY] Use status:blocked"; color = "DDDDDD" }
    @{ name = "status-in-review";  description = "[LEGACY] Use status:in-review"; color = "DDDDDD" }
)

$created = 0
$skipped = 0
$errors = 0

foreach ($label in $labels) {
    try {
        $body = $label | ConvertTo-Json
        $response = Invoke-RestMethod -Uri $apiUrl -Method Post -Headers $headers -Body $body -ContentType "application/json"
        Write-Host "[OK] Created label: $($label.name)" -ForegroundColor Green
        $created++
    }
    catch {
        if ($_.Exception.Response.StatusCode -eq 422) {
            Write-Host "[SKIP] Label already exists: $($label.name)" -ForegroundColor Yellow
            $skipped++
        }
        else {
            Write-Host "[ERROR] Failed to create label: $($label.name) - $($_.Exception.Message)" -ForegroundColor Red
            $errors++
        }
    }
}

Write-Host "`n=== Summary ===" -ForegroundColor Cyan
Write-Host "Created: $created labels" -ForegroundColor Green
Write-Host "Skipped: $skipped labels (already exist)" -ForegroundColor Yellow
Write-Host "Errors: $errors labels" -ForegroundColor Red
Write-Host "Total: $($labels.Count) labels defined" -ForegroundColor Cyan
