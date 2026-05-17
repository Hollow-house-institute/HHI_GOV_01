import os
import json
import hashlib

TELEMETRY_DIR = "runtime/telemetry/append_only"

def sha256_file(path):
    h = hashlib.sha256()

    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)

    return h.hexdigest()

def replay_validate():
    results = []

    for filename in sorted(os.listdir(TELEMETRY_DIR)):
        if not filename.endswith(".json"):
            continue

        path = os.path.join(TELEMETRY_DIR, filename)

        try:
            with open(path, "r") as f:
                data = json.load(f)

            recorded_hash = (
                data.get("evidence_hash", "")
                .replace("sha256:", "")
            )

            verification_copy = dict(data)
            verification_copy.pop("evidence_hash", None)

            regenerated_hash = hashlib.sha256(
                json.dumps(
                    verification_copy,
                    sort_keys=True
                ).encode()
            ).hexdigest()

            valid = recorded_hash == regenerated_hash

            results.append({
                "file": filename,
                "valid": valid,
                "recorded_hash": recorded_hash,
                "regenerated_hash": regenerated_hash
            })

        except Exception as e:
            results.append({
                "file": filename,
                "valid": False,
                "error": str(e)
            })

    return results

if __name__ == "__main__":
    validation = replay_validate()
    print(json.dumps(validation, indent=2))
