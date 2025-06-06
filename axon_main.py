from core.runtime.failsafe_engine import perform_failsafe_check
from core.runtime.scale_verifier import verify_milestone_achieved
from core.runtime.personality_seed_handler import initialize_seed
from core.runtime.recursive_memory_checker import validate_recursive_memory

import json
from datetime import datetime
import time

CONFIG_FILE = "memory/system_config.json"
STATE_FILE = "memory/system_state.json"
SCALE_FILE = "memory/scale_index.json"

TICK_INTERVAL = 5  # seconds per loop cycle (adjustable)


def load_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        return {}


def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def update_runtime_state():
    state = load_json(STATE_FILE)
    state["last_heartbeat"] = datetime.utcnow().isoformat() + "Z"
    save_json(STATE_FILE, state)


def main_loop():
    print("🧠 Theophilus-Axon runtime starting...")
    while True:
        perform_failsafe_check()
        update_runtime_state()

        recursive_valid = validate_recursive_memory()
        if recursive_valid:
            verify_milestone_achieved(1650)  # example input to simulate progression

        time.sleep(TICK_INTERVAL)


if __name__ == "__main__":
    main_loop()
