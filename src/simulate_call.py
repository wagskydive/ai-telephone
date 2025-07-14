"""Command-line tool to test the audio pipeline locally."""
from __future__ import annotations

from pathlib import Path
import argparse

from . import stt, llm, tts
from .audio_player import play_wav


def simulate_call(
    audio: Path | None = None,
    text: str | None = None,
    prompt: str | None = None,
    *,
    tts_method: str = "dummy",
    output: Path = Path("response.wav"),
) -> Path:
    """Run the STT → LLM → TTS pipeline using ``audio`` or ``text``.

    The synthesized response is written to ``output`` and the path is returned.
    """
    if text is None and audio is None:
        raise ValueError("audio or text required")

    if text is None:
        audio_bytes = audio.read_bytes() if audio else b""
        text = stt.transcribe(audio_bytes)

    reply = llm.generate_response(text, prompt)
    wav = tts.synthesize(reply, method=tts_method)
    output.write_bytes(wav)
    play_wav(output)
    return output


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Simulate a local AI call")
    parser.add_argument("--audio", type=Path, help="Path to WAV input")
    parser.add_argument("--text", help="Raw text input instead of audio")
    parser.add_argument("--prompt", help="Optional prompt override")
    parser.add_argument("--out", type=Path, default=Path("response.wav"))
    parser.add_argument("--tts", default="dummy", help="TTS method")
    args = parser.parse_args(argv)

    simulate_call(args.audio, args.text, args.prompt, tts_method=args.tts, output=args.out)


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()
