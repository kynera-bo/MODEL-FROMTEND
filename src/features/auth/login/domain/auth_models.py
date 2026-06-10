"""
Auth domain models — User, LoginCredentials (Pydantic).
"""
from dataclasses import dataclass


@dataclass
class User:
    id: str
    email: str
    display_name: str = ""
    role: str = "consumer"

    @property
    def initials(self) -> str:
        parts = self.display_name.split() if self.display_name else [self.email.split("@")[0]]
        return "".join(p[0].upper() for p in parts[:2])
