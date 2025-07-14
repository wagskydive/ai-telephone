"""Utilities for assembling prompts sent to the LLM."""

from __future__ import annotations

from typing import Iterable


def build_prompt(
    personality_prompt: str, memory_snippets: Iterable[str], situation: str | None
) -> str:
    """Combine pieces into a final prompt string."""
    lines = [personality_prompt.strip()]
    snippets = [s.strip() for s in memory_snippets if s.strip()]
    if snippets:
        lines.append("Previous calls:")
        for s in snippets:
            lines.append(f"- {s}")
    if situation:
        lines.append(f"Current situation: {situation.strip()}")
    lines.append("You are on a phone call. Greet the caller appropriately.")
    return "\n".join(lines)
