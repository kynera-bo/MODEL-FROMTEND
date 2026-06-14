"""
Gestos Frontend v3 — Flet + Aura Design System + Arquitectura Hexagonal
========================================================================
Ejecutar: python main.py           (desktop)
         python main.py --web     (browser, puerto 5050)
"""
import flet as ft
import flet_geolocator as ftg
from theme import C
from composition_root import init_container
from features.layout.shell.ui.shell import main_shell
from features.auth.login.ui.login_page import login_screen
from features.auth.register.ui.register_page import register_screen
from features.dashboard.dashboard.ui.dashboard_page import dashboard_content
from features.profile.profile.ui.profile_page import profile_content, placeholder_content
from features.showcase.showcase.ui.showcase_page import showcase_content
from features.map.map.ui.map_page import map_content

auth = {"token": "demo-token", "role": "owner", "user_id": "demo"}


def _init_geo(page):
    geo = ftg.Geolocator(
        configuration=ftg.GeolocatorConfiguration(
            accuracy=ftg.GeolocatorPositionAccuracy.LOW
        ),
        on_error=lambda e: print(f"Geolocator error: {e.data}"),
    )
    page.services.append(geo)
    page._geolocator = geo


def main(page: ft.Page):
    init_container()
    page.title = "Gestos"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = C.BG
    page.padding = 0
    page.on_route_change = lambda e: route_change(page, e)
    page.on_resize = lambda e: route_change(page, e)
    _init_geo(page)
    page.go("/login")


def route_change(page, e):
    page.views.clear()
    route = page.route

    if route == "/login":
        page.views.append(login_screen(page, auth))
    elif route == "/register":
        page.views.append(register_screen(page))
    elif not auth["token"]:
        page.views.append(login_screen(page, auth))
    else:
        inner, right_panel = _content_for(page, route)
        page.views.append(main_shell(page, inner, right_panel=right_panel))
    page.update()


def _content_for(page, route):
    if route == "/":
        return dashboard_content(page)
    if route == "/profile":
        return profile_content(page), None
    if route.startswith("/showcase"):
        return showcase_content(page), None
    if route == "/map":
        return map_content(page), None
    return placeholder_content(route), None


if __name__ == "__main__":
    import sys
    if "--web" in sys.argv:
        ft.run(main, view=ft.AppView.WEB_BROWSER, port=5050)
    else:
        ft.run(main, view=ft.AppView.FLET_APP)
