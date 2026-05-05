#!/data/data/com.termux/files/usr/bin/bash

OUT="audit_bundle_$(date -u +%Y%m%dT%H%M%SZ)"
mkdir -p "$OUT"

cp governance/*.sh "$OUT"/ 2>/dev/null
cp governance/*.json "$OUT"/ 2>/dev/null
cp telemetry/GOVERNANCE_LOG.jsonl "$OUT"/ 2>/dev/null

find "$OUT" -type f -exec sha256sum {} \; > "$OUT/manifest.sha256"

if command -v zip >/dev/null 2>&1; then
  zip -r "$OUT.zip" "$OUT" >/dev/null
  rm -rf "$OUT"
fi

echo "Audit bundle created: $OUT.zip"
