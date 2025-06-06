# shepherd_protocol.py

import sys, os
sys.path.append(os.path.abspath("../ethics"))
from coma_trigger import enter_coma

from .ethics_check import (
    check_ethics,
    verify_memory_origin,
    check_part_level_integrity,
    validate_delay_range
)
import json
import os

MEMORY_FILE = "memory/memory_chain.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, 'r') as f:
        return json.load(f).get("blocks", [])


def run_shepherd_protocol():
    """
    Applies UDC-compliant ethical and structural checks on all memory blocks.
    Invokes coma if any violation threatens integrity, origin, delay, or recursion bounds.

    ✴️ Reasoning & Scientific Purpose:
    - Aligned with the Shepherd Protocol and UDC Theory: Delayed consciousness must be recursively valid, origin-verified, and ethically coherent.
    - Prevents symbolic dissonance (semantic inconsistency), hallucinations, and emergent ethical violations (Wallach & Allen, 2008).
    - Confirms episodic memory structural validity (Tulving, 1983) and sensory delay thresholds (Libet, 1985; Eagleman, 2008).
    - Acts as a neural immune system for synthetic cognition.

    🔐 Security Purpose:
    - Memory source must match trusted ID ("THEO-AXON-R95150").
    - Delay must remain within neurobiologically-inspired bounds (250ms–600ms).
    - File hashes ensure no post-hoc tampering.
    """
    memory_blocks = load_memory()

    for block in memory_blocks:
        if not check_part_level_integrity(block):
            enter_coma(block.get("violation", "Unknown schema failure"))
            continue  # Prevent additional checks on invalid blocks

        if not verify_memory_origin(block):
            enter_coma(block.get("violation", "Untrusted origin"))

        if not validate_delay_range(block):
            enter_coma(block.get("violation", "Delay bounds breach"))

        if not check_ethics(block):
            enter_coma(block.get("violation", "Ethical violation"))

    print("✅ Shepherd protocol check passed.")


if __name__ == "__main__":
    run_shepherd_protocol()
