"""Core handler for AI phone calls."""

from __future__ import annotations

from pathlib import Path
import requests
import logging

from .audio_player import play_wav
from .vad_recorder import record_until_silence
from .memory_logger import log_interaction, load_memory
from .situation_generator import generate_situation
from .prompt_builder import build_prompt

logger = logging.getLogger(__name__)


def handle_call(
    temp_dir: Path,
    server_url: str,
    personality_id: str,
    memory_dir: Path | None = None,
    personality_prompt: str | None = None,
) -> None:
    """Record caller audio, send it for processing, and play the response.

    Parameters
    ----------
    temp_dir:
        Directory used for temporary audio files.
    server_url:
        Base URL of the LLM processing server.
    memory_dir:
        Optional directory for storing interaction logs.
    personality_prompt:
        Optional prompt text used to generate a call situation.
    """

    situation: str | None = None
    memory_snippets: list[str] = []
    if memory_dir is not None:
        memory = load_memory(memory_dir, personality_id)
        memory_snippets = [m.get("summary", "") for m in memory[-2:]]

    if personality_prompt is not None:
        try:
            situation = generate_situation(
                server_url, personality_id, memory_snippets, personality_prompt
            )
        except Exception:
            situation = None

    recorded = temp_dir / "caller.wav"
    try:
        record_until_silence(recorded)
    except Exception:  # pragma: no cover - log failure
        logger.exception("recording failed")
        return

    with recorded.open("rb") as fh:
        data = {"character_id": personality_id}
        if situation:
            data["situation"] = situation
        if personality_prompt is not None:
            prompt = build_prompt(personality_prompt, memory_snippets, situation)
            data["prompt"] = prompt

        try:
            response = requests.post(
                f"{server_url}/process-audio",
                files={"audio_file": fh},
                data=data,
            )
            response.raise_for_status()
        except Exception:  # pragma: no cover - log failure
            logger.exception("LLM request failed")
            return

    response_path = temp_dir / "response.wav"
    response_path.write_bytes(response.content)

    play_wav(response_path)

    if memory_dir is not None:
        log_interaction(
            memory_dir,
            personality_id,
            caller_extension="unknown",
            summary="",
            name_guess="",
            quotes=[],
        )
