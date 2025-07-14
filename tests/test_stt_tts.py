from src.stt import transcribe
from src.tts import synthesize


def test_transcribe():
    assert transcribe(b'data') == "beep"
    assert transcribe(b'') == ""


def test_synthesize():
    data = synthesize("hi")
    assert data == b"hi"
