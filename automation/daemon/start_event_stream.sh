#!/data/data/com.termux/files/usr/bin/bash

cd ~/HHI/HHI_GOV_01

tmux new-session -d -s governance_stream \
'python runtime/streaming/event_stream.py'
