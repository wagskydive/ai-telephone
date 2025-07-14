# Web-Based GUI

The Flask GUI application lives in `src/gui/app.py`. It exposes a few JSON API
endpoints for managing personalities and viewing logs.

## Endpoints

- `GET /api/personalities` – Return the list of personalities from
  `data/personalities.json`.
- `POST /api/personalities/<pid>/toggle` – Enable or disable a personality for
  outbound calls.
- `GET /api/logs/<pid>` – Retrieve the memory log for the given personality.
- `GET /api/stats` – Return call statistics calculated from the memory logs.

Start the GUI locally with:

```bash
python -m src.gui.app
```

By default it listens on port **8080**. It can be proxied or run alongside the
main API server on the Raspberry Pi.
