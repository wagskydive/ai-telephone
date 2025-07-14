from pathlib import Path
from unittest import mock

from src.vad_recorder import record_until_silence


def test_record_until_silence(tmp_path):
    out = tmp_path / "out.wav"
    fake_stream = mock.MagicMock()
    fake_stream.__enter__.return_value = fake_stream
    fake_stream.read.side_effect = [(b'abc', None), (b'def', None)]

    with mock.patch("sounddevice.RawInputStream", return_value=fake_stream) as rs, \
         mock.patch("wave.open") as wopen, \
         mock.patch("webrtcvad.Vad") as vad_cls:
        vad = vad_cls.return_value
        vad.is_speech.side_effect = [True, False]

        record_until_silence(out, sample_rate=16000, frame_duration=0.03, silence_duration=0.03)

        rs.assert_called()
        vad.is_speech.assert_called()
        wopen.assert_called_once()
