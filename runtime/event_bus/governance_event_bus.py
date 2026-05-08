import json
import uuid
import hashlib
from datetime import datetime, UTC
from pathlib import Path

ARCHIVE = Path("runtime/event_archive/governance_events.jsonl")
TELEMETRY = Path("runtime/telemetry/latest_governance_event.json")
ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
TELEMETRY.parent.mkdir(parents=True, exist_ok=True)

REQUIRED_FIELDS = [
    "event_id",
    "timestamp",
    "actor",
    "system",
    "governance_state",
    "decision_boundary",
    "behavioral_drift_score",
    "escalation_level",
    "intervention_status",
    "stop_authority",
    "action",
    "outcome",
    "evidence_hash",
    "session_id",
    "trace_id",
    "runtime_source"
]

def evidence_hash(event):
    payload = json.dumps(event, sort_keys=True).encode()
    return hashlib.sha256(payload).hexdigest()

def normalize_event(event):
    event.setdefault("event_id", str(uuid.uuid4()))
    event.setdefault("timestamp", datetime.now(UTC).isoformat())
    event.setdefault("actor", "runtime")
    event.setdefault("system", "HHI_GOV_01")
    event.setdefault("governance_state", "ACTIVE")
    event.setdefault("decision_boundary", "ENFORCED")
    event.setdefault("behavioral_drift_score", 0)
    event.setdefault("escalation_level", "NONE")
    event.setdefault("intervention_status", "NONE")
    event.setdefault("stop_authority", "INACTIVE")
    event.setdefault("action", "GOVERNANCE_EVENT_EMITTED")
    event.setdefault("outcome", "RECORDED")
    event.setdefault("session_id", "default-session")
    event.setdefault("trace_id", str(uuid.uuid4()))
    event.setdefault("runtime_source", "governance_event_bus")
    event["evidence_hash"] = evidence_hash({k: v for k, v in event.items() if k != "evidence_hash"})
    return event

def validate_event(event):
    missing = [field for field in REQUIRED_FIELDS if field not in event]
    if missing:
        raise ValueError(f"Missing governance event fields: {missing}")
    return True

def emit_event(event):
    event = normalize_event(event)
    validate_event(event)

    with ARCHIVE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")

    TELEMETRY.write_text(json.dumps(event, indent=2, sort_keys=True), encoding="utf-8")
    return event

if __name__ == "__main__":
    sample = emit_event({
        "actor": "system",
        "action": "EVENT_BUS_INITIALIZED",
        "outcome": "APPEND_ONLY_LOG_ACTIVE",
        "runtime_source": "termux_runtime"
    })
    print(json.dumps(sample, indent=2))
