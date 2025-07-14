from pathlib import Path
from unittest import mock

from src.audio_player import play_wav


def test_play_wav():
    path = Path("file.wav")
    with mock.patch("subprocess.run") as run:
        play_wav(path)
        run.assert_called_once_with(["aplay", "-q", str(path)], check=False)
