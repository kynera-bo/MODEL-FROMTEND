"""
Config — Settings via environment variables / defaults.
"""
import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Settings:
    API_BASE_URL: str = field(default_factory=lambda: os.getenv("API_BASE_URL", "http://localhost:8000"))
    WS_URL: str = field(default_factory=lambda: os.getenv("WS_URL", "ws://localhost:8000/ws"))
    APP_TITLE: str = field(default_factory=lambda: os.getenv("APP_TITLE", "Gestos"))
    APP_VERSION: str = field(default_factory=lambda: os.getenv("APP_VERSION", "1.0.0"))
    DEBUG: bool = field(default_factory=lambda: os.getenv("DEBUG", "false").lower() == "true")
