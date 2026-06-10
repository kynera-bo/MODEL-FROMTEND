"""
Centralized routing — todas las rutas en un solo lugar.
"""
import importlib

ROUTES = {
    "/login": "features.auth.login.ui.login_page:LoginPage",
    "/register": "features.auth.register.ui.register_page:RegisterPage",
    "/": "features.dashboard.dashboard.ui.dashboard_page:DashboardPage",
    "/profile": "features.profile.profile.ui.profile_page:ProfilePage",
    "/showcase": "features.showcase.showcase.ui.showcase_page:ShowcasePage",
}


def get_page_class(path: str):
    """Lazy import y devuelve la clase de pagina."""
    for route, class_path in ROUTES.items():
        if path.startswith(route) and (len(path) == len(route) or path[len(route)] == "/"):
            module_path, class_name = class_path.rsplit(":", 1)
            mod = importlib.import_module(module_path)
            return getattr(mod, class_name)
    return None
