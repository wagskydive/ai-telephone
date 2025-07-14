from __future__ import annotations

from flask import Flask, jsonify, abort
from pathlib import Path
import json
from ..analytics import compute_stats

PERSONALITIES_FILE = Path("data/personalities.json")
MEMORY_DIR = Path("memory")


def _load_personalities() -> list[dict]:
    return json.loads(PERSONALITIES_FILE.read_text())


def _save_personalities(data: list[dict]) -> None:
    PERSONALITIES_FILE.write_text(json.dumps(data, indent=2))


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/api/personalities")
    def get_personalities():
        return jsonify(_load_personalities())

    @app.post("/api/personalities/<pid>/toggle")
    def toggle_personality(pid: str):
        data = _load_personalities()
        for entry in data:
            if entry.get("id") == pid:
                entry["enabled"] = not entry.get("enabled", True)
                _save_personalities(data)
                return jsonify(entry)
        abort(404)

    @app.get("/api/logs/<pid>")
    def get_logs(pid: str):
        file_path = MEMORY_DIR / f"{pid}.json"
        if file_path.exists():
            return jsonify(json.loads(file_path.read_text()))
        return jsonify([])

    @app.get("/api/stats")
    def get_stats():
        return jsonify(compute_stats(MEMORY_DIR))

    return app


if __name__ == "__main__":  # pragma: no cover - manual launch
    create_app().run(host="0.0.0.0", port=8080)
