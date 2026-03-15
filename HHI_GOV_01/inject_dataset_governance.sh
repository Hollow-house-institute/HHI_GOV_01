#!/data/data/com.termux/files/usr/bin/bash

HEADER="$(cat DATASETS/Governance_Header.txt)"

for f in $(find . -type f \( -name "*.csv" -o -name "*.json" -o -name "*.txt" \)); do
  if ! grep -q "HHI_GOV_01" "$f"; then
    echo "$HEADER" | cat - "$f" > temp && mv temp "$f"
    echo "Injected governance header into $f"
  fi
done
