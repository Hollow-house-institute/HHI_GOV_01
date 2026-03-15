# HHI_GOV_01 — Implementation Patterns (Audit-Safe)

Status: DRAFT (Builder)
Purpose: Provide reference execution patterns that reduce interpretation risk.
Constraint: No new governance claims. Patterns only operationalize already-defined controls.

## Pattern P-01: Evidence-First Execution
When: Any governance-relevant run.
Steps:
1) Create evidence folder for run (timestamped)
2) Store raw inputs (no rewrite)
3) Produce outputs
4) Generate checksums
5) Commit + tag only after Human Authority approval (if required)
Artifacts:
- governance/audit/<run_id>/
- checksums.txt
TODO: confirm exact repo evidence path conventions.

## Pattern P-02: Non-bypassable Stop Boundary
When: Human-in-the-loop or stop authority is required.
Implementation:
- Define STOP gate in workflow scripts
- Require explicit approval token/file presence
Artifacts:
- STOP_REQUIRED marker file
- approval manifest reference
TODO: define approved marker filename and location.

## Pattern P-03: Drift Event Capture Template
When: suspected drift occurs (behavioral or authority drift).
Implementation:
- Capture transcript/logs verbatim
- Attach environment + version metadata
- Record boundary expectations vs observed
Artifacts:
- drift_event.md
- raw_transcript.txt
- env.json
TODO: link to existing repo drift schema if present.

## Pattern P-04: Release Integrity Chain
When: publishing a locked artifact.
Implementation:
- Create CANONICAL_CHECKSUMS
- Create LOCK_MANIFEST
- Tag release
- Verify tag points to lock commit
Artifacts:
- governance/approval/*
- git tag: vX.Y.Z-governance-lock
