"""
AuthAdapter — Token management, session.
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AuthSession:
    token: Optional[str] = None
    role: str = "consumer"
    user_id: Optional[str] = None

    @property
    def is_authenticated(self) -> bool:
        return self.token is not None

    def clear(self):
        self.token = None
        self.user_id = None

    def set_session(self, token: str, user_id: str, role: str):
        self.token = token
        self.user_id = user_id
        self.role = role
