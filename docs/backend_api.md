# Backend API Server

This Flask application exposes several endpoints used by the phone firmware.

- `/process-audio` accepts an uploaded WAV file, runs speech-to-text via Whisper (if installed), sends the text and optional `prompt` to the LLM server, and returns a synthesized WAV response. When the server is started with an API key, the header `X-API-Key` must be included.
- `/process-text` sends plain text and optional `prompt` to the LLM and returns synthesized speech.
- `/generate-situation` builds a prompt from the provided `character_id`, optional memory snippets and personality prompt, then asks the LLM to return a short situation string.

The speech-to-text step relies on the `whisper` library when installed. Text-to-speech falls back to a simple dummy engine but supports `espeak`, `pyttsx3`, an optional [ElevenLabs](https://elevenlabs.io) API backend, and a remote Chatterbox server when configured via `CHATTERBOX_URL`.
Errors while contacting Whisper, the LLM server or a TTS backend are logged and result in an empty response with HTTP 500.

The app is created via `src.api_server.create_app()` and can be launched with `python -m src.api_server`.
`create_app` accepts optional `api_key` and `allowed_ips` arguments to restrict access.
