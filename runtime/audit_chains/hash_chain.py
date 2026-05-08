import hashlib
import json

prev_hash="ROOT"

with open("runtime/logs/governance_events.jsonl") as f, open("runtime/logs/immutable_audit_chain.jsonl","w") as out:
    for line in f:
        event=json.loads(line)
        payload=json.dumps(event,sort_keys=True)
        current_hash=hashlib.sha256((prev_hash+payload).encode()).hexdigest()

        chain_event={
            "timestamp": event["timestamp"],
            "event": event["event"],
            "previous_hash": prev_hash,
            "current_hash": current_hash
        }

        out.write(json.dumps(chain_event)+"\n")
        prev_hash=current_hash

print("Immutable governance audit chain generated")
