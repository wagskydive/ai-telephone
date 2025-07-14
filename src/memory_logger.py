"""Utility for writing call interaction logs."""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict
import re


def guess_name(text: str) -> str:
    """Return a simple best-guess name from ``text``."""
    patterns = [
        r"my name is ([A-Za-z']+)",
        r"i'?m ([A-Za-z']+)",
        r"this is ([A-Za-z']+)",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            return m.group(1).capitalize()
    return ""

def log_interaction(
    memory_dir: Path,
    personality_id: str,
    *,
    caller_extension: str,
    summary: str,
    name_guess: str,
    quotes: List[str],
    max_entries: int | None = None,
    ) -> None:
    """Append an interaction entry for the given personality.

    When ``max_entries`` is provided, only the most recent entries up to that
    limit are retained on disk.
    """
    memory_dir.mkdir(parents=True, exist_ok=True)
    file_path = memory_dir / f"{personality_id}.json"
    if file_path.exists():
        data: List[Dict] = json.loads(file_path.read_text())
    else:
        data = []
    if not name_guess:
        name_guess = guess_name(" ".join([summary] + quotes))

    data.append(
        {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "caller_extension": caller_extension,
            "name_guess": name_guess,
            "summary": summary,
            "quotes": quotes,
        }
    )
    if max_entries is not None and len(data) > max_entries:
        data = data[-max_entries:]
    file_path.write_text(json.dumps(data, indent=2))


def load_memory(memory_dir: Path, personality_id: str) -> List[Dict]:
    """Return saved memory entries for ``personality_id``."""
    file_path = memory_dir / f"{personality_id}.json"
    if file_path.exists():
        return json.loads(file_path.read_text())
    return []


def summarize_memory(entries: List[Dict], *, limit: int = 3) -> str:
    """Return a short summary string from the last ``limit`` entries."""
    recent = entries[-limit:]
    parts = [e.get("summary", "") for e in recent if e.get("summary")]
    return "; ".join(parts).strip()
