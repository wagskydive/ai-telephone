"""Outbound call loop based on initiative."""
from __future__ import annotations

import random
from typing import Callable, Iterable
import time
import logging

from .personalities import Personality


def select_personalities(
    personalities: Iterable[Personality],
    rand: Callable[[], float] = random.random,
) -> list[Personality]:
    """Return personalities chosen to place outbound calls."""
    selected = []
    for p in personalities:
        if not p.enabled:
            continue
        if rand() < p.initiative:
            selected.append(p)
    return selected


def run_outbound(
    personalities: Iterable[Personality],
    originate: Callable[[int], None],
    *,
    rand: Callable[[], float] = random.random,
    call_history: list[int] | None = None,
    history_size: int = 5,
) -> None:
    """Trigger calls for selected personalities respecting call history."""
    history = call_history if call_history is not None else []
    for p in select_personalities(personalities, rand):
        if p.extension in history:
            continue
        originate(p.extension)
        history.append(p.extension)
        if len(history) > history_size:
            del history[0]


def outbound_loop(
    personalities: Iterable[Personality],
    originate: Callable[[int], None],
    *,
    interval: float = 60.0,
    rand: Callable[[], float] = random.random,
    history_size: int = 5,
) -> None:
    """Periodically invoke :func:`run_outbound`."""
    logger = logging.getLogger(__name__)
    call_history: list[int] = []
    while True:
        try:
            run_outbound(
                personalities,
                originate,
                rand=rand,
                call_history=call_history,
                history_size=history_size,
            )
        except Exception:  # pragma: no cover - log errors
            logger.exception("outbound loop failed")
        time.sleep(interval)
