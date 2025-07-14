from pathlib import Path
from unittest import mock

from src.call_handler import handle_call


def test_handle_call(tmp_path):
    record_path = tmp_path / "caller.wav"
    response_path = tmp_path / "response.wav"

    with mock.patch("src.call_handler.record_until_silence") as rec, \
         mock.patch("src.call_handler.play_wav") as play, \
         mock.patch("src.call_handler.log_interaction") as log, \
         mock.patch("requests.post") as post:
        rec.side_effect = lambda p: Path(p).write_bytes(b"caller")
        post.return_value.status_code = 200
        post.return_value.content = b"wavdata"
        post.return_value.raise_for_status = lambda: None

        handle_call(tmp_path, "http://server", "captain", tmp_path)

        rec.assert_called_once_with(record_path)
        post.assert_called_once()
        play.assert_called_once_with(response_path)
        log.assert_called_once()
