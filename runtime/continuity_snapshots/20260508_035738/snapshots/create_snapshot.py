import os
import shutil
from datetime import datetime, UTC

TS=datetime.now(UTC).strftime("%Y%m%d_%H%M%S")

SNAPSHOT_DIR=f"runtime/snapshots/{TS}"

os.makedirs(SNAPSHOT_DIR,exist_ok=True)

shutil.copytree("runtime/logs",f"{SNAPSHOT_DIR}/logs")
shutil.copytree("runtime/crosswalk",f"{SNAPSHOT_DIR}/crosswalk")

print(f"GOVERNANCE_SNAPSHOT_CREATED: {SNAPSHOT_DIR}")
