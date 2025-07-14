from __future__ import annotations

"""Simple Flask API server for audio processing."""

from flask import Flask, request, send_file, jsonify, abort
import io

from .stt import transcribe
from .tts import synthesize
from .llm import generate_response


def create_app(api_key: str | None = None, allowed_ips: list[str] | None = None) -> Flask:
    """Return a configured Flask application."""
    app = Flask(__name__)

    def check_key() -> None:
        if api_key and request.headers.get("X-API-Key") != api_key:
            abort(401)
        if allowed_ips and request.remote_addr not in allowed_ips:
            abort(403)

    @app.post("/process-audio")
    def process_audio():
        """Transcribe audio, send it to the LLM, and return synthesized speech."""
        check_key()
        file = request.files.get("audio_file")
        audio = file.read() if file else b""
        prompt = request.form.get("prompt")
        text = transcribe(audio)
        reply = generate_response(text, prompt)
        response_audio = synthesize(reply)
        return send_file(
            io.BytesIO(response_audio),
            mimetype="audio/wav",
            as_attachment=False,
            download_name="response.wav",
        )

    @app.post("/generate-situation")
    def generate_situation():
        check_key()
        payload = request.get_json(force=True, silent=True) or {}
        char_id = payload.get("character_id", "unknown")
        return jsonify({"situation": f"situation for {char_id}"})

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
