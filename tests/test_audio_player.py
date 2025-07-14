from pathlib import Path
from unittest import mock

import sys
print('sys.path in test_audio_player before import', sys.path[:3])

from src.audio_player import play_wav


def test_play_wav():
    path = Path("file.wav")
    with mock.patch("subprocess.run") as run:
        play_wav(path)
        run.assert_called_once_with(["aplay", str(path)], check=False)
print('sys.path during module import', sys.path[:3])
