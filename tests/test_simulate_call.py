from unittest import mock

import src.simulate_call as sc


def test_simulate_call_text(tmp_path):
    out = tmp_path / "out.wav"
    with mock.patch.object(sc.tts, "synthesize", return_value=b"wav") as synth, \
         mock.patch.object(sc.llm, "generate_response", return_value="r") as gen, \
         mock.patch.object(sc, "play_wav") as play:
        sc.simulate_call(text="hello", prompt=None, output=out)
        gen.assert_called_once_with("hello", None)
        synth.assert_called_once_with("r", method="dummy")
        play.assert_called_once_with(out)
        assert out.read_bytes() == b"wav"


def test_cli_text(monkeypatch, tmp_path):
    out = tmp_path / "x.wav"
    called = {}

    def fake_sim(audio, text, prompt, *, tts_method, output):
        called["args"] = (audio, text, prompt, tts_method, output)

    monkeypatch.setattr(sc, "simulate_call", fake_sim)
    sc.main(["--text", "hi", "--out", str(out)])
    assert called["args"] == (None, "hi", None, "dummy", out)
