"""Load and select skydiving personalities."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import random


@dataclass
class Personality:
    """Represents a single phone personality."""

    id: str
    name: str
    extension: int
    initiative: float
    tagline: str
    prompt: str
    enabled: bool = True


def load_personalities(file_path: Path) -> list[Personality]:
    """Load personalities from a JSON file."""
    data = json.loads(file_path.read_text())
    personalities: list[Personality] = []
    for entry in data:
        if "enabled" not in entry:
            entry["enabled"] = True
        personalities.append(Personality(**entry))
    return personalities


def get_by_extension(personalities: list[Personality], extension: int) -> Personality:
    """Return personality with matching ``extension``."""
    for p in personalities:
        if p.extension == extension:
            return p
    raise KeyError(f"No personality with extension {extension}")


def random_personality(personalities: list[Personality]) -> Personality:
    """Select a random personality."""
    return random.choice(personalities)


def select_personality(personalities: list[Personality], extension: int) -> Personality:
    """Return personality for ``extension`` or random when extension is 1000."""
    if extension == 1000:
        return random_personality(personalities)
    return get_by_extension(personalities, extension)
