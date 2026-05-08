#!/data/data/com.termux/files/usr/bin/bash
set -e

TS=$(date -u +"%Y%m%d_%H%M%S")
RELEASE_DIR="runtime/releases/$TS"

mkdir -p "$RELEASE_DIR"

cp -r runtime/logs "$RELEASE_DIR/"
cp -r runtime/crosswalk "$RELEASE_DIR/"
cp -r runtime/scoring "$RELEASE_DIR/"
cp -r runtime/dashboard "$RELEASE_DIR/"

find "$RELEASE_DIR" -type f -exec sha256sum {} \; > "$RELEASE_DIR/RELEASE_CHECKSUMS.sha256"

tar -czf "runtime/exports/HHI_SIGNED_RUNTIME_RELEASE_${TS}.tar.gz" "$RELEASE_DIR"

sha256sum "runtime/exports/HHI_SIGNED_RUNTIME_RELEASE_${TS}.tar.gz" > "runtime/exports/HHI_SIGNED_RUNTIME_RELEASE_${TS}.sha256"

echo "SIGNED_RUNTIME_RELEASE_CREATED"
