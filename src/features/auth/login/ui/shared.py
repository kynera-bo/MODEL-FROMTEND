"""
Helpers compartidos para paginas de auth.
"""
import flet as ft
from theme import C, F_LABEL, RADIUS_XL, SPACE_XXL, SPACE_LG, pad, _b


def label(text: str) -> ft.Text:
    """Label mono uppercase para formularios."""
    return ft.Text(text.upper(), size=F_LABEL, color=C.TEXT_DIM, weight="bold", font_family="monospace")


def card(title: str, desc: str, color: str) -> ft.Container:
    """Card para dashboard — surface bg, borde gold, radius XL."""
    s = ft.border.BorderSide(0.1, C.BORDER)
    return ft.Container(
        content=ft.Column(
            [ft.Text(title, size=18, weight="bold", color=color),
             ft.Text(desc, size=12, color=C.TEXT_MUTED)],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6,
        ),
        bgcolor=C.SURFACE,
        border=ft.border.Border(top=s, left=s, right=s, bottom=s),
        border_radius=14,
        padding=pad(v=24, h=20),
        col={"sm": 6, "md": 4},
        ink=True,
    )


def input_field(label_text: str, placeholder: str = "", password: bool = False,
                width: int = 320) -> ft.Column:
    """Input con label mono + campo estilizado."""
    return ft.Column([
        label(label_text),
        ft.Container(height=8),
        ft.TextField(
            hint_text=placeholder, password=password, can_reveal_password=password,
            bgcolor=C.SURFACE, border_color=C.BORDER, border_radius=10,
            color=C.TEXT, width=width, height=44, cursor_color=C.ACCENT,
            focused_border_color=C.ACCENT_DIM,
            content_padding=pad(v=10, h=14),
        ),
    ], spacing=0)


def auth_card(content: ft.Control, width: int = 400) -> ft.Container:
    """Card centrada para paginas de auth (login/register)."""
    return ft.Container(
        content=content,
        bgcolor=C.SURFACE, border=_b(1, C.BORDER),
        border_radius=RADIUS_XL, padding=SPACE_XXL, width=width,
    )
