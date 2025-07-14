"""Utilities for computing call analytics."""
from __future__ import annotations

from pathlib import Path
import json
from collections import Counter


def compute_stats(memory_dir: Path) -> dict:
    """Return call statistics from ``memory_dir``.

    The directory should contain JSON files with lists of interaction
    entries. Each entry must include a ``caller_extension`` field.
    """
    totals = Counter()
    for file in memory_dir.glob("*.json"):
        try:
            data = json.loads(file.read_text())
        except Exception:
            continue
        totals[file.stem] = len(data)
    most_popular = totals.most_common(1)[0][0] if totals else ""
    return {"totals": dict(totals), "most_popular": most_popular}
