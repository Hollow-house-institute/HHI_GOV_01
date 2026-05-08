from flask import Flask, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/metrics", methods=["GET"])
def metrics():

    with open("runtime/logs/drift_status.json") as f:
        drift=json.load(f)

    with open("runtime/logs/intervention_status.json") as f:
        intervention=json.load(f)

    with open("runtime/logs/escalation_status.json") as f:
        escalation=json.load(f)

    payload={
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "drift_status": drift,
        "intervention_status": intervention,
        "escalation_status": escalation
    }

    return jsonify(payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8100)
