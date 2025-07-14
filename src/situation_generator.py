"""Generate call situations using remote LLM server."""
from __future__ import annotations

from typing import List
import requests


def generate_situation(server_url: str, character_id: str, memory_snippets: List[str], personality_prompt: str) -> str:
    """Request a situation from the LLM server.

    Parameters
    ----------
    server_url:
        Base URL of the LLM server.
    character_id:
        Identifier for the personality.
    memory_snippets:
        Recent memory snippets for context.
    personality_prompt:
        The personality's base prompt text.
    """
    payload = {
        "character_id": character_id,
        "memory_snippets": memory_snippets,
        "personality_prompt": personality_prompt,
    }
    response = requests.post(f"{server_url}/generate-situation", json=payload)
    response.raise_for_status()
    data = response.json()
    return data.get("situation", "")
