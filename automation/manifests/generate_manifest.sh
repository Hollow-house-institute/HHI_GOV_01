#!/data/data/com.termux/files/usr/bin/bash
find . -type f ! -path "./.git/*" | sort > runtime/snapshots/FILE_MANIFEST.txt
sha256sum $(find . -type f ! -path "./.git/*") > runtime/snapshots/CANONICAL_CHECKSUMS.sha256
date -u +"%Y-%m-%dT%H:%M:%SZ" > runtime/snapshots/LAST_INTEGRITY_RUN.txt
