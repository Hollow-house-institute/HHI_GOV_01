import json
from datetime import datetime, UTC

payload={
    "timestamp": datetime.now(UTC).isoformat(),
    "webhook_event":"governance_status_update",
    "runtime_status":"ACTIVE",
    "continuity_status":"ACTIVE",
    "stop_authority":"ENFORCED"
}

with open("runtime/logs/webhook_dispatch.json","w") as out:
    json.dump(payload,out,indent=2)

print(json.dumps(payload,indent=2))
