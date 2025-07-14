from unittest import mock

from src import stt, tts


def test_transcribe_with_whisper():
    model = mock.Mock()
    model.transcribe.return_value = {"text": "hello"}
    with mock.patch.object(stt, "whisper", mock.Mock(load_model=lambda name: model)):
        assert stt.transcribe(b"data") == "hello"


def test_transcribe_empty():
    assert stt.transcribe(b"") == ""


def test_synthesize_dummy():
    assert tts.synthesize("hi") == b"hi"


def test_synthesize_espeak(monkeypatch):
    class Dummy:
        name = "tmp.wav"

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def write(self, data):
            pass

        def flush(self):
            pass

        def read(self):
            return b"espeak"

    monkeypatch.setattr(tts, "NamedTemporaryFile", lambda suffix: Dummy())
    monkeypatch.setattr(tts.subprocess, "run", lambda *a, **k: None)
    assert tts.synthesize("hello", method="espeak") == b"espeak"


def test_synthesize_pyttsx3(monkeypatch):
    engine = mock.Mock()
    monkeypatch.setattr(tts, "pyttsx3", mock.Mock(init=lambda: engine))

    class Dummy:
        name = "tmp.wav"

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def write(self, data):
            pass

        def flush(self):
            pass

        def read(self):
            return b"pyttsx3"

    monkeypatch.setattr(tts, "NamedTemporaryFile", lambda suffix: Dummy())
    out = tts.synthesize("hello", method="pyttsx3")
    engine.save_to_file.assert_called_once()
    engine.runAndWait.assert_called_once()
    assert out == b"pyttsx3"
