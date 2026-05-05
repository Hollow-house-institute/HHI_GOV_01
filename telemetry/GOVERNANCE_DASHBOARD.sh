#!/data/data/com.termux/files/usr/bin/bash

LOG="telemetry/GOVERNANCE_LOG.jsonl"

TOTAL=$(wc -l < "$LOG")
ALLOWED=$(grep -c '"outcome":"ALLOW"' "$LOG")
DENIED=$(grep -c '"outcome":"DENY"' "$LOG")
ESCALATED=$(grep -c '"outcome":"ESCALATE"' "$LOG")
STOP_EVENTS=$(grep -c 'STOP_' "$LOG")

printf "\n=== GOVERNANCE DASHBOARD ===\n"
printf "Total Events: %s\n" "$TOTAL"
printf "Allowed: %s\n" "$ALLOWED"
printf "Denied: %s\n" "$DENIED"
printf "Escalated: %s\n" "$ESCALATED"
printf "STOP Events: %s\n" "$STOP_EVENTS"

if [ "$TOTAL" -gt 0 ]; then
  GSI=$(awk "BEGIN { printf \"%.2f\", ($ALLOWED/$TOTAL)*100 }")
  printf "Governance Stability Index (GSI): %s%%\n" "$GSI"
fi
