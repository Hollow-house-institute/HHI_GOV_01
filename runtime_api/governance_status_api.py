from flask import Flask, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/governance", methods=["GET"])
def governance_status():
    status = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "decision_boundary": "ENFORCED",
        "stop_authority": "ACTIVE",
        "behavioral_drift": "MONITORED",
        "telemetry_status": "ACTIVE",
        "continuous_assurance": "ACTIVE",
        "governance_continuity": "ACTIVE",
        "standards_alignment": [
            "NIST AI RMF",
            "ISO/IEC 42001",
            "EU AI Act",
            "OECD AI Principles",
            "CAISI"
        ]
    }
    return jsonify(status)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
