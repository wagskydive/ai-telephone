"""AI Telephone firmware package."""

from .api_server import create_app
from .gui.app import create_app as create_gui_app

__all__ = ["create_app", "create_gui_app"]
