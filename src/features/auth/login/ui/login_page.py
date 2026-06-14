"""
Login page.
"""
import flet as ft
from theme import C, pad, icon, F_H2, F_CAPTION, SPACE_SM, SPACE_LG, SPACE_XL, RADIUS_MD
from features.auth.login.ui.shared import label, input_field, auth_card


def login_screen(page: ft.Page, auth: dict) -> ft.View:
    email = ft.TextField(
        hint_text="tu@email.com", bgcolor=C.SURFACE, border_color=C.BORDER,
        border_radius=10, color=C.TEXT, width=320, height=44,
        cursor_color=C.ACCENT, focused_border_color=C.ACCENT_DIM,
        content_padding=pad(v=10, h=14))

    pwd = ft.TextField(
        hint_text="Password", password=True, can_reveal_password=True,
        bgcolor=C.SURFACE, border_color=C.BORDER, border_radius=10,
        color=C.TEXT, width=320, height=44, cursor_color=C.ACCENT,
        focused_border_color=C.ACCENT_DIM, content_padding=pad(v=10, h=14))

    def do_login(e):
        auth["token"] = "demo-token"
        page.go("/")

    return ft.View(
        route="/login", bgcolor=C.BG, padding=0,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            auth_card(ft.Column([
                icon("sparkles", size=28, color=C.ACCENT),
                ft.Container(height=16),
                ft.Text("Gestos", size=F_H2, weight="bold", color=C.TEXT),
                ft.Text("Sistema de Monitoreo Laboral", size=F_CAPTION, color=C.TEXT_MUTED),
                ft.Container(height=SPACE_XL),
                input_field("EMAIL", "tu@email.com"),
                ft.Container(height=SPACE_SM),
                input_field("PASSWORD", "", password=True),
                ft.Container(height=SPACE_LG),
                ft.Button(
                    content=ft.Text("Ingresar", color=C.BG),
                    on_click=do_login, bgcolor=C.ACCENT,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=RADIUS_MD),
                                         padding=pad(v=12, h=SPACE_LG)),
                    width=320),
                ft.Container(height=SPACE_SM),
                ft.TextButton("Crear empresa", on_click=lambda e: page.go("/register"),
                              style=ft.ButtonStyle(color=C.TEXT_MUTED)),
            ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
            )),
        ],
    )


class LoginPage:
    """Wrapper class para router lazy loading."""
    def __init__(self, auth: dict):
        self.auth = auth

    def build(self, page: ft.Page) -> ft.View:
        return login_screen(page, self.auth)
