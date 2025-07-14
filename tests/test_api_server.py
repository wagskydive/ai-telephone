import io
from unittest import mock

from src.api_server import create_app


def test_process_audio():
    app = create_app()
    client = app.test_client()
    with mock.patch(
        "src.api_server.transcribe", return_value="hello"
    ) as tr, mock.patch(
        "src.api_server.generate_response", return_value="reply"
    ) as llm, mock.patch(
        "src.api_server.synthesize", return_value=b"hi"
    ) as syn:
        response = client.post(
            "/process-audio",
            data={"audio_file": (io.BytesIO(b"data"), "in.wav")},
        )
        assert response.status_code == 200
        assert response.data == b"hi"
        tr.assert_called_once()
        llm.assert_called_once_with("hello", None)
        syn.assert_called_once_with("reply")


def test_generate_situation():
    app = create_app()
    client = app.test_client()
    with mock.patch(
        "src.api_server.generate_response", return_value="scene"
    ) as gen:
        resp = client.post(
            "/generate-situation",
            json={
                "character_id": "cap",
                "memory_snippets": ["m"],
                "personality_prompt": "p",
            },
        )
        assert resp.status_code == 200
        assert resp.get_json()["situation"] == "scene"
        gen.assert_called_once()


def test_process_text():
    app = create_app()
    client = app.test_client()
    with mock.patch(
        "src.api_server.generate_response", return_value="r"
    ) as llm, mock.patch(
        "src.api_server.synthesize", return_value=b"wav"
    ) as syn:
        resp = client.post(
            "/process-text",
            json={"text": "hi", "prompt": "p"},
        )
        assert resp.status_code == 200
        assert resp.data == b"wav"
        llm.assert_called_once_with("hi", "p")
        syn.assert_called_once_with("r")


def test_api_key_required():
    app = create_app(api_key="tok")
    client = app.test_client()
    with mock.patch("src.api_server.transcribe", return_value="hi") as tr, \
         mock.patch("src.api_server.generate_response", return_value="r") as llm, \
         mock.patch("src.api_server.synthesize", return_value=b"out"):
        unauthorized = client.post("/process-audio")
        assert unauthorized.status_code == 401
        authorized = client.post("/process-audio", headers={"X-API-Key": "tok"})
        assert authorized.status_code == 200
        llm.assert_called_once()


def test_allowed_ips():
    app = create_app(allowed_ips=["1.2.3.4"])
    client = app.test_client()
    with mock.patch("src.api_server.transcribe", return_value="hi"), \
         mock.patch("src.api_server.generate_response", return_value="r"), \
         mock.patch("src.api_server.synthesize", return_value=b"out"):
        disallowed = client.post("/process-audio", environ_overrides={"REMOTE_ADDR": "2.2.2.2"})
        assert disallowed.status_code == 403
        allowed = client.post(
            "/process-audio",
            environ_overrides={"REMOTE_ADDR": "1.2.3.4"},
        )
        assert allowed.status_code == 200
