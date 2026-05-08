import json
from pathlib import Path

ARCHIVE = Path("runtime/event_archive/governance_events.jsonl")

def calculate_score():
    if not ARCHIVE.exists():
        print("GOVERNANCE_CONTINUITY_SCORE: 0")
        return

    total_events = 0
    escalation_events = 0
    stop_events = 0
    replayable_events = 0

    with ARCHIVE.open("r", encoding="utf-8") as f:
        for line in f:
            total_events += 1
            event = json.loads(line.strip())

            if event.get("escalation_level") != "NONE":
                escalation_events += 1

            if event.get("stop_authority") == "ACTIVE":
                stop_events += 1

            if event.get("evidence_hash"):
                replayable_events += 1

    continuity_score = round(
        (
            (replayable_events / max(total_events, 1)) * 60 +
            (1 - (stop_events / max(total_events, 1))) * 20 +
            (1 - (escalation_events / max(total_events, 1))) * 20
        ),
        2
    )

    report = {
        "total_events": total_events,
        "replayable_events": replayable_events,
        "escalation_events": escalation_events,
        "stop_events": stop_events,
        "governance_continuity_score": continuity_score
    }

    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    calculate_score()
