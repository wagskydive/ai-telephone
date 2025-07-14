# Backend API Server

This Flask application exposes two basic endpoints used by the phone firmware.

- `/process-audio` accepts an uploaded WAV file and returns a WAV response.
  For now the endpoint simply echoes the uploaded audio bytes.
- `/generate-situation` returns a short text snippet describing a call
  situation based on the provided `character_id`.

The app is created via `src.api_server.create_app()` and can be launched
with `python -m src.api_server`.
