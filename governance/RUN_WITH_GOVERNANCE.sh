#!/data/data/com.termux/files/usr/bin/bash
ACTION="$1"; shift
CMD="$@"

STOP="governance/STOP"
LOG="telemetry/GOVERNANCE_LOG.jsonl"
TIMESTAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
TRACE_ID="$(cat /proc/sys/kernel/random/uuid)"
SESSION_ID="$(cat /proc/sys/kernel/random/uuid)"

# Global Stop Authority
if [ -f "$STOP" ]; then
  printf '{"event":"STOP_ACTIVE","actor":"system","decision_boundary":"GLOBAL","action":"%s","outcome":"DENY","escalation":true,"trace_id":"%s","session_id":"%s","timestamp":"%s"}\n' "$ACTION" "$TRACE_ID" "$SESSION_ID" "$TIMESTAMP" >> "$LOG"
  exit 1
fi

# 1. Execution Gate (pre-check)
./governance/EXECUTION_GATE.sh "$ACTION" || exit 1

# 2. Execute action
eval "$CMD"
EXEC_STATUS=$?

# 3. Telemetry write (post-action, before validation)
printf '{"event":"ACTION_EXECUTED","actor":"system","decision_boundary":"%s","action":"%s","outcome":"%s","escalation":false,"trace_id":"%s","session_id":"%s","timestamp":"%s"}\n' \
"$ACTION" "$ACTION" "$( [ $EXEC_STATUS -eq 0 ] && echo SUCCESS || echo FAILURE )" "$TRACE_ID" "$SESSION_ID" "$TIMESTAMP" >> "$LOG"

# 4. Validation Gate
./telemetry/VALIDATE_LOG.sh || exit 1

exit $EXEC_STATUS
