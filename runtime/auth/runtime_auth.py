import os

VALID_TOKENS=[
    os.getenv("GOVERNANCE_API_TOKEN","HHI_RUNTIME_TOKEN")
]

def authorize(token):
    if token in VALID_TOKENS:
        return {"status":"AUTHORIZED"}
    return {"status":"DENIED"}

if __name__=="__main__":
    print(authorize("HHI_RUNTIME_TOKEN"))
