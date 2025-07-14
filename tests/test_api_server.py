import io
from unittest import mock

from src.api_server import create_app


def test_process_audio():
    app = create_app()
    client = app.test_client()
    with mock.patch(
        "src.api_server.transcribe", return_value="hello"
    ) as tr, mock.patch("src.api_server.synthesize", return_value=b"hi") as syn:
        response = client.post(
            "/process-audio",
            data={"audio_file": (io.BytesIO(b"data"), "in.wav")},
        )
        assert response.status_code == 200
        assert response.data == b"hi"
        tr.assert_called_once()
        syn.assert_called_once_with("hello")


def test_generate_situation():
    app = create_app()
    client = app.test_client()
    response = client.post("/generate-situation", json={"character_id": "cap"})
    assert response.status_code == 200
    assert response.get_json()["situation"] == "situation for cap"


def test_api_key_required():
    app = create_app(api_key="tok")
    client = app.test_client()
    with mock.patch("src.api_server.transcribe", return_value="hi") as tr, mock.patch(
        "src.api_server.synthesize", return_value=b"out"
    ):
        unauthorized = client.post("/process-audio")
        assert unauthorized.status_code == 401
        authorized = client.post("/process-audio", headers={"X-API-Key": "tok"})
        assert authorized.status_code == 200
