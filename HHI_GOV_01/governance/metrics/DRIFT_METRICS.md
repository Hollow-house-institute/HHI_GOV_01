# HHI_GOV_01 — Drift Metrics (Operationalization)

Status: DRAFT (Builder)
Authority: HHI_GOV_01 (implementation support only)
Scope: Measurement templates for audit-defensible drift detection.

## Principles
- Metrics do not redefine governance; they measure execution behavior against defined boundaries.
- Metrics must be reproducible from evidence artifacts (logs, manifests, transcripts).
- Metrics must be computed without semantic interpretation unless explicitly governed.

## Metric Set (Core)

### M-01 Decision Boundary Breach Rate
Definition: Count of actions executed past a defined boundary without authorized handoff.
Evidence: execution logs, boundary markers, role handoff records.
Computation:
- Numerator: boundary breaches
- Denominator: total boundary events
TODO: define boundary marker format used in this repo.

### M-02 Stop Authority Invocation Latency
Definition: Time from trigger condition to stop invocation.
Evidence: incident timeline log, system event timestamps.
Computation: (stop_invoked_ts - trigger_detected_ts)
TODO: define trigger events and timestamp source of truth.

### M-03 Escalation Completion Rate
Definition: Escalations that reach an authorized decision endpoint.
Evidence: escalation tickets/threads, approval records, closure markers.
Computation: completed / initiated
TODO: define "initiated" and "completed" markers.

### M-04 Override Utilization Ratio
Definition: Frequency of overrides relative to eligible override opportunities.
Evidence: override events, eligible events list.
Computation: override_events / eligible_events
TODO: define eligibility criteria without inference.

### M-05 Confidence Reinforcement Exposure
Definition: Number of confirmations that increase reliance absent evidence linkage.
Evidence: transcripts with confirmations lacking citations/controls.
Computation: count of confirmation events lacking evidence anchors.
TODO: define evidence anchor format.

### M-06 Audit Evidence Completeness Score
Definition: Proportion of required evidence objects present per release/tag.
Evidence: lock manifest, checksums, evidence index.
Computation: present_required / total_required
TODO: map required evidence types to HHI_GOV_01 clauses.

## Output Format
All metric runs MUST produce:
- metrics_run.json (machine readable)
- metrics_run.md (human summary)
- sha256 checksums
