import json
import time

print("HHI Governance Event Stream Active")

while True:
    with open("runtime/logs/governance_events.jsonl") as f:
        lines=f.readlines()

    if lines:
        latest=json.loads(lines[-1])
        print(json.dumps(latest,indent=2))

    time.sleep(10)
