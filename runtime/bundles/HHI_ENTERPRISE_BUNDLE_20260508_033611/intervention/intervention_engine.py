import json
from datetime import datetime

with open("runtime/logs/drift_status.json") as f:
    drift=json.load(f)

status={
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "intervention_required": False,
    "stop_authority": "ACTIVE"
}

if drift["behavioral_drift_status"] == "DRIFT_ESCALATED":
    status["intervention_required"]=True

with open("runtime/logs/intervention_status.json","w") as out:
    json.dump(status,out,indent=2)

print(json.dumps(status,indent=2))
