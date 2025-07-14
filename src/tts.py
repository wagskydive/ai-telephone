"""Text-To-Speech helpers with multiple backends."""
from __future__ import annotations

from tempfile import NamedTemporaryFile
import subprocess

try:  # optional dependency
    import pyttsx3  # type: ignore
except Exception:  # pragma: no cover - pyttsx3 may not be installed
    pyttsx3 = None


def synthesize(text: str, method: str = "dummy") -> bytes:
    """Synthesize ``text`` to WAV bytes using ``method``.

    Supported methods are ``dummy`` (return UTF‑8 bytes), ``espeak`` using the
    ``espeak`` command, and ``pyttsx3`` when the library is available.
    """

    if method == "dummy":
        return text.encode("utf-8")

    if method == "espeak":
        with NamedTemporaryFile(suffix=".wav") as tmp:
            subprocess.run(["espeak", "-w", tmp.name, text], check=True)
            return tmp.read()

    if method == "pyttsx3" and pyttsx3 is not None:
        engine = pyttsx3.init()
        with NamedTemporaryFile(suffix=".wav") as tmp:
            engine.save_to_file(text, tmp.name)
            engine.runAndWait()
            return tmp.read()

    raise ValueError("Unknown TTS method")
