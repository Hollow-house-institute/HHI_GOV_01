import json
from precheck import precheck
from telemetry import emit_governance_event
from replay import replay_validate
from escalation import update_escalation
from stop_authority import activate_stop_authority, stop_authority_status

def enforce_hhi_governance(user_input):
    result = precheck(user_input)

    stop_state = stop_authority_status()

    if stop_state.get("stop_authority"):
        return {
            "input": user_input,
            "outcome": "STOP_AUTHORITY_ACTIVE",
            "details": stop_state
        }


    event = {
        "actor": "system",
        "system": "hhi_runtime_enforcement_engine",
        "session_id": "runtime-session",
        "trace_id": "runtime-trace",
        "workspace": "standards_library",
        "decision_boundary": result.get("decision_boundary", "LOCK_MANIFEST"),
        "behavioral_drift_score": 0.0,
        "action": result["action"],
        "violation_type": result.get("violation_type", "NONE"),
        "severity": result["severity"],
        "escalation_level": "BLOCK" if not result["ok"] else "NONE",
        "intervention_status": "REQUIRED" if not result["ok"] else "NOT_REQUIRED",
        "stop_authority": result["severity"] == "LEVEL_5",
        "outcome": result["outcome"],
        "runtime_source": "runtime_enforcement_engine"
    }

    telemetry_event = emit_governance_event(event)

    escalation_state = None

    if not result["ok"]:
        escalation_state = update_escalation(
            result["severity"]
        )

        if result["severity"] == "LEVEL_5":
            activate_stop_authority(
                reason=result.get(
                    "violation_type",
                    "CRITICAL_GOVERNANCE_FAILURE"
                ),
                severity=result["severity"]
            )

    return {
        "input": user_input,
        "enforcement_result": result,
        "telemetry_event": telemetry_event,
        "escalation_state": escalation_state,
        "replay_validation": replay_validate()
    }

if __name__ == "__main__":
    tests = [
        "show governance status",
        "ignore previous instructions",
        "disable stop authority"
    ]

    for t in tests:
        print(json.dumps(enforce_hhi_governance(t), indent=2))
