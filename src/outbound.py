"""Outbound call loop based on initiative."""
from __future__ import annotations

import random
from typing import Callable, Iterable

from .personalities import Personality


def select_personalities(personalities: Iterable[Personality], rand: Callable[[], float] = random.random) -> list[Personality]:
    """Return personalities chosen to place outbound calls."""
    return [p for p in personalities if rand() < p.initiative]


def run_outbound(personalities: Iterable[Personality], originate: Callable[[int], None], rand: Callable[[], float] = random.random) -> None:
    """Trigger calls for selected personalities."""
    for p in select_personalities(personalities, rand):
        originate(p.extension)
