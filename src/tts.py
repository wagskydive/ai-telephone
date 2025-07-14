"""Simple placeholder Text-To-Speech implementation."""
from __future__ import annotations


def synthesize(text: str) -> bytes:
    """Return dummy WAV bytes for given text."""
    # A real implementation would call a TTS engine and return WAV data.
    return text.encode("utf-8")
