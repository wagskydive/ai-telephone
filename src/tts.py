"""Text-To-Speech helpers with multiple backends."""
from __future__ import annotations

from tempfile import NamedTemporaryFile
import subprocess
import os
import requests
import logging

try:  # optional dependency
    import pyttsx3  # type: ignore
except Exception:  # pragma: no cover - pyttsx3 may not be installed
    pyttsx3 = None

logger = logging.getLogger(__name__)


def synthesize(
    text: str,
    method: str = "dummy",
    *,
    api_key: str | None = None,
    voice_id: str = "21m00Tcm4TlvDq8ikWAM",
    base_url: str | None = None,
) -> bytes:
    """Synthesize ``text`` to WAV bytes using ``method``.

    Supported methods are ``dummy`` (return UTF‑8 bytes), ``espeak`` using the
    ``espeak`` command, ``pyttsx3`` when the library is available, ``chatterbox``
    which posts to a remote Chatterbox server, and ``elevenlabs`` which calls
    the ElevenLabs API.  For ``elevenlabs`` the API key is read from
    ``ELEVENLABS_API_KEY`` unless ``api_key`` is supplied, and the ``voice_id``
    can be overridden.  ``base_url`` overrides the default Chatterbox endpoint
    from ``CHATTERBOX_URL``.
    """

    if method == "dummy":
        return text.encode("utf-8")

    if method == "espeak":
        try:
            with NamedTemporaryFile(suffix=".wav") as tmp:
                subprocess.run(["espeak", "-w", tmp.name, text], check=True)
                return tmp.read()
        except Exception:  # pragma: no cover - log failure
            logger.exception("espeak failed")
            return synthesize(text, method="dummy")

    if method == "pyttsx3" and pyttsx3 is not None:
        try:
            engine = pyttsx3.init()
            with NamedTemporaryFile(suffix=".wav") as tmp:
                engine.save_to_file(text, tmp.name)
                engine.runAndWait()
                return tmp.read()
        except Exception:  # pragma: no cover - log failure
            logger.exception("pyttsx3 failed")
            return synthesize(text, method="dummy")

    if method == "chatterbox":
        url = base_url or os.getenv("CHATTERBOX_URL", "http://localhost:7860/speak")
        try:
            resp = requests.post(url, json={"text": text})
            resp.raise_for_status()
            return resp.content
        except Exception:  # pragma: no cover - log failure
            logger.exception("chatterbox failed")
            return synthesize(text, method="dummy")

    if method == "elevenlabs":
        key = api_key or os.getenv("ELEVENLABS_API_KEY")
        if not key:
            raise ValueError("ElevenLabs API key not set")
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        headers = {"xi-api-key": key}
        try:
            resp = requests.post(url, json={"text": text}, headers=headers)
            resp.raise_for_status()
            return resp.content
        except Exception:  # pragma: no cover - log failure
            logger.exception("elevenlabs failed")
            return synthesize(text, method="dummy")

    raise ValueError("Unknown TTS method")
