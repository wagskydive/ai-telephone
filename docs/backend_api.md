# Backend API Server

This Flask application exposes two basic endpoints used by the phone firmware.

- `/process-audio` accepts an uploaded WAV file, runs speech-to-text via Whisper (if installed) and returns a synthesized WAV response. A `prompt` field may be supplied to steer the LLM. When the server is started with an API key, the header `X-API-Key` must be included.
- `/generate-situation` returns a short text snippet describing a call situation based on the provided `character_id`.

The speech-to-text step relies on the `whisper` library when installed. Text-to-speech falls back to a simple dummy engine but supports `espeak` and `pyttsx3` if available.

The app is created via `src.api_server.create_app()` and can be launched with `python -m src.api_server`.
`create_app` accepts optional `api_key` and `allowed_ips` arguments to restrict access.
