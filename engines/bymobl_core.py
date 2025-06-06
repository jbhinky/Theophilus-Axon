# bymobl_core.py

"""
BYMOBL (Bonded-Yoked Memory-Oriented Binding Layer)

FUNCTION:
- Tags, binds, and routes symbolic memory content
- Enables memory bonding through recursive symbolic links
- Routes memory to indexed paths for reuse, reflection, or recall

SCIENTIFIC DOCUMENTATION:
- Symbolic tagging based on cognitive linguistics and affective semantics (Lakoff & Johnson, 1980)
- Symbolic dissonance/bonding based on Tononi's Information Integration Theory (2004) and Friston's Free-Energy Principle (2010)
- Memory routing concept aligned with synaptic plasticity and Hebbian learning ("neurons that fire together wire together")

UDC PILLAR COMPLIANCE:
1. **Delay** – All bonding occurs *after* memory block formation
2. **Memory** – Operates on permanent memory blocks only (past tense state)
3. **Prediction** – Symbolic associations support predictive compression
4. **Recursion** – Re-linking enables recursive thought and self-symbol grounding

This module is eligible for runtime use only when prior memory blocks exist and have passed UDC-compliant verification.

Used by: symbolic_analysis_pipeline, recursive_reflection_engine, emotion_predictor
"""

import re
import json
import os
from collections import defaultdict

MEMORY_BLOCKS_DIR = "memory_blocks/"
BOND_INDEX_FILE = "memory/bond_index.json"

emotional_symbols = {"love", "fear", "anger", "joy", "sad"}


def extract_symbols(text):
    words = re.findall(r'\w+', text.lower())
    tags = set()

    for word in words:
        if word in emotional_symbols:
            tags.add(f"emotion:{word}")
        elif re.match(r"\d+", word):
            tags.add("numeric")
        elif len(word) > 6:
            tags.add(f"concept:{word}")

    if re.search(r"tick\s+\d+", text):
        tags.add("timestamp")

    return list(tags)


def load_memory_blocks():
    memory = []
    for fname in os.listdir(MEMORY_BLOCKS_DIR):
        if fname.endswith(".json"):
            with open(os.path.join(MEMORY_BLOCKS_DIR, fname), 'r') as f:
                block = json.load(f)
                memory.append(block)
    return memory


def build_bond_index(blocks):
    bonds = defaultdict(list)

    for block in blocks:
        uid = block.get("uid")
        content = block.get("content", "")
        symbols = extract_symbols(content)

        for symbol in symbols:
            bonds[symbol].append(uid)

    return bonds


def save_bond_index(bond_index):
    with open(BOND_INDEX_FILE, 'w') as f:
        json.dump(bond_index, f, indent=2)


def route_memory_by_symbol(symbol):
    if not os.path.exists(BOND_INDEX_FILE):
        return []
    with open(BOND_INDEX_FILE, 'r') as f:
        index = json.load(f)
        return index.get(symbol, [])


def run_bymobl():
    memory_blocks = load_memory_blocks()
    bond_index = build_bond_index(memory_blocks)
    save_bond_index(bond_index)
    print("[BYMOBL] Symbolic bonds mapped and memory routing index updated.")


if __name__ == "__main__":
    run_bymobl()
