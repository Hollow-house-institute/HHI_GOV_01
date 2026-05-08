import json
from collections import Counter

counter=Counter()

with open("runtime/logs/governance_events.jsonl") as f:
    for line in f:
        event=json.loads(line)
        counter[event["event"]] += 1

summary={
    "event_totals":dict(counter),
    "continuity_status":"ACTIVE"
}

with open("runtime/logs/telemetry_aggregate.jsonl","w") as out:
    out.write(json.dumps(summary,indent=2))

print(json.dumps(summary,indent=2))
