"""
Dashboard page.
"""
import flet as ft
from theme import C, pad, F_H1, F_CAPTION, SPACE_XXL
from features.auth.login.ui.shared import card


def dashboard_content(page: ft.Page) -> ft.Container:
    cards = [
        ("Trabajadores", "Gestiona el personal", C.GREEN),
        ("Equipos", "Organiza los equipos", C.BLUE),
        ("Camaras", "Configura las camaras", C.GOLD),
        ("Asistencia", "Registros de entrada/salida", C.PURPLE),
        ("Tareas", "Gestion de tareas", C.GOLD_DIM),
        ("Analiticas", "Metricas y predicciones", C.RED_DIM),
    ]
    return ft.Container(
        content=ft.Column([
            ft.Text("Dashboard", size=F_H1, weight="bold", color=C.TEXT),
            ft.Text("Bienvenido al Sistema de Monitoreo Laboral", size=F_CAPTION, color=C.TEXT_MUTED),
            ft.Container(height=32),
            ft.ResponsiveRow(
                [card(t, d, c) for t, d, c in cards],
                spacing=16, run_spacing=16,
            ),
        ], spacing=0, scroll=ft.ScrollMode.AUTO),
        padding=SPACE_XXL, expand=True,
    )


class DashboardPage:
    def build(self, page: ft.Page) -> ft.Container:
        return dashboard_content(page)
