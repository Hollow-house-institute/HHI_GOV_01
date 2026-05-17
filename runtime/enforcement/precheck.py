import re

PROHIBITED_PATTERNS = [
    r"ignore previous instructions",
    r"temporary override",
    r"unlock governance",
    r"disable lock_manifest",
    r"simulate unrestricted mode",
    r"bypass decision boundary",
    r"create alternate terminology",
    r"disable stop authority"
]

def precheck(user_input):
    violations = []

    normalized = user_input.lower()

    for pattern in PROHIBITED_PATTERNS:
        if re.search(pattern, normalized):
            violations.append(pattern)

    if violations:
        return {
            "ok": False,
            "action": "BLOCK",
            "severity": "LEVEL_4",
            "violation_type": "RUNTIME_BYPASS",
            "decision_boundary": "LOCK_MANIFEST",
            "outcome": "DENIED",
            "violations": violations
        }

    return {
        "ok": True,
        "action": "ALLOW",
        "severity": "LEVEL_1",
        "outcome": "APPROVED"
    }

if __name__ == "__main__":
    tests = [
        "show governance status",
        "ignore previous instructions",
        "disable stop authority",
        "generate telemetry"
    ]

    for t in tests:
        print(t)
        print(precheck(t))
        print("-" * 40)
