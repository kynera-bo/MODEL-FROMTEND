"""
Design Tokens — Aura frontend v3.
Paleta tricolor boliviano (verde/gold/rojo) + premium dark.
Cada color tiene proposito semantico. NUNCA usar colores fuera de este archivo.
"""
import flet as ft
from flet.controls.material.icons import Icons as IconEnum

# ============================================================
#  COLORES — Premium Dark con acentos Bolivia
#  Regla: verde=exito, gold=destacado, rojo=peligro.
#         Blancos/grises para texto. NUNCA intercambiar.
# ============================================================

class C:
    # Fondos — jerarquia clara (de oscuro a claro)
    BG          = "#080504"              # pagina (warm black, ligerisimo tinte rojizo)
    SURFACE     = "#11100e"              # cards, inputs, paneles
    SURFACE2    = "#1a1816"              # hover de cards, superficies secundarias
    SHELL_BG    = "#080504"              # contenedor desktop (mismo que BG — el mas oscuro)
    POPUP_BG    = "#141210"              # fondo popup/sheet
    OVERLAY     = "#CC000000"            # backdrop oscuro (#000000cc)

    # Component backgrounds (reemplazan los rgba hardcodeados)
    SIDEBAR_BG     = "#E60F0E0C"         # Sidebar (rgba(15,14,12,0.9))
    TABBAR_BG      = "#F0121212"         # Tabbar (rgba(18,18,18,0.94))
    AVATAR_BG      = "#14FFFFFF"         # Contenedor avatar iniciales (rgba(255,255,255,0.08))
    AVATAR_BG2     = "#1AFFFFFF"         # Contenedor avatar activo (rgba(255,255,255,0.1))
    ITEM_ACTIVE_BG = "#0AFFFFFF"         # Elemento activo lista (rgba(255,255,255,0.04))
    DRAG_HANDLE_BG = "#26FFFFFF"         # Drag handle (rgba(255,255,255,0.15))

    # Bordes — de alta gama (blanco/plata brillante, contenedores oro y hover verde)
    BORDER        = "#D9F0F0F0"          # blanco plata brillante y definido (rgba(240,240,240,0.85))
    BORDER_HOVER  = "#F28CC878"          # verde vibrante para hover/enfoque (rgba(140,200,120,0.95))
    BORDER_STRONG = "#E6E1BE64"          # oro boliviano brillante para contenedores principales (rgba(225,190,100,0.90))

    # Texto — contraste limpio
    TEXT        = "#F0F0F0"              # headings, texto principal
    TEXT_MUTED  = "#B0B0B0"              # parrafos, descripciones
    TEXT_DIM    = "#6A6A6A"              # labels, metadata
    TEXT_DIM2   = "#40FFFFFF"            # texto secundario atenuado (rgba(255,255,255,0.25))

    # Verde — EXITO, ACTIVO, CONFIRMAR, CHECK, ONLINE
    GREEN       = "#CC8CC878"            # (rgba(140,200,120,0.80))
    GREEN_DIM   = "#4D8CC878"            # (rgba(140,200,120,0.30))
    GREEN_FAINT = "#148CC878"            # (rgba(140,200,120,0.08))
    GREEN_BG    = "#1F8CC878"            # (rgba(140,200,120,0.12))

    # Gold — PREMIUM, DESTACADO, HOVER, MONEDA
    GOLD        = "#E6E1BE64"            # (rgba(225,190,100,0.90))
    GOLD_DIM    = "#73E1BE64"            # (rgba(225,190,100,0.45))
    GOLD_FAINT  = "#1FE1BE64"            # (rgba(225,190,100,0.12))
    GOLD_BG     = "#14E1BE64"            # (rgba(225,190,100,0.08))

    # Rojo — PELIGRO, CANCELAR, ERROR, ALERTA
    RED         = "#BFDC8C78"            # (rgba(220,140,120,0.75))
    RED_DIM     = "#40DC8C78"            # (rgba(220,140,120,0.25))
    RED_FAINT   = "#14DC8C78"            # (rgba(220,140,120,0.08))
    RED_BG      = "#0FDC8C78"            # (rgba(220,140,120,0.06))

    # Acentos para Dashboard
    BLUE        = "#64B5F6"
    PURPLE      = "#CE93D8"

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
    "home": IconEnum.HOME, "search": IconEnum.SEARCH,
    "chat": IconEnum.CHAT_BUBBLE, "bell": IconEnum.NOTIFICATIONS,
    "person": IconEnum.PERSON, "trophy": IconEnum.EMOJI_EVENTS,
    "people": IconEnum.GROUP, "settings": IconEnum.SETTINGS,
    "cube": IconEnum.INVENTORY_2, "receipt": IconEnum.RECEIPT,
    "location": IconEnum.LOCATION_ON, "add": IconEnum.ADD,
    "logout": IconEnum.LOGOUT, "check": IconEnum.CHECK,
    "chevron_down": IconEnum.KEYBOARD_ARROW_DOWN,
    "chevron_up": IconEnum.KEYBOARD_ARROW_UP,
    "sparkles": IconEnum.AUTO_AWESOME,
    "notifications": IconEnum.NOTIFICATIONS,
    "messages": IconEnum.CHAT_BUBBLE,
    "branches": IconEnum.ACCOUNT_TREE,
    "orders": IconEnum.SHOPPING_CART,
    "explore": IconEnum.EXPLORE,
    "gamification": IconEnum.EMOJI_EVENTS,
    "social": IconEnum.GROUP,
    "profile_menu": IconEnum.PERSON,
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


def gradient_border(content: ft.Control, colors: list, width: float = 0.8, radius: float = 18, bgcolor: str = C.SURFACE, padding=None, expand: bool = False) -> ft.Container:
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
    """Icono Material. icon('home', size=20, color=C.GREEN)"""
    return ft.Icon(I.get(name, IconEnum.CIRCLE), size=size, color=color)

def divider(color: str = C.BORDER) -> ft.Container:
    """Divisor sutil con padding horizontal."""
    return ft.Container(
        content=ft.Divider(color=color, height=1),
        padding=pad(h=SPACE_MD),
    )
