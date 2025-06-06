# activation_path_resolver.py
"""
Activation Path Resolver – NeuroBase v1.3 (Theophilus-Axon)

Purpose:
    Resolves memory node activation pathways using weighted associative bonds.

Explanation:
    When a concept is triggered (e.g., "fire"), this module traces which related nodes should activate next,
    similar to how associative memory or symbolic cognition works in the human brain.

Scientific Support:
    - Hebbian theory: "cells that fire together wire together"
    - Connectionist models of memory

Ethics:
    Activation tracing is used only in sandboxed simulation or internally logged cognition.
    It is not used to infer behavior or external control.

Citation:
    Hinkson, J. (2025). Symbolic Merge Theory and Recursive Path Resolution in Artificial Minds.
"""

import json
import os
from typing import List, Dict
from memory.neurobase.neuron_memory_node import NeuronMemoryNode

BOND_FILE = "memory/neurobase/synapse_bond_map.json"


def resolve_memory_path(trigger_symbol: str, threshold: float = 0.1) -> List[NeuronMemoryNode]:
    """
    Given a symbolic trigger, resolve associated nodes via bond strengths above threshold.
    """
    if not os.path.exists(BOND_FILE):
        return []

    with open(BOND_FILE, 'r') as f:
        bond_map: Dict[str, Dict[str, float]] = json.load(f)

    activated_ids = [target for target, weight in bond_map.get(trigger_symbol, {}).items() if weight >= threshold]

    node_path = []
    for node_id in activated_ids:
        node = NeuronMemoryNode.load_by_id(node_id)
        if node:
            node_path.append(node)

    return node_path
