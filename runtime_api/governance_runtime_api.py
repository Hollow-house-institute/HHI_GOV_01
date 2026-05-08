from flask import Flask, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/governance", methods=["GET"])
def governance():
    return jsonify({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "runtime_status": "ACTIVE",
        "decision_boundary": "ENFORCED",
        "stop_authority": "ACTIVE",
        "continuity_status": "ACTIVE",
        "audit_chain": "LOCKED",
        "telemetry_status": "ACTIVE"
    })

@app.route("/continuity", methods=["GET"])
def continuity():
    with open("runtime/logs/telemetry_aggregate.jsonl") as f:
        data=json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
