#!/usr/bin/env bash
set -euo pipefail

echo "Running HHI governance checks..."

# Required governance files
REQUIRED_FILES=(
  "LOCK_MANIFEST.md"
  "CANONICAL_CHECKSUMS.txt"
  "HHI-GOV-01.md"
)

for file in "${REQUIRED_FILES[@]}"; do
  if [ ! -f "$file" ]; then
    echo "ERROR: Required governance file missing: $file"
    exit 1
  fi
done

echo "All required governance files present."
echo "Governance check passed."
