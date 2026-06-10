"""
ProfileSheet — replica del frontendx.
Bottom sheet con drag handle, perfil, quick actions horizontales, cuentas.
"""
import flet as ft
from theme import C, I, icon, _b, pad, CENT, divider, RADIUS_MD, RADIUS_SHEET, gradient_border


def profile_sheet(page: ft.Page, visible: bool, on_close) -> ft.Container:
    is_business = True
    accent = C.GOLD if is_business else C.GREEN
    accent_dim = C.GOLD_DIM if is_business else C.GREEN_DIM

    quick_actions = [
        ("branches", "Sucursales", "branches"),
        ("team", "Equipo", "people"),
        ("messages", "Mensajes", "messages"),
        ("settings", "Ajustes", "settings"),
        ("gamification", "Gamific.", "gamification"),
        ("social", "Social", "social"),
    ]

    quick_chips = []
    for _, label, ico in quick_actions:
        quick_chips.append(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Container(
                            content=icon(ico, size=22, color=accent),
                            width=48, height=48, border_radius=24,
                            bgcolor=C.GOLD_FAINT, alignment=CENT,
                        ),
                        ft.Text(label, size=8, color=C.TEXT_DIM, font_family="monospace",
                                text_align=ft.TextAlign.CENTER),
                    ],
                    spacing=6,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=pad(v=8, h=12),
                on_click=lambda e: on_close(), ink=True,
            )
        )

    quick_row = ft.Row(quick_chips, spacing=2, scroll=ft.ScrollMode.AUTO,
                       alignment=ft.MainAxisAlignment.CENTER)

    def _account(initials, name, detail, acctype, is_active, on_click):
        av_border = accent_dim if is_active else C.BORDER
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Text(initials, size=12, weight="bold",
                                        color=C.TEXT, text_align=ft.TextAlign.CENTER),
                        width=36, height=36, border_radius=18,
                        bgcolor=C.GOLD_FAINT,
                        border=_b(2, av_border),
                        alignment=CENT,
                    ),
                    ft.Column(
                        [ft.Text(name, size=14, weight="bold", color=C.TEXT),
                         ft.Text(detail, size=9, color=C.TEXT_DIM, font_family="monospace")],
                        spacing=1, expand=True,
                    ),
                    icon("check", size=18, color=accent) if is_active else ft.Container(),
                ], spacing=12,
            ),
            padding=pad(v=10, h=16), border_radius=RADIUS_MD,
            bgcolor=C.GOLD_FAINT if is_active else None,
            on_click=on_click, ink=True,
        )

    content = ft.Column(
        [
            ft.Container(height=12),
            ft.Container(
                content=ft.Container(width=36, height=5, border_radius=3,
                                     bgcolor=C.DRAG_HANDLE_BG),
                alignment=CENT,
            ),
            ft.Container(height=4),
            ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Text("AD", size=18, weight="bold", color=C.TEXT,
                                            text_align=ft.TextAlign.CENTER),
                            width=48, height=48, border_radius=24,
                            bgcolor=C.AVATAR_BG2,
                            border=_b(2, accent_dim),
                            alignment=CENT,
                        ),
                        ft.Column(
                            [ft.Text("Admin Demo", size=16, weight="bold", color=C.TEXT),
                             ft.Text("admin@demo.com", size=9, color=C.TEXT_DIM, font_family="monospace")],
                            spacing=1, expand=True,
                        ),
                        ft.Container(
                            content=ft.Text("BUSINESS", size=7, color=accent, weight="bold",
                                            font_family="monospace"),
                            border=_b(1, accent_dim),
                            border_radius=999, padding=pad(v=3, h=8),
                        ),
                    ], spacing=14,
                ),
                padding=pad(t=4, b=16, h=20),
            ),
            divider(),
            ft.Container(content=ft.Text("ACCESO RAPIDO", size=8, color=C.TEXT_DIM, weight="bold",
                    font_family="monospace"), padding=pad(l=20, t=12)),
            ft.Container(height=8),
            quick_row,
            divider(),
            ft.Container(content=ft.Text("CAMBIAR CUENTA", size=8, color=C.TEXT_DIM, weight="bold",
                    font_family="monospace"), padding=pad(l=20, t=12)),
            ft.Container(height=8),
            _account("US", "Cuenta Consumer", "admin@demo.com", "consumer", False, lambda e: None),
            ft.Container(height=6),
            _account("AD", "Admin Demo", "1 sucursal", "business", True, lambda e: None),
            divider(),
            ft.Container(
                content=ft.Row([icon("add", size=18, color=C.TEXT_MUTED),
                                ft.Text("Crear cuenta business", size=14, color=C.TEXT_MUTED)],
                               spacing=12),
                on_click=lambda e: on_close(), ink=True,
                padding=pad(v=12, h=24),
            ),
            ft.Container(height=6),
            ft.Container(
                content=ft.Row([icon("logout", size=18, color=C.RED),
                                ft.Text("Cerrar sesion", size=14, color=C.RED)],
                               spacing=12),
                on_click=lambda e: (page.go("/login"), on_close()),
                ink=True, padding=pad(v=12, h=24),
            ),
            ft.Container(height=20),
        ],
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
    )

    return gradient_border(
        content=content,
        colors=[C.GREEN, C.GOLD, C.RED, C.TEXT],
        width=1.0,
        radius=22,
        bgcolor=C.POPUP_BG,
    )
