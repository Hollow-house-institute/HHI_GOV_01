#!/data/data/com.termux/files/usr/bin/bash

LOG="telemetry/GOVERNANCE_LOG.jsonl"
STOP="governance/STOP"
TIMESTAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
TRACE_ID="$(cat /proc/sys/kernel/random/uuid)"
SESSION_ID="$(cat /proc/sys/kernel/random/uuid)"

TOTAL=$(wc -l < "$LOG")
ALLOWED=$(grep -c '"outcome":"ALLOW"' "$LOG")

if [ "$TOTAL" -eq 0 ]; then
  exit 0
fi

GSI=$(awk "BEGIN { printf \"%.2f\", ($ALLOWED/$TOTAL)*100 }")

THRESHOLD=80

if (( $(echo "$GSI < $THRESHOLD" | bc -l) )); then
  printf '{"event":"GSI_THRESHOLD_BREACH","actor":"system","decision_boundary":"THRESHOLD_ENFORCEMENT","action":"EVALUATE_GSI","outcome":"DENY","escalation":true,"trace_id":"%s","session_id":"%s","timestamp":"%s"}\n' "$TRACE_ID" "$SESSION_ID" "$TIMESTAMP" >> "$LOG"
  touch "$STOP"
  exit 1
else
  printf '{"event":"GSI_WITHIN_THRESHOLD","actor":"system","decision_boundary":"THRESHOLD_ENFORCEMENT","action":"EVALUATE_GSI","outcome":"ALLOW","escalation":false,"trace_id":"%s","session_id":"%s","timestamp":"%s"}\n' "$TRACE_ID" "$SESSION_ID" "$TIMESTAMP" >> "$LOG"
  exit 0
fi
