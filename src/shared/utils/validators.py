"""
Common form validation helpers.
"""

def validate_email(email: str) -> str | None:
    """Retorna mensaje de error o None si valido."""
    if not email:
        return "El email es requerido"
    if "@" not in email or "." not in email.split("@")[-1]:
        return "Email invalido"
    return None


def validate_password(password: str) -> str | None:
    """Retorna mensaje de error o None si valido."""
    if not password:
        return "La contrasena es requerida"
    if len(password) < 6:
        return "Minimo 6 caracteres"
    return None


def validate_required(value: str, field_name: str = "Campo") -> str | None:
    """Retorna mensaje de error o None si valido."""
    if not value or not value.strip():
        return f"{field_name} es requerido"
    return None
