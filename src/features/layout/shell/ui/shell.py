"""
MainShell — replica exacta del frontendx MainShell.tsx.
Responsive: Desktop = sidebar + content. Mobile = content + floating tab bar + profile sheet.
"""
import flet as ft
from theme import _b, C, SHELL_PAD, SIDEBAR_WIDTH, MOBILE_TAB_HEIGHT, MOBILE_TAB_BOTTOM, pad, CENT, gradient_border
from features.layout.shell.ui.sidebar import sidebar_desktop
from features.layout.shell.ui.tabbar import tab_bar_mobile
from features.layout.shell.ui.popup import account_popup
from features.layout.shell.ui.sheet import profile_sheet


class MainShellState:
    """Estado compartido del shell."""
    def __init__(self):
        self.is_business = True
        self.popup_visible = False
        self.sheet_visible = False

    def toggle_popup(self, page):
        self.sheet_visible = False
        self.popup_visible = not self.popup_visible
        _rebuild(page)

    def toggle_sheet(self, page):
        self.popup_visible = False
        self.sheet_visible = not self.sheet_visible
        _rebuild(page)

    def close_all(self, page):
        self.popup_visible = False
        self.sheet_visible = False
        _rebuild(page)


def _rebuild(page):
    """Forzar reconstruccion de vistas."""
    route = page.route
    page.views.clear()
    page.on_route_change(ft.RouteChangeEvent("route_change", page, route))
    page.update()


def main_shell(page: ft.Page, content: ft.Control) -> ft.View:
    shell_state = _get_shell_state(page)

    w = None
    try:
        w = page.width
    except Exception:
        pass
    if w is None:
        try:
            w = page.window_width
        except Exception:
            pass
    if w is None:
        w = 1200

    is_desktop = w >= 768

    if is_desktop:
        return _desktop_layout(page, content, shell_state)
    else:
        return _mobile_layout(page, content, shell_state)


def _desktop_layout(page, content, st) -> ft.View:
    sidebar_widget = sidebar_desktop(page, st.is_business, lambda: st.toggle_popup(page))

    main_row = ft.Row(
        [
            sidebar_widget,
            ft.Container(width=SHELL_PAD),
            ft.Container(content=content, expand=True),
        ],
        spacing=0,
    )

    shell = gradient_border(
        content=main_row,
        colors=[C.GREEN, C.GOLD, C.RED, C.TEXT],
        width=1.0,
        radius=18,
        bgcolor=C.SHELL_BG,
        padding=SHELL_PAD,
        expand=True,
    )

    if st.popup_visible:
        popup_widget = account_popup(page, st.popup_visible, lambda: st.close_all(page))
        layout = ft.Stack(
            [shell, ft.Container(content=popup_widget, left=SIDEBAR_WIDTH + SHELL_PAD * 2, bottom=32)],
            expand=True,
        )
    else:
        layout = shell

    return ft.View(
        route=page.route, bgcolor=C.BG, padding=SHELL_PAD,
        controls=[layout],
    )


def _mobile_layout(page, content, st) -> ft.View:
    tabbar = tab_bar_mobile(page, st.is_business, lambda: st.toggle_sheet(page))
    tab_row = ft.Row([tabbar], alignment=ft.MainAxisAlignment.CENTER)
    tab_container = ft.Container(content=tab_row, padding=pad(t=MOBILE_TAB_BOTTOM, b=MOBILE_TAB_BOTTOM, h=14))

    main_column = ft.Column(
        [
            ft.Container(content=content, expand=True),
            tab_container,
        ],
        spacing=0, expand=True,
    )

    if st.sheet_visible:
        sheet_content = profile_sheet(page, st.sheet_visible, lambda: st.close_all(page))
        sheet_bottom = MOBILE_TAB_HEIGHT + MOBILE_TAB_BOTTOM + 8

        layout = ft.Stack(
            [
                main_column,
                ft.Container(bgcolor=C.OVERLAY, expand=True,
                             on_click=lambda e: st.close_all(page)),
                ft.Container(
                    content=sheet_content,
                    left=32, right=32, bottom=sheet_bottom,
                ),
            ],
            expand=True,
        )
    else:
        layout = main_column

    return ft.View(
        route=page.route, bgcolor=C.BG, padding=0,
        controls=[layout],
    )


_shell_state = MainShellState()


def _get_shell_state(page) -> MainShellState:
    return _shell_state
