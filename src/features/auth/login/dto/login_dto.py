"""
Login DTO — Request/Response models.
"""
from dataclasses import dataclass


@dataclass
class LoginRequest:
    email: str
    password: str


@dataclass
class LoginResponse:
    token: str
    user_id: str
    role: str
    display_name: str = ""
