import json
from pathlib import Path

ARCHIVE = Path("runtime/event_archive/governance_events.jsonl")

def replay():
    if not ARCHIVE.exists():
        print("NO_GOVERNANCE_EVENTS_FOUND")
        return

    with ARCHIVE.open("r", encoding="utf-8") as f:
        for line in f:
            event = json.loads(line.strip())
            print("=" * 80)
            print(f"TIMESTAMP: {event['timestamp']}")
            print(f"ACTOR: {event['actor']}")
            print(f"ACTION: {event['action']}")
            print(f"OUTCOME: {event['outcome']}")
            print(f"DRIFT_SCORE: {event['behavioral_drift_score']}")
            print(f"ESCALATION: {event['escalation_level']}")
            print(f"STOP_AUTHORITY: {event['stop_authority']}")
            print(f"EVIDENCE_HASH: {event['evidence_hash']}")

if __name__ == "__main__":
    replay()
