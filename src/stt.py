"""Simple placeholder Speech-To-Text implementation."""
from __future__ import annotations


def transcribe(audio_bytes: bytes) -> str:
    """Return a dummy transcription for given audio bytes."""
    # A real implementation would run Whisper or another STT engine here.
    if not audio_bytes:
        return ""
    return "beep"
