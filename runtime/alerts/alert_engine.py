import json
from datetime import datetime

with open("runtime/logs/drift_status.json") as f:
    drift=json.load(f)

alert={
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "alert_status":"NORMAL"
}

if drift["behavioral_drift_status"] == "DRIFT_ESCALATED":
    alert["alert_status"]="ALERT_TRIGGERED"

with open("runtime/logs/alert_status.json","w") as out:
    json.dump(alert,out,indent=2)

print(json.dumps(alert,indent=2))
