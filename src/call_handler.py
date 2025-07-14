"""Core handler for AI phone calls."""
from __future__ import annotations

from pathlib import Path
import requests

from .audio_player import play_wav
from .vad_recorder import record_until_silence


def handle_call(temp_dir: Path, server_url: str) -> None:
    """Record caller audio, send it for processing, and play the response.

    Parameters
    ----------
    temp_dir:
        Directory used for temporary audio files.
    server_url:
        Base URL of the LLM processing server.
    """

    recorded = temp_dir / "caller.wav"
    record_until_silence(recorded)

    with recorded.open("rb") as fh:
        response = requests.post(
            f"{server_url}/process-audio",
            files={"audio_file": fh},
        )
        response.raise_for_status()

    response_path = temp_dir / "response.wav"
    response_path.write_bytes(response.content)

    play_wav(response_path)
