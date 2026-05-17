import os
import json
from datetime import datetime

STATE_FILE = "runtime/escalations/escalation_state.json"

DEFAULT_STATE = {
    "total_violations": 0,
    "severity_counts": {
        "LEVEL_1": 0,
        "LEVEL_2": 0,
        "LEVEL_3": 0,
        "LEVEL_4": 0,
        "LEVEL_5": 0
    },
    "stop_authority_active": False,
    "last_updated": None
}

os.makedirs("runtime/escalations", exist_ok=True)

def load_state():
    if not os.path.exists(STATE_FILE):
        return DEFAULT_STATE.copy()

    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    state["last_updated"] = datetime.utcnow().isoformat() + "Z"

    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def update_escalation(severity):
    state = load_state()

    state["total_violations"] += 1

    if severity in state["severity_counts"]:
        state["severity_counts"][severity] += 1

    if severity == "LEVEL_5":
        state["stop_authority_active"] = True

    save_state(state)

    return state

if __name__ == "__main__":
    demo = update_escalation("LEVEL_4")
    print(json.dumps(demo, indent=2))
