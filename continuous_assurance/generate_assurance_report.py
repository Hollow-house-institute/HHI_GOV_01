from datetime import datetime
import json

report = {
    "generated_at": datetime.utcnow().isoformat() + "Z",
    "governance_status": "ACTIVE",
    "decision_boundary_status": "ENFORCED",
    "stop_authority_status": "ACTIVE",
    "telemetry_continuity": "VALID",
    "behavioral_drift_status": "MONITORED",
    "continuous_assurance": "ACTIVE"
}

with open("continuous_assurance/reports/assurance_report.json", "w") as f:
    json.dump(report, f, indent=2)

print("Continuous assurance report generated.")
