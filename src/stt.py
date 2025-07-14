"""Speech-To-Text utilities using Whisper when available."""
from __future__ import annotations


from tempfile import NamedTemporaryFile
import logging

logger = logging.getLogger(__name__)

try:  # Optional heavy dependency
    import whisper  # type: ignore
except Exception:  # pragma: no cover - fallback when whisper missing
    whisper = None

def transcribe(audio_bytes: bytes) -> str:
    """Transcribe ``audio_bytes`` using Whisper if installed."""
    if not audio_bytes:
        return ""

    if whisper is None:  # pragma: no cover - environment without whisper
        return "beep"

    try:
        with NamedTemporaryFile(suffix=".wav") as tmp:
            tmp.write(audio_bytes)
            tmp.flush()
            model = whisper.load_model("base")
            result = model.transcribe(tmp.name)
            return result.get("text", "")
    except Exception:  # pragma: no cover - log failure and fallback
        logger.exception("whisper failed")
        return ""
