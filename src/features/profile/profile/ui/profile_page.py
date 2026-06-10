"""
Profile y placeholder pages.
"""
import flet as ft
from theme import C, pad, F_H1, F_BODY, F_CAPTION, F_LABEL, CENT, SPACE_XXL


def profile_content(page: ft.Page) -> ft.Container:
    def _row(label, value):
        return ft.Row([
            ft.Text(label, size=F_CAPTION, color=C.TEXT_DIM, width=90),
            ft.Text(value, size=F_BODY, color=C.TEXT),
        ], spacing=8)

    def _section(title):
        return ft.Text(title.upper(), size=F_LABEL, color=C.TEXT_DIM, weight="bold",
                       font_family="monospace")

    return ft.Container(
        content=ft.Column([
            ft.Text("Mi Perfil", size=F_H1, weight="bold", color=C.TEXT),
            ft.Container(height=24),
            _section("CUENTA"),
            ft.Container(height=8),
            _row("Email:", "admin@demo.com"),
            _row("Rol:", "OWNER"),
            _row("Empresa:", "Mi Empresa Demo"),
            ft.Container(height=24),
            _section("LABORAL"),
            ft.Container(height=8),
            _row("Equipo:", "Administracion"),
            _row("Puesto:", "Gerente General"),
            _row("Nacimiento:", "1990-06-15"),
            _row("Genero:", "M"),
        ], spacing=4, scroll=ft.ScrollMode.AUTO),
        padding=SPACE_XXL, expand=True,
    )


def placeholder_content(route: str) -> ft.Container:
    return ft.Container(
        content=ft.Column([
            ft.Text("Proximamente", size=F_H1, weight="bold", color=C.TEXT),
            ft.Text(f"Ruta: {route}", size=F_CAPTION, color=C.TEXT_MUTED),
        ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=CENT, expand=True,
    )


class ProfilePage:
    def build(self, page: ft.Page) -> ft.Container:
        return profile_content(page)
