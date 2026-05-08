import json
from datetime import datetime

DRIFT_THRESHOLD=10

with open("runtime/logs/governance_events.jsonl") as f:
    events=[json.loads(line) for line in f]

drift_score=len(events)

status={
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "drift_score": drift_score,
    "drift_threshold": DRIFT_THRESHOLD,
    "behavioral_drift_status": "NORMAL"
}

if drift_score >= DRIFT_THRESHOLD:
    status["behavioral_drift_status"]="DRIFT_ESCALATED"

with open("runtime/logs/drift_status.json","w") as out:
    json.dump(status,out,indent=2)

print(json.dumps(status,indent=2))
