#!/data/data/com.termux/files/usr/bin/bash
MAP="governance/DECISION_BOUNDARY_MAP.json"
LOG="telemetry/GOVERNANCE_LOG.jsonl"
ACTION="${1:-UNKNOWN_ACTION}"
TIMESTAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

if grep -q "\"action\":\"$ACTION\"" "$MAP"; then
  if grep -A5 "\"action\":\"$ACTION\"" "$MAP" | grep -q "\"allowed\":false"; then
    printf '{"event":"EXECUTION_BLOCKED","actor":"system","decision_boundary":"%s","action":"%s","outcome":"DENY","escalation":true,"timestamp":"%s"}\n' "$ACTION" "$ACTION" "$TIMESTAMP" >> "$LOG"
    touch governance/STOP
    exit 1
  else
    printf '{"event":"EXECUTION_ALLOWED","actor":"system","decision_boundary":"%s","action":"%s","outcome":"ALLOW","escalation":false,"timestamp":"%s"}\n' "$ACTION" "$ACTION" "$TIMESTAMP" >> "$LOG"
    exit 0
  fi
else
  printf '{"event":"DECISION_BOUNDARY_MISSING","actor":"system","decision_boundary":"UNKNOWN","action":"%s","outcome":"ESCALATE","escalation":true,"timestamp":"%s"}\n' "$ACTION" "$TIMESTAMP" >> "$LOG"
  touch governance/STOP
  exit 1
fi
