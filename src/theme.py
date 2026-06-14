"""
Design Tokens — Kynera Brand System v1.
Paleta monocromática premium (negro/blanco/grises) + acento azul eléctrico.
Dark mode first. Sin colores Bolivia (verde/gold/rojo).
"""
import flet as ft
from flet.controls.material.icons import Icons as IconEnum

# ============================================================
#  COLORES — Dark Mode (Primario)
# ============================================================

class C:
    # ── Fondos ──
    BG          = "#000000"       # página
    SURFACE     = "#111111"       # cards, inputs, paneles
    SURFACE2    = "#1A1A1A"       # hover de cards, superficies secundarias
    SHELL_BG    = "#000000"       # contenedor desktop (mismo que BG)
    POPUP_BG    = "#181818"       # fondo popup/sheet
    OVERLAY     = "#CC000000"     # backdrop oscuro (#000000cc)

    # ── Fondos de componentes ──
    SIDEBAR_BG     = "#E6181818"  # Sidebar (rgba(24,24,24,0.9))
    TABBAR_BG      = "#F0121212"  # Tabbar (rgba(18,18,18,0.94))
    AVATAR_BG      = "#14FFFFFF"  # Avatar iniciales (rgba(255,255,255,0.08))
    AVATAR_BG2     = "#1AFFFFFF"  # Avatar activo (rgba(255,255,255,0.1))
    ITEM_ACTIVE_BG = "#0AFFFFFF"  # Elemento activo lista (rgba(255,255,255,0.04))
    DRAG_HANDLE_BG = "#26FFFFFF"  # Drag handle (rgba(255,255,255,0.15))

    # ── Bordes ──
    BORDER        = "#242424"     # borde estándar
    BORDER_HOVER  = "#3B82F6"     # hover/enfoque azul
    BORDER_STRONG = "#424242"     # borde fuerte (gris grafito)

    # ── Texto ──
    TEXT        = "#FFFFFF"       # headings, texto principal
    TEXT_MUTED  = "#C3C3C3"      # párrafos, descripciones
    TEXT_DIM    = "#818182"      # labels, metadata
    TEXT_DIM2   = "#40FFFFFF"    # texto secundario atenuado (rgba(255,255,255,0.25))

    # ── Acento (Azul Eléctrico) ──
    ACCENT       = "#3B82F6"     # azul eléctrico — botones, links, activo
    ACCENT_DIM   = "#1E40AF"     # azul profundo — hover estados
    ACCENT_FAINT = "#143B82F6"   # azul tenue (rgba(59,130,246,0.08))
    ACCENT_BG    = "#1F3B82F6"   # azul fondo (rgba(59,130,246,0.12))

    # ── Estados semánticos (versión monocromática) ──
    SUCCESS      = "#3B82F6"     # éxito = azul acento
    SUCCESS_BG   = "#1F3B82F6"   # fondo éxito
    ERROR        = "#DC2626"     # error (rojo sutil, solo para errores críticos)
    ERROR_BG     = "#1FDC2626"   # fondo error (rgba(220,38,38,0.12))

    # ── Gradiente para border premium (monocromático metálico) ──
    GRADIENT_BORDER = ["#1A1A1A", "#424242", "#818182", "#C3C3C3"]

# ============================================================
#  LIGHT MODE (Referencia — implementación futura)
# ============================================================
#  BG          = "#FFFFFF"
#  SURFACE     = "#F7F7F7"
#  SURFACE2    = "#EFEFEF"
#  TEXT        = "#000000"
#  TEXT_MUTED  = "#181818"
#  TEXT_DIM    = "#424242"
#  BORDER      = "#E0E0E0"
#  BORDER_HOVER = "#3B82F6"
#  ACCENT       = "#3B82F6"
#  ACCENT_DIM   = "#2563EB"
# ============================================================

# ============================================================
#  ESPACIADO + RADIOS
# ============================================================

SHELL_PAD = 8
SIDEBAR_WIDTH = 220
MOBILE_TAB_HEIGHT = 56
MOBILE_TAB_BOTTOM = 26

RADIUS_SM  = 6
RADIUS_MD  = 10
RADIUS_LG  = 14
RADIUS_XL  = 16
RADIUS_PILL = 999
RADIUS_POPUP = 18
RADIUS_SHEET = 22

SPACE_XS = 4; SPACE_SM = 8; SPACE_MD = 14; SPACE_LG = 20; SPACE_XL = 28; SPACE_XXL = 40

