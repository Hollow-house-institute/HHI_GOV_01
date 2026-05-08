#!/data/data/com.termux/files/usr/bin/bash

cd ~/HHI/HHI_GOV_01

tmux new-session -d -s governance_runtime \
'gunicorn -w 2 -b 0.0.0.0:8000 runtime_api.governance_runtime_api:app'

echo "HHI_RUNTIME_ACTIVE"
