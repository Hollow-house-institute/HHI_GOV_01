#!/data/data/com.termux/files/usr/bin/bash

STOP="governance/STOP"
LOG="telemetry/GOVERNANCE_LOG.jsonl"
TIMESTAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
TRACE_ID="$(cat /proc/sys/kernel/random/uuid)"
SESSION_ID="$(cat /proc/sys/kernel/random/uuid)"

if [ ! -f "$STOP" ]; then
  printf '{"event":"STOP_NOT_PRESENT","actor":"system","decision_boundary":"STOP_RESOLUTION","action":"CHECK","outcome":"ALLOW","escalation":false,"trace_id":"%s","session_id":"%s","timestamp":"%s"}\n' "$TRACE_ID" "$SESSION_ID" "$TIMESTAMP" >> "$LOG"
  exit 0
fi

read -p "Acknowledge STOP condition and resolve? (yes/no): " CONFIRM

if [ "$CONFIRM" = "yes" ]; then
  rm -f "$STOP"
  printf '{"event":"STOP_RESOLVED","actor":"human_in_the_loop","decision_boundary":"STOP_RESOLUTION","action":"REMOVE_STOP","outcome":"ALLOW","escalation":false,"trace_id":"%s","session_id":"%s","timestamp":"%s"}\n' "$TRACE_ID" "$SESSION_ID" "$TIMESTAMP" >> "$LOG"
  exit 0
else
  printf '{"event":"STOP_PERSIST","actor":"human_in_the_loop","decision_boundary":"STOP_RESOLUTION","action":"DENY_RESOLUTION","outcome":"DENY","escalation":true,"trace_id":"%s","session_id":"%s","timestamp":"%s"}\n' "$TRACE_ID" "$SESSION_ID" "$TIMESTAMP" >> "$LOG"
  exit 1
fi
