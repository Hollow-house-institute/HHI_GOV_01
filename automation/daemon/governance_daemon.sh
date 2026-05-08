#!/data/data/com.termux/files/usr/bin/bash
while true; do
bash automation/manifests/generate_manifest.sh
echo "{\"timestamp\":\"$(date -u +"%Y-%m-%dT%H:%M:%SZ")\",\"event\":\"governance_runtime_heartbeat\",\"status\":\"operational\"}" >> runtime/logs/governance_telemetry.jsonl
sleep 300
done
