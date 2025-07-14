from unittest import mock
from src.call_handler import handle_call


def test_handle_call_network_failure(tmp_path):
    record_path = tmp_path / "caller.wav"
    import src.call_handler as ch
    with mock.patch("src.call_handler.record_until_silence") as rec, \
         mock.patch("src.call_handler.play_wav") as play, \
         mock.patch("src.call_handler.log_interaction") as log, \
         mock.patch.object(ch.requests, "post", side_effect=Exception("network fail")):
        rec.side_effect = lambda p: record_path.write_bytes(b"call")
        handle_call(tmp_path, "http://server", "captain", tmp_path)
        rec.assert_called_once_with(record_path)
        play.assert_not_called()
        log.assert_not_called()

