"""Minimal LLM client helpers."""
from __future__ import annotations

import os
import requests
import logging


_DEFAULT_URL = os.environ.get("LLM_API_URL", "http://localhost:8001")

logger = logging.getLogger(__name__)


def generate_response(text: str, prompt: str | None = None, *, url: str | None = None) -> str:
    """Send ``text`` and optional ``prompt`` to an LLM server and return its reply."""
    target = url or _DEFAULT_URL
    payload = {"text": text}
    if prompt:
        payload["prompt"] = prompt
    try:
        resp = requests.post(f"{target}/generate", json=payload)
        resp.raise_for_status()
        data = resp.json()
        return data.get("response", "")
    except Exception:  # pragma: no cover - log failure and fallback
        logger.exception("LLM request failed")
        return ""
