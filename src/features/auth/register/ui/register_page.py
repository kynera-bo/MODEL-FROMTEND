"""
Register page.
"""
import flet as ft
from theme import C, pad, _b, F_H2, F_CAPTION, SPACE_LG, SPACE_SM, SPACE_XXL, RADIUS_MD, RADIUS_XL
from features.auth.login.ui.shared import label, auth_card


def register_screen(page: ft.Page) -> ft.View:
    fields = [
        ("NOMBRE DE LA EMPRESA", "Mi Negocio SRL", False),
        ("TU NOMBRE", "", False), ("TU APELLIDO", "", False),
        ("EMAIL", "", False), ("PASSWORD", "", True), ("CONFIRMAR PASSWORD", "", True),
    ]
    inputs = []
    for lbl, placeholder, is_pwd in fields:
        inputs.append(label(lbl))
        inputs.append(ft.Container(height=8))
        inputs.append(ft.TextField(
            hint_text=placeholder, password=is_pwd, can_reveal_password=is_pwd,
            bgcolor=C.SURFACE, border_color=C.BORDER, border_radius=10,
            color=C.TEXT, width=320, height=44, cursor_color=C.ACCENT,
            focused_border_color=C.ACCENT_DIM, content_padding=pad(v=10, h=14),
        ))
        inputs.append(ft.Container(height=12))

    def do_register(e):
        page.go("/login")

    return ft.View(
        route="/register", bgcolor=C.BG, padding=0,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            auth_card(ft.Column([
                ft.Text("Crear Empresa", size=F_H2, weight="bold", color=C.TEXT),
                ft.Text("Registrate como dueno de tu negocio", size=F_CAPTION, color=C.TEXT_MUTED),
                ft.Container(height=SPACE_LG),
                *inputs,
                ft.Button(
                    content=ft.Text("Crear Empresa", color=C.BG), on_click=do_register,
                    bgcolor=C.ACCENT,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=RADIUS_MD),
                                         padding=pad(v=12, h=SPACE_LG)),
                    width=320),
                ft.Container(height=SPACE_SM),
                ft.TextButton("Ya tengo cuenta", on_click=lambda e: page.go("/login"),
                              style=ft.ButtonStyle(color=C.TEXT_MUTED)),
            ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0, scroll=ft.ScrollMode.AUTO,
            ), width=420),
        ],
    )


class RegisterPage:
    """Wrapper class para router lazy loading."""
    def build(self, page: ft.Page) -> ft.View:
        return register_screen(page)
