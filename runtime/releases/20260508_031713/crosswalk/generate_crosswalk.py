import json

crosswalk={
    "Decision Boundary":["NIST AI RMF","ISO/IEC 42001","EU AI Act"],
    "Stop Authority":["ISO/IEC 42001","EU AI Act Article 14"],
    "Behavioral Drift":["NIST Govern","OECD AI Principles"],
    "Governance Telemetry":["Continuous Assurance","Audit Evidence"]
}

with open("runtime/crosswalk/runtime_crosswalk.json","w") as f:
    json.dump(crosswalk,f,indent=2)

print("runtime_crosswalk.json generated")
