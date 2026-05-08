#!/data/data/com.termux/files/usr/bin/bash

TS=$(date -u +"%Y%m%d_%H%M%S")

BUNDLE="runtime/bundles/HHI_ENTERPRISE_BUNDLE_${TS}"

mkdir -p "$BUNDLE"

cp -r runtime/logs "$BUNDLE/"
cp -r runtime/crosswalk "$BUNDLE/"
cp -r runtime/analytics "$BUNDLE/"
cp -r runtime/scoring "$BUNDLE/"
cp -r runtime/escalation "$BUNDLE/"
cp -r runtime/intervention "$BUNDLE/"

find "$BUNDLE" -type f -exec sha256sum {} \; > "$BUNDLE/BUNDLE_CHECKSUMS.sha256"

tar -czf "${BUNDLE}.tar.gz" "$BUNDLE"

echo "ENTERPRISE_BUNDLE_CREATED"
