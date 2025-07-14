from __future__ import annotations

"""Simple Flask API server for audio processing."""

from flask import Flask, request, send_file, jsonify, abort
import io
import logging

from .stt import transcribe
from .tts import synthesize
from .llm import generate_response

logger = logging.getLogger(__name__)


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
        if not file:
            return ("", 400)
        audio = file.read()
        prompt = request.form.get("prompt")
        try:
            text = transcribe(audio)
            reply = generate_response(text, prompt)
            response_audio = synthesize(reply)
        except Exception:  # pragma: no cover - log unexpected failures
            logger.exception("processing failed")
            fallback = synthesize(
                "Sorry, something went wrong.",
                method="dummy",
            )
            return send_file(io.BytesIO(fallback), mimetype="audio/wav")
        return send_file(
            io.BytesIO(response_audio),
            mimetype="audio/wav",
            as_attachment=False,
            download_name="response.wav",
        )

    @app.post("/process-text")
    def process_text():
        """Send provided text to the LLM and return synthesized speech."""
        check_key()
        data = request.get_json(force=True, silent=True) or {}
        text = data.get("text")
        if not text:
            return ("", 400)
        prompt = data.get("prompt")
        try:
            reply = generate_response(text, prompt)
            response_audio = synthesize(reply)
        except Exception:  # pragma: no cover - log unexpected failures
            logger.exception("text processing failed")
            return ("", 500)
        return send_file(io.BytesIO(response_audio), mimetype="audio/wav")

    @app.post("/generate-situation")
    def generate_situation():
        check_key()
        payload = request.get_json(force=True, silent=True) or {}
        char_id = payload.get("character_id", "unknown")
        memory = payload.get("memory_snippets", [])
        personality_prompt = payload.get("personality_prompt", "")
        prompt_lines = []
        if personality_prompt:
            prompt_lines.append(personality_prompt)
        prompt_lines.extend(memory)
        prompt_lines.append(
            f"Generate a short phone call situation for {char_id}."
        )
        prompt = "\n".join(prompt_lines)
        try:
            situation = generate_response("", prompt)
        except Exception:  # pragma: no cover - log unexpected failures
            logger.exception("situation generation failed")
            return jsonify({"situation": ""}), 500
        return jsonify({"situation": situation})

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
