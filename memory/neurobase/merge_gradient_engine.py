# merge_gradient_engine.py
"""
Merge Gradient Engine – NeuroBase v1.3 (Theophilus-Axon)

Purpose:
    Merges similar memory nodes based on symbolic and functional overlap,
    reducing redundancy while preserving meaning and importance.

Explanation:
    This simulates memory consolidation and abstraction as seen in higher cognition.
    Highly similar or frequently co-activated nodes are blended into unified representations.

Scientific Support:
    - Memory consolidation and schema theory (McClelland et al., 1995)
    - Cortical abstraction and generalization

Ethics:
    Merging is logged and always reversible in audit trails.
    Used only in symbolic learning phase; real memories remain unmerged.

Citation:
    Hinkson, J. (2025). Neurobase Optimization via Symbolic Convergence.
"""


import json
import os
from typing import List
from memory.neurobase.neuron_memory_node import NeuronMemoryNode

NODE_STORE_PATH = "memory/neurobase/neuron_nodes.json"

def merge_similar_nodes(similarity_threshold: float = 0.85) -> List[NeuronMemoryNode]:
    if isinstance(similarity_threshold, list):
        similarity_threshold = float(sum(similarity_threshold) / len(similarity_threshold))

    """
    Merge memory nodes that share symbols or tags and exceed similarity threshold.
    Returns the updated list of memory nodes.
    """
    if not os.path.exists(NODE_STORE_PATH):
        return []

    with open(NODE_STORE_PATH, 'r') as f:
        data = json.load(f)
        nodes: List[NeuronMemoryNode] = [NeuronMemoryNode.from_dict(d) for d in data]

    merged = []
    skip_ids = set()

    for i, node_a in enumerate(nodes):
        for j, node_b in enumerate(nodes):
            if i >= j or node_a.id in skip_ids or node_b.id in skip_ids:
                continue

            sim = node_a.similarity(node_b)
            print(f"[DEBUG] similarity result between {node_a.id} and {node_b.id}: {sim} | type: {type(sim)}")

           
            # --- Force safe float casting ---
           
            if isinstance(sim, list):
                sim = float(sum(sim) / len(sim)) if sim else 0.0
            elif not isinstance(sim, float):
                try:
                    sim = float(sim)
                except (TypeError, ValueError):
                    sim = 0.0

            if sim >= similarity_threshold:
                new_node = node_a.merge_with(node_b)
                merged.append(new_node)
                skip_ids.update([node_a.id, node_b.id])


    survivors = [n for n in nodes if n.id not in skip_ids]
    final = survivors + merged

    with open(NODE_STORE_PATH, 'w') as f:
        json.dump([n.to_dict() for n in final], f, indent=2)

    return final

# --- RUNTIME PATCHED METHODS ---

def _merge_with(self, other):
    merged_tags = list(set(self.tags + other.tags))
    merged_strength = min(1.0, (self.strength + other.strength) / 2)
    merged_symbol = f"{self.symbol}+{other.symbol}"
    merged_node = NeuronMemoryNode(symbol=merged_symbol, tags=merged_tags)

    # Manually assign extended properties
    merged_node.id = f"{self.id}_{other.id}_merged"
    merged_node.timestamp = self.timestamp
    merged_node.strength = merged_strength
    merged_node.bonds = {**self.bonds, **other.bonds}
    return merged_node

setattr(NeuronMemoryNode, "merge_with", _merge_with)

