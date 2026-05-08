#!/data/data/com.termux/files/usr/bin/bash

mkdir -p export_bundle

cp -r telemetry export_bundle/
cp -r schemas export_bundle/
cp -r continuous_assurance export_bundle/

find export_bundle -type f -exec sha256sum {} \; > export_bundle/CHECKSUMS.sha256

echo "Governance export bundle generated."
