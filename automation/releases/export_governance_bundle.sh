#!/data/data/com.termux/files/usr/bin/bash
TS=$(date -u +"%Y%m%d_%H%M%S")
mkdir -p runtime/exports
zip -r "runtime/exports/HHI_GOVERNANCE_EXPORT_${TS}.zip" runtime automation *.md *.json *.yml 2>/dev/null
sha256sum runtime/exports/*.zip > runtime/exports/EXPORT_CHECKSUMS.sha256
