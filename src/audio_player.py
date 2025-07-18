"""Simple audio playback utility."""
from __future__ import annotations

from pathlib import Path
import subprocess


def play_wav(file_path: Path) -> None:
    """Play a WAV file using system audio tools.

    Parameters
    ----------
    file_path:
        Path to the WAV file to play.
    """
    # ``-q`` suppresses header messages from ``aplay`` for slightly faster start.
    subprocess.run(["aplay", "-q", str(file_path)], check=False)
