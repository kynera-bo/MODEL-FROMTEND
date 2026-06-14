"""
SidebarDesktopV2 — collapsible, pill-shaped with gradient border.
Expanded: 280px, icons + labels + sections.
Collapsed: 64px, only icons, no labels, no sections.
"""
import flet as ft
from theme import C, icon, _b, pad, CENT, divider, BUSINESS_NAV, CONSUMER_NAV, RADIUS_MD, SPACE_SM


EXPANDED_WIDTH = 280
COLLAPSED_WIDTH = 64


def sidebar_desktop_v2(
    page: ft.Page,
    is_business: bool,
    minimized: bool,
    on_toggle,
    on_toggle_popup,
) -> ft.Container:
    nav = BUSINESS_NAV if is_business else CONSUMER_NAV
    accent = C.ACCENT
    accent_dim = C.ACCENT_DIM

    def _nav_item(item, is_active, mini):
        clr = C.TEXT if is_active else C.TEXT_MUTED
        bg = C.ACCENT_FAINT if is_active else None
        icon_name = item["icon"] if is_active else item["icon"] + "_outlined"
        ic = icon(icon_name, size=18, color=clr)
        if mini:
            return ft.Container(
                content=ic,
                padding=pad(v=10, h=0),
                alignment=CENT,
                on_click=lambda e, r=item["route"]: page.go(r),
                ink=True,
                border_radius=8,
            )
        return ft.Container(
            content=ft.Row([ic, ft.Text(item["label"], size=13, color=clr)], spacing=10),
            padding=pad(v=9, h=12),
            border_radius=RADIUS_MD,
            bgcolor=bg,
            on_click=lambda e, r=item["route"]: page.go(r),
            ink=True,
        )

    # ---- Header ----
    if minimized:
        header = ft.Container(
            content=icon("sparkles", size=20, color=C.ACCENT),
            padding=pad(v=16, h=0),
            alignment=CENT,
            on_click=lambda e: page.go("/"),
            ink=True,
        )
    else:
        header = ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=icon("sparkles", size=16, color=C.ACCENT),
                        width=30, height=30, border_radius=8,
                        bgcolor=C.ACCENT_FAINT, alignment=CENT,
                        on_click=lambda e: page.go("/"), ink=True,
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                content=icon("bell", size=16, color=C.TEXT_DIM),
                                width=30, height=30, alignment=CENT,
                                on_click=lambda e: page.go("/notifications"), ink=True,
                            ),
                            ft.Container(
                                content=icon("chat", size=14, color=C.TEXT_DIM),
                                width=30, height=30, alignment=CENT,
                                on_click=lambda e: page.go("/messages"), ink=True,
                            ),
                        ],
                        spacing=0,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=pad(t=12, b=4, h=10),
        )

    # ---- Toggle button ----
    toggle_btn = ft.Container(
        content=icon("chevron_left" if not minimized else "chevron_right", size=12, color=C.TEXT_DIM),
        width=22, height=22, border_radius=11,
        bgcolor=C.SURFACE2,
        border=_b(0.5, C.BORDER),
        alignment=CENT,
        on_click=lambda e: on_toggle(),
        ink=True,
    )

    if minimized:
        toggle_row = ft.Container(
            content=toggle_btn,
            padding=pad(v=8, h=0),
            alignment=CENT,
        )
    else:
        toggle_row = ft.Container(
            content=ft.Row(
                [ft.Container(expand=True), toggle_btn],
                spacing=0,
            ),
            padding=pad(v=4, b=8, h=10),
        )

    # ---- Nav items ----
    nav_controls: list[ft.Control] = []
    if not minimized:
        for idx, section in enumerate(nav):
            if idx > 0:
                nav_controls.append(ft.Container(height=SPACE_SM))
                nav_controls.append(divider())
                nav_controls.append(ft.Container(height=SPACE_SM))
            nav_controls.append(
                ft.Text(
                    section["section"].upper(), size=8, color=C.TEXT_DIM,
                    weight="bold", font_family="monospace",
                )
            )
            nav_controls.append(ft.Container(height=4))
            for item in section["items"]:
                is_active = page.route == item["route"]
                nav_controls.append(_nav_item(item, is_active, mini=False))
                nav_controls.append(ft.Container(height=1))
    else:
        nav_controls.append(ft.Container(height=4))
        for section in nav:
            for item in section["items"]:
                is_active = page.route == item["route"]
                nav_controls.append(_nav_item(item, is_active, mini=True))
                nav_controls.append(ft.Container(height=2))

    nav_column = ft.Column(nav_controls, spacing=0, scroll=ft.ScrollMode.AUTO, expand=True)
    nav_container = ft.Container(
        content=nav_column,
        padding=pad(h=0) if minimized else pad(h=6),
        expand=True,
    )

    # ---- Profile ----
    initials = "AD"
    if minimized:
        profile_btn = ft.Container(
            content=ft.Container(
                content=ft.Text(initials, size=10, weight="bold", color=C.TEXT,
                                text_align=ft.TextAlign.CENTER),
                width=30, height=30, border_radius=15,
                bgcolor=C.AVATAR_BG, border=_b(2, accent_dim), alignment=CENT,
            ),
            padding=pad(v=8, h=0),
            alignment=CENT,
            on_click=lambda e: on_toggle_popup(),
            ink=True,
        )
        profile_section = ft.Container(content=profile_btn, padding=pad(v=8, h=0))
    else:
        profile_btn = ft.Container(
            on_click=lambda e: on_toggle_popup(),
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Text(initials, size=10, weight="bold", color=C.TEXT,
                                        text_align=ft.TextAlign.CENTER),
                        width=30, height=30, border_radius=15,
                        bgcolor=C.AVATAR_BG, border=_b(2, accent_dim), alignment=CENT,
                    ),
                    ft.Column(
                        [
                            ft.Text("Admin Demo", size=13, weight="bold", color=C.TEXT,
                                    overflow=ft.TextOverflow.ELLIPSIS),
                            ft.Text("MODO NEGOCIO" if is_business else "CONSUMIDOR", size=8,
                                    color=accent, weight="bold", font_family="monospace"),
                        ],
                        spacing=1, expand=True,
                    ),
                    icon("chevron_down", size=12, color=C.TEXT_DIM),
                ],
                spacing=10,
            ),
            padding=pad(v=9, h=10),
            border_radius=RADIUS_MD,
        )
        profile_section = ft.Container(
            content=ft.Column([divider(), profile_btn], spacing=6),
            padding=pad(v=6, h=10),
        )

    inner_content = ft.Column(
        [header, toggle_row, nav_container, profile_section],
        spacing=0,
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER if minimized else ft.CrossAxisAlignment.STRETCH,
    )

    sidebar = ft.Container(
        content=inner_content,
        border_radius=40 if minimized else 18,
        bgcolor=C.SIDEBAR_BG,
        width=COLLAPSED_WIDTH if minimized else EXPANDED_WIDTH,
        animate=ft.Animation(300, "ease"),
    )
    return sidebar
