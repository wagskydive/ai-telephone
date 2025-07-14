"""Voice Activity Detector-based recorder."""
from __future__ import annotations

from pathlib import Path
import wave
import sounddevice as sd
import webrtcvad


def record_until_silence(
    output_path: Path,
    sample_rate: int = 16_000,
    frame_duration: float = 0.03,
    silence_duration: float = 1.0,
) -> None:
    """Record audio until silence is detected and save to ``output_path``.

    Parameters
    ----------
    output_path:
        Destination for the recorded WAV file.
    sample_rate:
        Audio sample rate in Hz.
    frame_duration:
        Frame size in seconds for VAD analysis.
    silence_duration:
        Amount of consecutive silence (in seconds) required to stop recording.
    """

    vad = webrtcvad.Vad(2)
    frame_size = int(sample_rate * frame_duration)
    silence_frames = int(silence_duration / frame_duration)

    frames: list[bytes] = []
    silence_counter = 0

    with sd.RawInputStream(
        samplerate=sample_rate,
        blocksize=frame_size,
        dtype="int16",
        channels=1,
    ) as stream:
        while True:
            audio = stream.read(frame_size)[0]
            frames.append(audio)

            if vad.is_speech(audio, sample_rate):
                silence_counter = 0
            else:
                silence_counter += 1

            if silence_counter >= silence_frames:
                break

    with wave.open(str(output_path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # int16
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames))
