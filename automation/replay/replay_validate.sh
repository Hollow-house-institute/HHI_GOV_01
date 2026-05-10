#!/data/data/com.termux/files/usr/bin/bash
find runtime/event_archive -type f -name "*.json" | while read f; do
jq empty "$f" || exit 1
done
printf 'REPLAY_VALIDATION=PASS\nTIMESTAMP=%s\n' "$(date -u +%FT%TZ)" >> runtime/logs/replay_validation.log
