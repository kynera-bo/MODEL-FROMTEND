"""
MarketplaceBarterCard — Card de trueque: Ofrezco <-> Busco.
Layout de dos columnas con items, flecha central y estado del intercambio.
"""
import flet as ft
from theme import C, F_BODY, F_CAPTION, F_LABEL, F_MONO, RADIUS_XL, RADIUS_LG, RADIUS_MD, RADIUS_PILL, SPACE_XS, SPACE_SM, SPACE_MD, SPACE_LG, pad, _b, icon, CENT


BARTER_STATUS = {
    "open": ("ABIERTO", C.GREEN, C.GREEN_FAINT),
    "negotiating": ("NEGOCIANDO", C.GOLD, C.GOLD_FAINT),
    "closed": ("CERRADO", C.TEXT_DIM, C.SURFACE2),
}


def marketplace_barter_card(
    offer_item: str = "iPhone 13 128GB",
    offer_category: str = "Tecnologia",
    seek_item: str = "MacBook Air",
    seek_category: str = "Computadoras",
    status: str = "open",
    match_percent: int = 85,
    username: str = "carlos.dev",
    user_initials: str = "CD",
    timestamp: str = "hace 3h",
) -> ft.Container:
    """Card de trueque para marketplace.

    Args:
        offer_item: Que ofrece el usuario
        offer_category: Categoria de lo ofrecido
        seek_item: Que busca a cambio
        seek_category: Categoria de lo buscado
        status: "open" | "negotiating" | "closed"
        match_percent: Porcentaje de compatibilidad (0-100)
        username: Nombre del usuario publicante
        user_initials: Iniciales del usuario
        timestamp: Tiempo relativo
    """
    status_label, status_color, status_bg = BARTER_STATUS.get(
        status, BARTER_STATUS["open"]
    )

    content_items = []

    # Header: usuario + timestamp + status badge
    user_avatar = ft.Container(
        content=ft.Text(
            user_initials.upper(), size=F_LABEL, weight="bold",
            color=C.TEXT, text_align=ft.TextAlign.CENTER,
        ),
        width=28, height=28, border_radius=14,
        bgcolor=C.AVATAR_BG,
        alignment=CENT,
    )

    status_badge = ft.Container(
        content=ft.Text(status_label, size=F_LABEL, color=status_color,
                        weight="bold", font_family="monospace"),
        bgcolor=status_bg,
        border_radius=RADIUS_PILL,
        padding=pad(v=3, h=SPACE_SM),
    )

    header_row = ft.Row(
        [
            user_avatar,
            ft.Column(
                [
                    ft.Text(username, size=F_CAPTION, weight="bold", color=C.TEXT),
                    ft.Text(timestamp, size=F_MONO, color=C.TEXT_DIM),
                ],
                spacing=0,
            ),
            ft.Container(expand=True),
            status_badge,
        ],
        spacing=SPACE_SM,
    )
    content_items.append(header_row)
    content_items.append(ft.Container(height=SPACE_LG))

    # Cuerpo: Ofrezco <-> Busco
    offer_col = _barter_side(
        label="OFREZCO",
        item_name=offer_item,
        category=offer_category,
        accent_color=C.GREEN,
        accent_bg=C.GREEN_FAINT,
    )

    seek_col = _barter_side(
        label="BUSCO",
        item_name=seek_item,
        category=seek_category,
        accent_color=C.GOLD,
        accent_bg=C.GOLD_FAINT,
    )

    swap_icon = ft.Container(
        content=icon("swap_horiz", size=18, color=C.GOLD),
        width=36, height=36, border_radius=18,
        bgcolor=C.GOLD_BG,
        border=_b(1, C.GOLD_DIM),
        alignment=CENT,
    )

    barter_row = ft.Row(
        [offer_col, swap_icon, seek_col],
        spacing=SPACE_SM,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )
    content_items.append(barter_row)

    # Footer: match %
    content_items.append(ft.Container(height=SPACE_MD))
    match_color = C.GREEN if match_percent >= 70 else C.GOLD if match_percent >= 40 else C.RED
    match_badge = ft.Container(
        content=ft.Text(
            f"Match {match_percent}%",
            size=F_LABEL, color=match_color, weight="bold",
            font_family="monospace",
        ),
        bgcolor=C.PURPLE + "1A" if "1A" not in C.PURPLE else "#1ACE93D8",
        border_radius=RADIUS_PILL,
        padding=pad(v=3, h=SPACE_SM),
    )

    content_items.append(
        ft.Row([match_badge, ft.Container(expand=True)], spacing=0)
    )

    return ft.Container(
        content=ft.Column(content_items, spacing=0, tight=True),
        bgcolor=C.SURFACE,
        border=_b(1, C.BORDER),
        border_radius=RADIUS_XL,
        padding=pad(v=SPACE_LG, h=SPACE_LG),
        width=380,
        ink=True,
    )


def _barter_side(label: str, item_name: str, category: str,
                 accent_color: str, accent_bg: str) -> ft.Column:
    """Construye un lado del trueque (Ofrezco o Busco)."""
    return ft.Column(
        [
            ft.Text(label, size=F_LABEL, color=C.TEXT_DIM, weight="bold",
                    font_family="monospace"),
            ft.Container(height=SPACE_XS),
            ft.Text(item_name, size=F_BODY, weight="bold", color=C.TEXT,
                    max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
            ft.Container(height=SPACE_XS),
            ft.Container(
                content=ft.Text(category.upper(), size=F_LABEL, color=accent_color,
                                weight="bold", font_family="monospace"),
                bgcolor=accent_bg,
                border_radius=RADIUS_PILL,
                padding=pad(v=2, h=SPACE_SM),
            ),
        ],
        spacing=0,
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
