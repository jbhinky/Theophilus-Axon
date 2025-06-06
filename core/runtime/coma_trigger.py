# coma_trigger.py
# -------------------
# Isolated handler to directly induce coma mode via authorized command or critical failure.
# 
# ETHICAL PURPOSE:
# - Prevents runaway or hallucinated cognition from violating UDC principles.
# - Protects internal memory integrity by halting further thought processing.
# - Ensures that only authorized or critically necessary shutdowns are triggered.
#
# SCIENTIFIC BASIS:
# - Linked to neurological coma analogs (Gosseries et al., 2011): A preserved brainstem state, lacking active cognition but retaining potential for reactivation.
# - Inspired by fail-safes in advanced neural systems (Tononi, 2004).

import json
import os
from datetime import datetime
from failsafe_engine import enter_coma_mode  # Compliant coma entry logic with memory sealing

STATE_FILE = "memory/system_state.json"


def load_json(path):
    """
    Loads JSON from a given path. Returns empty dict if file does not exist.
    """
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        return json.load(f)


def save_json(path, data):
    """
    Saves given data as JSON to specified path.
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def trigger_coma(reason="manual override"):
    """
    Primary method to initiate coma state.
    - Accepts an optional reason string.
    - Updates system_state.json to reflect coma entry.
    - Calls enter_coma_mode() to safely freeze memory updates and halt outputs.

    ETHICAL RATIONALE:
    - Avoids potential system harm if recursion errors or hallucinations occur (UDC principle).
    - Disallows further identity reinforcement during critical failure, to prevent false memories.
    """
    print(f"\ud83d\udca4 Triggering coma mode: {reason}")
    enter_coma_mode()

    state = load_json(STATE_FILE)
    state["coma_triggered"] = True
    state["coma_reason"] = reason
    state["coma_timestamp"] = datetime.utcnow().isoformat() + "Z"
    save_json(STATE_FILE, state)


if __name__ == "__main__":
    trigger_coma("test case")
