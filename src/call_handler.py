"""Core handler for AI phone calls."""
from __future__ import annotations

from pathlib import Path
import requests

from .audio_player import play_wav
from .vad_recorder import record_until_silence
from .memory_logger import log_interaction


def handle_call(temp_dir: Path, server_url: str, personality_id: str, memory_dir: Path | None = None) -> None:
    """Record caller audio, send it for processing, and play the response.

    Parameters
    ----------
    temp_dir:
        Directory used for temporary audio files.
    server_url:
        Base URL of the LLM processing server.
    memory_dir:
        Optional directory for storing interaction logs.
    """

    recorded = temp_dir / "caller.wav"
    record_until_silence(recorded)

    with recorded.open("rb") as fh:
        response = requests.post(
            f"{server_url}/process-audio",
            files={"audio_file": fh},
            data={"character_id": personality_id},
        )
        response.raise_for_status()

    response_path = temp_dir / "response.wav"
    response_path.write_bytes(response.content)

    play_wav(response_path)

    if memory_dir is not None:
        log_interaction(memory_dir, personality_id, caller_extension="unknown", summary="", name_guess="", quotes=[])
