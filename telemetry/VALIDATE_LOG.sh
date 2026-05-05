#!/data/data/com.termux/files/usr/bin/bash
LOG="telemetry/GOVERNANCE_LOG.jsonl"
REQUIRED=("event" "actor" "decision_boundary" "action" "outcome" "escalation" "trace_id" "session_id" "timestamp")
LAST_LINE="$(tail -n 1 "$LOG")"
TIMESTAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

missing=false
for field in "${REQUIRED[@]}"; do
  if ! echo "$LAST_LINE" | grep -q "\"$field\""; then
    missing=true
  fi
done

if [ "$missing" = true ]; then
  printf '{"event":"TELEMETRY_INVALID","actor":"system","decision_boundary":"LOG_VALIDATION","action":"VALIDATE","outcome":"DENY","escalation":true,"trace_id":"%s","session_id":"%s","timestamp":"%s"}\n' "$(cat /proc/sys/kernel/random/uuid)" "$(cat /proc/sys/kernel/random/uuid)" "$TIMESTAMP" >> "$LOG"
  touch governance/STOP
  exit 1
else
  printf '{"event":"TELEMETRY_VALID","actor":"system","decision_boundary":"LOG_VALIDATION","action":"VALIDATE","outcome":"ALLOW","escalation":false,"trace_id":"%s","session_id":"%s","timestamp":"%s"}\n' "$(cat /proc/sys/kernel/random/uuid)" "$(cat /proc/sys/kernel/random/uuid)" "$TIMESTAMP" >> "$LOG"
  exit 0
fi
