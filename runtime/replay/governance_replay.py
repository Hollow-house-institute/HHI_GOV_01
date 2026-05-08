import json

with open("runtime/logs/governance_events.jsonl") as f:
    for line in f:
        event=json.loads(line)
        print(f"[{event['timestamp']}] {event['event']} -> {event['outcome']}")
