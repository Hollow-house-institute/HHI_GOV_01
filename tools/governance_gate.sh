#!/usr/bin/env bash
set -e
[ -f authority/telemetry/governance_telemetry.jsonl ] || { echo "Missing telemetry"; exit 1; }
sha256sum README.md > CANONICAL_CHECKSUMS.sha256
