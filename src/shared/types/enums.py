"""
Shared enums — LoadState y otros tipos compartidos.
"""

from enum import Enum


class LoadState(Enum):
    IDLE = "idle"
    LOADING = "loading"
    SUCCESS = "success"
    ERROR = "error"


class AuthState(Enum):
    AUTHENTICATED = "authenticated"
    UNAUTHENTICATED = "unauthenticated"
    EXPIRED = "expired"


class UserRole(Enum):
    CONSUMER = "consumer"
    BUSINESS = "business"
    ADMIN = "admin"
