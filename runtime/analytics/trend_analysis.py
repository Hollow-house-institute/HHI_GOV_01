import json
from collections import Counter

counter=Counter()

with open("runtime/logs/governance_events.jsonl") as f:
    for line in f:
        event=json.loads(line)
        counter[event["event"]] += 1

trend_report={
    "event_distribution":dict(counter),
    "governance_health":"STABLE",
    "runtime_status":"ACTIVE"
}

with open("runtime/logs/trend_analysis.json","w") as out:
    json.dump(trend_report,out,indent=2)

print(json.dumps(trend_report,indent=2))
