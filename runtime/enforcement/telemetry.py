import os
import json
import uuid
import hashlib
from datetime import datetime

BASE_DIR = "runtime/telemetry/append_only"

os.makedirs(BASE_DIR, exist_ok=True)

def sha256_data(data):
    return hashlib.sha256(
        json.dumps(data, sort_keys=True).encode()
    ).hexdigest()

def emit_governance_event(event):
    event["event_id"] = str(uuid.uuid4())
    event["timestamp"] = datetime.utcnow().isoformat() + "Z"

    payload_hash = sha256_data(event)
    event["evidence_hash"] = f"sha256:{payload_hash}"

    filename = (
        f'{event["timestamp"].replace(":","-")}_'
        f'{event["event_id"]}.json'
    )

    path = os.path.join(BASE_DIR, filename)

    with open(path, "a") as f:
        f.write(json.dumps(event, indent=2))
        f.write("\n")

    return event

if __name__ == "__main__":
    sample = {
        "actor": "system",
        "system": "hhi_runtime_enforcement_engine",
        "session_id": "demo-session",
        "trace_id": "demo-trace",
        "workspace": "standards_library",
        "decision_boundary": "LOCK_MANIFEST",
        "behavioral_drift_score": 0.0,
        "action": "ALLOW",
        "severity": "LEVEL_1",
        "escalation_level": "NONE",
        "intervention_status": "NOT_REQUIRED",
        "stop_authority": False,
        "outcome": "APPROVED",
        "runtime_source": "runtime_enforcement_engine"
    }

    result = emit_governance_event(sample)
    print(json.dumps(result, indent=2))
