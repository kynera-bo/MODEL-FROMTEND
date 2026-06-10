"""
AccountPopup — replica frontendx con iconos reales. Fondo opaco.
"""
import flet as ft
from theme import C, I, icon, _b, pad, CENT, divider, gradient_border


def account_popup(page: ft.Page, visible: bool, on_close) -> ft.Container:
    if not visible:
        return ft.Container()

    is_business = True
    accent = C.GOLD if is_business else C.GREEN
    accent_dim = C.GOLD_DIM if is_business else C.GREEN_DIM

    def _account_item(initials, name, detail, acctype, is_active, on_click):
        av_border = accent_dim if is_active else C.BORDER
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Text(initials, size=10, weight="bold",
                                        color=C.TEXT if is_active else C.TEXT_DIM,
                                        text_align=ft.TextAlign.CENTER),
                        width=30, height=30, border_radius=15,
                        bgcolor=C.AVATAR_BG,
                        border=_b(2, av_border),
                        alignment=CENT,
                    ),
                    ft.Column(
                        [
                            ft.Text(name, size=13, weight="bold",
                                    color=C.TEXT if is_active else C.TEXT_MUTED),
                            ft.Text(detail, size=9, color=C.TEXT_DIM2,
                                    font_family="monospace"),
                            ft.Container(
                                content=ft.Text(acctype.upper(), size=6, color=accent,
                                                weight="bold", font_family="monospace"),
                                border=_b(1, accent_dim),
                                border_radius=999, padding=pad(v=1, h=5),
                            ),
                        ], spacing=1, expand=True,
                    ),
                    icon("check", size=14, color=C.TEXT) if is_active else ft.Container(),
                ], spacing=10,
            ),
            padding=pad(v=8, h=6), border_radius=10,
            bgcolor=C.ITEM_ACTIVE_BG if is_active else None,
            on_click=on_click, ink=True,
        )

    content = ft.Column(
        [
            ft.Text("CUENTA ACTIVA", size=8, color=C.TEXT_DIM, weight="bold",
                    font_family="monospace"),
            ft.Container(height=10),
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text("AD", size=15, weight="bold", color=C.TEXT,
                                        text_align=ft.TextAlign.CENTER),
                        width=42, height=42, border_radius=21,
                        bgcolor=C.AVATAR_BG2,
                        border=_b(2, accent_dim),
                        alignment=CENT,
                    ),
                    ft.Column(
                        [ft.Text("Admin Demo", size=14, weight="bold", color=C.TEXT),
                         ft.Text("admin@demo.com", size=9, color=C.TEXT_DIM, font_family="monospace")],
                        spacing=1, expand=True,
                    ),
                    ft.Container(
                        content=ft.Text("BUSINESS", size=7, color=accent, weight="bold",
                                        font_family="monospace"),
                        border=_b(1, accent_dim),
                        border_radius=999, padding=pad(v=1, h=7),
                    ),
                ], spacing=12,
            ),
            ft.Container(height=12),
            divider().content,

            ft.Text("CAMBIAR CUENTA", size=8, color=C.TEXT_DIM, weight="bold",
                    font_family="monospace"),
            ft.Container(height=10),
            _account_item("US", "Cuenta Consumer", "admin@demo.com", "consumer", False,
                         lambda e: on_close()),
            _account_item("AD", "Admin Demo", "1 sucursal", "business", True,
                         lambda e: None),

            divider().content,

            ft.Container(
                content=ft.Row([icon("add", size=14, color=C.TEXT_DIM),
                                ft.Text("Crear cuenta business", size=13, color=C.TEXT_MUTED)],
                               spacing=10),
                on_click=lambda e: on_close(), ink=True, padding=pad(v=9, h=6),
                border_radius=10,
            ),
            ft.Container(
                content=ft.Row([icon("logout", size=14, color=C.RED),
                                ft.Text("Cerrar sesion", size=13, color=C.RED)],
                               spacing=10),
                on_click=lambda e: (page.go("/login"), on_close()),
                ink=True, padding=pad(v=9, h=6), border_radius=10,
            ),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )

    popup = gradient_border(
        content=content,
        colors=[C.GREEN, C.GOLD, C.RED, C.TEXT],
        width=1.0,
        radius=18,
        bgcolor=C.POPUP_BG,
        padding=pad(v=18, h=18),
    )
    popup.width = 288
    popup.shadow = ft.BoxShadow(spread_radius=1, blur_radius=40, color="#000000aa")
    return popup
