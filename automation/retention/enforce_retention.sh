#!/data/data/com.termux/files/usr/bin/bash
find runtime/logs -type f -mtime +30 -delete
find runtime/snapshots -type f -mtime +60 -delete
find runtime/exports -type f -mtime +90 -delete
printf 'RETENTION_PRUNE=%s\n' "$(date -u +%FT%TZ)" >> runtime/logs/retention.log
