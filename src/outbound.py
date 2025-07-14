"""Outbound call loop based on initiative."""
from __future__ import annotations

import random
from typing import Callable, Iterable
import time
import logging

from .personalities import Personality


def select_personalities(personalities: Iterable[Personality], rand: Callable[[], float] = random.random) -> list[Personality]:
    """Return personalities chosen to place outbound calls."""
    return [p for p in personalities if rand() < p.initiative]


def run_outbound(personalities: Iterable[Personality], originate: Callable[[int], None], rand: Callable[[], float] = random.random) -> None:
    """Trigger calls for selected personalities."""
    for p in select_personalities(personalities, rand):
        originate(p.extension)


def outbound_loop(
    personalities: Iterable[Personality],
    originate: Callable[[int], None],
    *,
    interval: float = 60.0,
    rand: Callable[[], float] = random.random,
) -> None:
    """Periodically invoke :func:`run_outbound`."""
    logger = logging.getLogger(__name__)
    while True:
        try:
            run_outbound(personalities, originate, rand=rand)
        except Exception:  # pragma: no cover - log errors
            logger.exception("outbound loop failed")
        time.sleep(interval)
