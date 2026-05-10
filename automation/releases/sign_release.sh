#!/data/data/com.termux/files/usr/bin/bash
TAG=$(git describe --tags --always)
git archive --format zip --output runtime/signatures/${TAG}.zip HEAD
sha256sum runtime/signatures/${TAG}.zip > runtime/signatures/${TAG}.sha256
