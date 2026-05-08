from flask import Flask, jsonify
from pathlib import Path
import json

app = Flask(__name__)

EVENTS = Path("runtime/event_archive/governance_events.jsonl")
LATEST = Path("runtime/telemetry/latest_governance_event.json")

def load_events(limit=25):
    if not EVENTS.exists():
        return []

    with EVENTS.open("r", encoding="utf-8") as f:
        lines = f.readlines()[-limit:]

    return [json.loads(line.strip()) for line in lines]

@app.route("/governance/health")
def health():
    return jsonify({
        "runtime": "ACTIVE",
        "telemetry": "ACTIVE",
        "replay": "ACTIVE",
        "continuous_assurance": "ACTIVE"
    })

@app.route("/governance/status")
def status():
    if not LATEST.exists():
        return jsonify({"status": "NO_TELEMETRY"})

    return jsonify(json.loads(LATEST.read_text()))

@app.route("/governance/events")
def events():
    return jsonify(load_events())

@app.route("/governance/replay")
def replay():
    return jsonify(load_events(limit=100))

@app.route("/governance/continuity")
def continuity():
    from continuous_assurance.governance_continuity_score import calculate_score
    return jsonify({"continuity_engine": "AVAILABLE"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
