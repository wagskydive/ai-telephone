from __future__ import annotations

"""Simple Flask API server for audio processing."""

from flask import Flask, request, send_file, jsonify
import io

from .stt import transcribe
from .tts import synthesize


def create_app() -> Flask:
    """Return a configured Flask application."""
    app = Flask(__name__)

    @app.post('/process-audio')
    def process_audio():
        """Transcribe uploaded audio and return synthesized response."""
        file = request.files.get('audio_file')
        audio = file.read() if file else b''
        text = transcribe(audio)
        response_audio = synthesize(text)
        return send_file(
            io.BytesIO(response_audio),
            mimetype='audio/wav',
            as_attachment=False,
            download_name='response.wav',
        )

    @app.post('/generate-situation')
    def generate_situation():
        payload = request.get_json(force=True, silent=True) or {}
        char_id = payload.get('character_id', 'unknown')
        return jsonify({'situation': f'situation for {char_id}'})

    return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)
