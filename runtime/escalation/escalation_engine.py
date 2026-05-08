import json
from datetime import datetime

THRESHOLD=5

with open("runtime/logs/governance_events.jsonl") as f:
    events=[json.loads(line) for line in f]

event_count=len(events)

status={
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "events_observed": event_count,
    "threshold": THRESHOLD,
    "escalation_status": "NORMAL"
}

if event_count >= THRESHOLD:
    status["escalation_status"]="ESCALATED"

with open("runtime/logs/escalation_status.json","w") as out:
    json.dump(status,out,indent=2)

print(json.dumps(status,indent=2))
