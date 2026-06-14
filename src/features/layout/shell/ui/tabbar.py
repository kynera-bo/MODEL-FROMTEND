"""
TabBarMobile — floating pill bar.
"""
from theme import C, I, icon, pad, CENT, MOBILE_TAB_HEIGHT, _b, gradient_border
import flet as ft


def tab_bar_mobile(page: ft.Page, is_business: bool, on_toggle_sheet) -> ft.Container:
    accent = C.ACCENT
    ACTIVE_COLOR = C.ACCENT

    def _tab(icon_name, route):
        active = page.route == route
        color = ACTIVE_COLOR if active else C.TEXT_DIM
        bg = C.ACCENT_FAINT if active else None
        name = icon_name if active else icon_name + "_outlined"
        return ft.Container(
            content=icon(name, size=22, color=color),
            width=40, height=40, border_radius=20,
            bgcolor=bg, alignment=CENT,
            on_click=lambda e: page.go(route), ink=True,
        )

    tabs = [
        _tab("home", "/"),
        _tab("explore", "/explore"),
        _tab("map", "/map"),
        _tab("messages", "/messages"),
        _tab("bell", "/notifications"),
    ]

    avatar = ft.Container(
        content=ft.Container(
            content=ft.Text("AD", size=11, weight="bold", color=C.TEXT,
                            text_align=ft.TextAlign.CENTER),
            width=28, height=28, border_radius=14,
            bgcolor=C.AVATAR_BG,
            alignment=CENT,
        ),
        width=34, height=34, border_radius=17,
        border=ft.border.Border(
            top=ft.border.BorderSide(2, accent),
            left=ft.border.BorderSide(2, accent),
            right=ft.border.BorderSide(2, accent),
            bottom=ft.border.BorderSide(2, accent),
        ),
        alignment=CENT,
        on_click=lambda e: on_toggle_sheet(), ink=True,
    )

    tabbar = gradient_border(
        content=ft.Row(
            tabs + [avatar],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        colors=None,
        width=1.0,
        radius=28,
        bgcolor=C.TABBAR_BG,
        padding=pad(v=7, h=10),
    )
    tabbar.height = MOBILE_TAB_HEIGHT
    tabbar.width = 340
    return tabbar
