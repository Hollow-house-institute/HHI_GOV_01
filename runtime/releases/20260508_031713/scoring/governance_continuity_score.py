import json

score=100
events=0

with open("runtime/logs/governance_events.jsonl") as f:
    for line in f:
        events += 1

score=max(0,100-(events*0.1))

print({
    "governance_continuity_score": round(score,2),
    "events_observed": events,
    "continuity_status": "ACTIVE"
})
