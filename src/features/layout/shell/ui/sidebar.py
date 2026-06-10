"""
SidebarDesktop — frontendv2
Logo app icon + nav sections con divisores + perfil.
"""
import flet as ft
from theme import C, I, icon, _b, pad, CENT, divider, BUSINESS_NAV, CONSUMER_NAV, RADIUS_MD, SPACE_MD, SPACE_SM, SPACE_LG, gradient_border


def sidebar_desktop(page: ft.Page, is_business: bool, on_toggle_popup) -> ft.Container:
    nav = BUSINESS_NAV if is_business else CONSUMER_NAV
    accent = C.GOLD if is_business else C.GREEN
    accent_dim = C.GOLD_DIM if is_business else C.GREEN_DIM

    header = ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    content=icon("sparkles", size=16, color=C.GOLD),
                    width=30, height=30, border_radius=8,
                    bgcolor=C.GOLD_FAINT,
                    alignment=CENT,
                    on_click=lambda e: page.go("/"),
                    ink=True,
                ),
                ft.Row(
                    [
                        ft.IconButton(
                            icon=icon("bell", size=16, color=C.TEXT_DIM).icon,
                            icon_size=16, icon_color=C.TEXT_DIM,
                            on_click=lambda e: page.go("/notifications"),
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16)),
                        ),
                        ft.IconButton(
                            icon=icon("chat", size=14, color=C.TEXT_DIM).icon,
                            icon_size=14, icon_color=C.TEXT_DIM,
                            on_click=lambda e: page.go("/messages"),
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16)),
                        ),
                    ], spacing=0,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=pad(t=12, b=12, h=10),
    )

    nav_items = []
    for idx, section in enumerate(nav):
        if idx > 0:
            nav_items.append(ft.Container(height=SPACE_SM))
            nav_items.append(divider())
            nav_items.append(ft.Container(height=SPACE_SM))
        nav_items.append(
            ft.Text(section["section"].upper(), size=8, color=C.TEXT_DIM,
                    weight="bold", font_family="monospace")
        )
        nav_items.append(ft.Container(height=4))

        for item in section["items"]:
            is_active = page.route == item["route"]
            clr = C.TEXT if is_active else C.TEXT_MUTED
            bg = C.GOLD_FAINT if is_active else None
            ic = icon(item["icon"], size=16, color=clr)
            nav_items.append(
                ft.Container(
                    content=ft.Row([ic, ft.Text(item["label"], size=13, color=clr)], spacing=10),
                    padding=pad(v=9, h=12), border_radius=RADIUS_MD,
                    bgcolor=bg,
                    on_click=lambda e, r=item["route"]: page.go(r),
                    ink=True,
                )
            )
            nav_items.append(ft.Container(height=1))

    nav_column = ft.Column(nav_items, spacing=0, scroll=ft.ScrollMode.AUTO, expand=True)
    nav_container = ft.Container(content=nav_column, padding=pad(h=6), expand=True)

    initials = "AD"
    profile_btn = ft.Container(
        on_click=lambda e: on_toggle_popup(),
        content=ft.Row(
            [
                 ft.Container(
                    content=ft.Text(initials, size=10, weight="bold", color=C.TEXT,
                                    text_align=ft.TextAlign.CENTER),
                    width=30, height=30, border_radius=15,
                    bgcolor=C.AVATAR_BG,
                    border=_b(2, accent_dim),
                    alignment=CENT,
                ),
                ft.Column(
                    [
                        ft.Text("Admin Demo", size=13, weight="bold", color=C.TEXT,
                                overflow=ft.TextOverflow.ELLIPSIS),
                        ft.Text("MODO NEGOCIO" if is_business else "CONSUMIDOR", size=8,
                                color=accent, weight="bold", font_family="monospace"),
                    ], spacing=1, expand=True,
                ),
                icon("chevron_down", size=12, color=C.TEXT_DIM),
            ], spacing=10,
        ),
        padding=pad(v=9, h=10), border_radius=RADIUS_MD,
    )

    profile_section = ft.Container(
        content=ft.Column([divider(), profile_btn], spacing=SPACE_SM),
        padding=pad(v=SPACE_SM, h=10),
    )

    sidebar = gradient_border(
        content=ft.Column([header, nav_container, profile_section], spacing=0, expand=True),
        colors=[C.GREEN, C.GOLD, C.RED, C.TEXT],
        width=0.8,
        radius=14,
        bgcolor=C.SIDEBAR_BG,
        expand=False,
    )
    sidebar.width = 220
    return sidebar
