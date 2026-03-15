#!/usr/bin/env bash
set -euo pipefail

OUT="HHI_GOV_01_AUDIT_PACK_$(date +%Y%m%d).zip"

zip -r "$OUT" \
  HHI-GOV-01.md \
  glossary.json \
  glossary.md \
  governance/approval/LOCK_MANIFEST.json \
  governance/approval/CANONICAL_CHECKSUMS_*.txt \
  governance/compliance/COMPLIANCE_MATRIX.csv \
  governance/compliance/ISO_CROSSWALK.csv \
  governance/compliance/NIST_CROSSWALK.csv \
  governance/metrics \
  governance/audit || true

sha256sum "$OUT" > "$OUT.sha256"

echo "Built $OUT"
