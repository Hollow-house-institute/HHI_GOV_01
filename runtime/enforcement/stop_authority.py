import os
import json
from datetime import datetime

STOP_FILE = "runtime/escalations/STOP_AUTHORITY_ACTIVE.json"

os.makedirs("runtime/escalations", exist_ok=True)

def activate_stop_authority(reason, severity):
    payload = {
        "stop_authority": True,
        "reason": reason,
        "severity": severity,
        "activated_at": datetime.utcnow().isoformat() + "Z"
    }

    with open(STOP_FILE, "w") as f:
        json.dump(payload, f, indent=2)

    return payload

def stop_authority_status():
    if not os.path.exists(STOP_FILE):
        return {
            "stop_authority": False
        }

    with open(STOP_FILE, "r") as f:
        return json.load(f)

def clear_stop_authority():
    if os.path.exists(STOP_FILE):
        os.remove(STOP_FILE)

    return {
        "stop_authority": False
    }
