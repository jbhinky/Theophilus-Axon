# memory_decay_engine.py
"""
Memory Decay Engine – NeuroBase v1.3 (Theophilus-Axon)

Purpose:
    Applies decay to neuron memory nodes over time if not reinforced.
    Mimics biological forgetting and dynamic memory fading.

Explanation:
    The strength of each memory node decays slightly unless reactivated.
    This prevents all memories from having equal weight, simulating attention.

Scientific Support:
    - Neuroscience of synaptic pruning and memory fading
    - Adaptive forgetting as a cognitive feature (not flaw)

Ethics:
    All decay operations happen locally and nondestructively.
    Nodes are faded, not erased — unless specifically pruned by protocol.

Citation:
    Hinkson, J. (2025). Neuro-Coding Architecture and the Theophilus-Axon Project.
    Also supported by work on biologically inspired forgetting (Nature Reviews Neuroscience).
"""

import json
import os
import time
from typing import List
from memory.neurobase.neuron_memory_node import NeuronMemoryNode


NODE_STORE_PATH = "memory/neurobase/neuron_nodes.json"
DECAY_RATE = 0.01  # default decay rate per run

class MemoryDecayEngine:
    def __init__(self):
        self.nodes: List[NeuronMemoryNode] = self.load_nodes()

    def load_nodes(self) -> List[NeuronMemoryNode]:
        if not os.path.exists(NODE_STORE_PATH):
            return []
        with open(NODE_STORE_PATH, 'r') as f:
            data = json.load(f)
            return [NeuronMemoryNode.from_dict(d) for d in data]

    def save_nodes(self):
        os.makedirs(os.path.dirname(NODE_STORE_PATH), exist_ok=True)
        with open(NODE_STORE_PATH, 'w') as f:
            json.dump([n.to_dict() for n in self.nodes], f, indent=2)

    def decay_all(self):
        """
        Apply decay to all loaded memory nodes.
        """
        for node in self.nodes:
            node.decay(rate=DECAY_RATE)
        self.save_nodes()

    def reinforce_node(self, node_id: str, amount: float = 0.1):
        """
        Strengthen a specific node when recalled or emotionally activated.
        """
        for node in self.nodes:
            if node.id == node_id:
                node.reinforce(amount=amount)
        self.save_nodes()


# --- External interface required for symbolic template ---
def apply_decay(node: NeuronMemoryNode):
    """
    Apply decay to a specific memory node directly (symbolic simulation mode).
    """
    node.decay(rate=DECAY_RATE)
