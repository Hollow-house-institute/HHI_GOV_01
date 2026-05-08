#!/data/data/com.termux/files/usr/bin/bash

cd ~/HHI/HHI_GOV_01/runtime/ui

tmux new-session -d -s governance_dashboard \
'python -m http.server 8080'
