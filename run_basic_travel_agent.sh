#!/usr/bin/env bash
#############################################################################
#Script Name: run_basic_travel_agent.sh
#Description: Script to run the basic travel agent using agent_builder.py
#Usage: ./run_basic_travel_agent.sh

#Author: Aparchyanta Aneja
#Email: aaneja1990@gmail.com
#############################################################################

set -euo pipefail

# Run `agent_builder.py` with PYTHONPATH set so `agents` is importable from project root.
SCRIPT_PATH="$(cd "$(dirname "$0")" && pwd)"

# The project folder was renamed to `basicTravelAgent` — use that path here.
export PYTHONPATH="$SCRIPT_PATH/basicTravelAgent:${PYTHONPATH:-}"

"$SCRIPT_PATH/.venv/bin/python" "$SCRIPT_PATH/basicTravelAgent/agent_builder.py"