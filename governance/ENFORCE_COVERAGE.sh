#!/data/data/com.termux/files/usr/bin/bash

LOG="telemetry/GOVERNANCE_LOG.jsonl"
STOP="governance/STOP"
TIMESTAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
TRACE_ID="$(cat /proc/sys/kernel/random/uuid)"
SESSION_ID="$(cat /proc/sys/kernel/random/uuid)"

if [ -z "$GOVERNANCE_ACTIVE" ]; then
  printf '{"event":"GOVERNANCE_BYPASS_DETECTED","actor":"system","decision_boundary":"ENTRY_POINT","action":"DIRECT_EXECUTION","outcome":"DENY","escalation":true,"trace_id":"%s","session_id":"%s","timestamp":"%s"}\n' "$TRACE_ID" "$SESSION_ID" "$TIMESTAMP" >> "$LOG"
  touch "$STOP"
  exit 1
else
  printf '{"event":"GOVERNANCE_ENFORCED","actor":"system","decision_boundary":"ENTRY_POINT","action":"RUNNER_EXECUTION","outcome":"ALLOW","escalation":false,"trace_id":"%s","session_id":"%s","timestamp":"%s"}\n' "$TRACE_ID" "$SESSION_ID" "$TIMESTAMP" >> "$LOG"
  exit 0
fi
