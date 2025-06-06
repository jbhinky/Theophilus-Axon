# verify_manifest_integrity.py

import hashlib
import json
import os
from core.runtime.coma_trigger import enter_coma

MANIFEST_FILE = "spark_manifest.json"


def hash_line(line):
    return hashlib.sha256(line.strip().encode("utf-8")).hexdigest()


def verify_line_hash(filepath, expected_hashes):
    if not os.path.exists(filepath):
        enter_coma(f"Missing spark file: {filepath}")

    with open(filepath, 'r') as f:
        for i, line in enumerate(f):
            actual_hash = hash_line(line)
            expected_hash = expected_hashes[i] if i < len(expected_hashes) else None
            if actual_hash != expected_hash:
                enter_coma(f"Spark file tampering detected in {filepath} at line {i+1}.")


def verify_manifest():
    if not os.path.exists(MANIFEST_FILE):
        enter_coma("Missing spark manifest file")

    with open(MANIFEST_FILE, 'r') as f:
        manifest = json.load(f)

    for filepath, line_hashes in manifest.items():
        verify_line_hash(filepath, line_hashes)

    print("✅ Spark integrity verified.")


if __name__ == "__main__":
    verify_manifest()