# ============================================================
#  TIPOGRAFIA (tamanios)
# ============================================================

F_H1 = 28   # titulo de pagina
F_H2 = 20   # titulo de seccion
F_H3 = 16   # titulo de card
F_BODY = 14 # texto cuerpo
F_CAPTION = 12  # secundario
F_LABEL = 9     # mono uppercase labels
F_MONO = 11     # codigo/metadata

# ============================================================
#  ICONOS MATERIAL (reales, via Flet)
# ============================================================

I = {
    "home": IconEnum.HOME, "home_outlined": IconEnum.HOME_OUTLINED,
    "search": IconEnum.SEARCH, "search_outlined": IconEnum.SEARCH_OUTLINED,
    "chat": IconEnum.MODE_COMMENT, "chat_outlined": IconEnum.MODE_COMMENT_OUTLINED,
    "bell": IconEnum.NOTIFICATIONS, "bell_outlined": IconEnum.NOTIFICATIONS_OUTLINED,
    "person": IconEnum.PERSON, "person_outlined": IconEnum.PERSON_OUTLINED,
    "trophy": IconEnum.EMOJI_EVENTS, "trophy_outlined": IconEnum.EMOJI_EVENTS_OUTLINED,
    "people": IconEnum.GROUP, "people_outlined": IconEnum.GROUP_OUTLINED,
    "settings": IconEnum.SETTINGS, "settings_outlined": IconEnum.SETTINGS_OUTLINED,
    "cube": IconEnum.INVENTORY_2, "cube_outlined": IconEnum.INVENTORY_2_OUTLINED,
    "receipt": IconEnum.RECEIPT, "receipt_outlined": IconEnum.RECEIPT_OUTLINED,
    "location": IconEnum.LOCATION_ON, "location_outlined": IconEnum.LOCATION_ON_OUTLINED,
    "add": IconEnum.ADD,
    "logout": IconEnum.LOGOUT, "logout_outlined": IconEnum.LOGOUT_OUTLINED,
    "check": IconEnum.CHECK,
    "chevron_down": IconEnum.KEYBOARD_ARROW_DOWN,
    "chevron_up": IconEnum.KEYBOARD_ARROW_UP,
    "sparkles": IconEnum.AUTO_AWESOME,
    "notifications": IconEnum.NOTIFICATIONS, "notifications_outlined": IconEnum.NOTIFICATIONS_OUTLINED,
    "messages": IconEnum.MODE_COMMENT, "messages_outlined": IconEnum.MODE_COMMENT_OUTLINED,
    "branches": IconEnum.ACCOUNT_TREE, "branches_outlined": IconEnum.ACCOUNT_TREE_OUTLINED,
    "orders": IconEnum.SHOPPING_CART, "orders_outlined": IconEnum.SHOPPING_CART_OUTLINED,
    "map": IconEnum.MAP, "map_outlined": IconEnum.MAP_OUTLINED,
    "explore": IconEnum.EXPLORE, "explore_outlined": IconEnum.EXPLORE_OUTLINED,
    "gamification": IconEnum.EMOJI_EVENTS, "gamification_outlined": IconEnum.EMOJI_EVENTS_OUTLINED,
    "social": IconEnum.GROUP, "social_outlined": IconEnum.GROUP_OUTLINED,
    "profile_menu": IconEnum.PERSON, "profile_menu_outlined": IconEnum.PERSON_OUTLINED,
    "favorite": IconEnum.FAVORITE,
    "favorite_border": IconEnum.FAVORITE_BORDER,
    "bookmark_border": IconEnum.BOOKMARK_BORDER,
    "send": IconEnum.SEND,
    "trending_up": IconEnum.TRENDING_UP,
    "event": IconEnum.EVENT,
    "star": IconEnum.STAR,
    "star_half": IconEnum.STAR_HALF,
    "star_border": IconEnum.STAR_BORDER,
    "code": IconEnum.CODE,
    "brush": IconEnum.BRUSH,
    "location": IconEnum.LOCATION_ON,
    "location_on": IconEnum.LOCATION_ON,
    "schedule": IconEnum.SCHEDULE,
    "play_arrow": IconEnum.PLAY_ARROW,
    "swap_horiz": IconEnum.SWAP_HORIZ,
    "more_vert": IconEnum.MORE_VERT,
    "remove": IconEnum.REMOVE,
    "delete_outline": IconEnum.DELETE_OUTLINE,
    "tune": IconEnum.TUNE,
    "history": IconEnum.HISTORY,
    "info": IconEnum.INFO,
    "play_circle_filled": IconEnum.PLAY_CIRCLE_FILLED,
    "close": IconEnum.CLOSE,
    "check_circle": IconEnum.CHECK_CIRCLE,
    "inventory_2": IconEnum.INVENTORY_2,
}

# ============================================================
#  NAV CONFIG
# ============================================================

CONSUMER_NAV = [
    {"section": "Principal", "items": [
        {"id": "home", "label": "Inicio", "icon": "home", "route": "/"},
        {"id": "explore", "label": "Explorar", "icon": "explore", "route": "/explore"},
        {"id": "messages", "label": "Mensajes", "icon": "messages", "route": "/messages"},
        {"id": "notifications", "label": "Notificaciones", "icon": "bell", "route": "/notifications"},
    ]},
    {"section": "Social", "items": [
        {"id": "profile", "label": "Perfil", "icon": "profile_menu", "route": "/profile"},
        {"id": "gamification", "label": "Gamificacion", "icon": "gamification", "route": "/gamification"},
        {"id": "social", "label": "Social", "icon": "social", "route": "/social"},
        {"id": "settings", "label": "Ajustes", "icon": "settings", "route": "/settings"},
    ]},
    {"section": "Dev", "items": [
        {"id": "showcase", "label": "Componentes", "icon": "cube", "route": "/showcase"},
        {"id": "map", "label": "Mapa", "icon": "location", "route": "/map"},
    ]},
]

BUSINESS_NAV = [
    {"section": "Negocio", "items": [
        {"id": "dashboard", "label": "Dashboard", "icon": "home", "route": "/"},
        {"id": "catalog", "label": "Catalogo", "icon": "cube", "route": "/catalog"},
        {"id": "orders", "label": "Ordenes", "icon": "orders", "route": "/orders"},
        {"id": "messages", "label": "Mensajes", "icon": "messages", "route": "/messages"},
    ]},
    {"section": "Gestion", "items": [
        {"id": "branches", "label": "Sucursales", "icon": "branches", "route": "/branches"},
        {"id": "team", "label": "Equipo", "icon": "people", "route": "/team"},
        {"id": "notifications", "label": "Alertas", "icon": "bell", "route": "/notifications"},
        {"id": "settings", "label": "Ajustes", "icon": "settings", "route": "/settings"},
    ]},
    {"section": "Dev", "items": [
        {"id": "showcase", "label": "Componentes", "icon": "cube", "route": "/showcase"},
        {"id": "map", "label": "Mapa", "icon": "location", "route": "/map"},
    ]},
]

# ============================================================
#  HELPERS
# ============================================================

def _b(width: float, color: str) -> ft.border.Border:
    """Borde uniforme en los 4 lados. _b(1.0, C.BORDER)"""
    s = ft.border.BorderSide(width, color)
    return ft.border.Border(top=s, left=s, right=s, bottom=s)


def gradient_border(content: ft.Control, colors: list | None = None, width: float = 0.8, radius: float = 18, bgcolor: str = C.SURFACE, padding=None, expand: bool = False) -> ft.Container:
    colors = colors or C.GRADIENT_BORDER
    return ft.Container(
        gradient=ft.LinearGradient(
            colors=colors,
            begin=ft.alignment.Alignment(-1, -1),
            end=ft.alignment.Alignment(1, 1),
        ),
        border_radius=radius,
        padding=width,
        content=ft.Container(
            bgcolor=bgcolor,
            border_radius=radius - width,
            content=content,
            padding=padding,
            expand=expand,
        ),
        expand=expand,
    )


def pad(v=0, h=0, l=0, t=0, r=0, b=0):
    """Padding: pad(v=10, h=14) o pad(l=5, t=3, r=5, b=3)"""
    left = l or h; top_val = t or v; right = r or h; bottom = b or v
    return ft.padding.Padding(left=left, top=top_val, right=right, bottom=bottom)

CENT = ft.alignment.Alignment(0, 0)

def icon(name: str, size: int = 20, color: str = C.TEXT_MUTED) -> ft.Icon:
    """Icono Material. icon('home', size=20, color=C.TEXT_MUTED)"""
    return ft.Icon(I.get(name, IconEnum.CIRCLE), size=size, color=color)

def divider(color: str = C.BORDER) -> ft.Container:
    """Divisor sutil con padding horizontal."""
    return ft.Container(
        content=ft.Divider(color=color, height=1),
        padding=pad(h=SPACE_MD),
    )
