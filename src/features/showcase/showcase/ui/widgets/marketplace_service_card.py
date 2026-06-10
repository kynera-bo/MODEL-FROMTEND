"""
MarketplaceServiceCard — Card de servicio con icono, descripcion, tags, precio y disponibilidad.
"""
import flet as ft
from theme import C, F_H3, F_BODY, F_CAPTION, F_LABEL, RADIUS_XL, RADIUS_MD, RADIUS_PILL, SPACE_XS, SPACE_SM, SPACE_MD, SPACE_LG, pad, _b, icon, CENT


def marketplace_service_card(
    title: str = "Diseno Grafico Profesional",
    description: str = "Logos, branding, social media y mas. Resultados profesionales en 48h.",
    icon_name: str = "brush",
    tags: list[str] = None,
    price_label: str = "Desde $50/h",
    available: bool = True,
    provider_name: str = "Ana Martinez",
    provider_initials: str = "AM",
    rating: float = 4.9,
) -> ft.Container:
    """Card de servicio para marketplace.

    Args:
        title: Nombre del servicio
        description: Descripcion corta
        icon_name: Nombre del icono Material representativo
        tags: Lista de etiquetas (badges)
        price_label: Texto de precio ("Desde $X" o "$X fijo")
        available: Disponibilidad actual
        provider_name: Nombre del proveedor
        provider_initials: Iniciales del proveedor
        rating: Puntuacion
    """
    if tags is None:
        tags = ["Branding", "Social Media", "Logos"]

    content_items = []

    # Icono grande representativo
    icon_circle = ft.Container(
        content=icon(icon_name, size=32, color=C.GOLD),
        width=64, height=64, border_radius=32,
        bgcolor=C.GOLD_FAINT,
        border=_b(1.5, C.GOLD_DIM),
        alignment=CENT,
    )
    content_items.append(icon_circle)
    content_items.append(ft.Container(height=SPACE_MD))

    # Titulo y descripcion
    content_items.append(
        ft.Text(title, size=F_H3, weight="bold", color=C.TEXT)
    )
    content_items.append(ft.Container(height=SPACE_XS))
    content_items.append(
        ft.Text(description, size=F_CAPTION, color=C.TEXT_MUTED, max_lines=2,
                overflow=ft.TextOverflow.ELLIPSIS)
    )

    # Tags
    content_items.append(ft.Container(height=SPACE_MD))
    tag_chips = [
        ft.Container(
            content=ft.Text(tag.upper(), size=F_LABEL, color=C.GREEN,
                            weight="bold", font_family="monospace"),
            bgcolor=C.GREEN_FAINT,
            border_radius=RADIUS_PILL,
            padding=pad(v=2, h=SPACE_SM),
        )
        for tag in tags
    ]
    content_items.append(
        ft.Row(tag_chips, spacing=SPACE_SM, wrap=True, run_spacing=SPACE_SM)
    )

    # Precio
    content_items.append(ft.Container(height=SPACE_MD))
    content_items.append(
        ft.Text(price_label, size=F_H3, weight="bold", color=C.GOLD)
    )

    # Disponibilidad + proveedor
    content_items.append(ft.Container(height=SPACE_MD))
    avail_dot = ft.Container(
        width=6, height=6, border_radius=3,
        bgcolor=C.GREEN if available else C.RED,
    )
    avail_text = "Disponible ahora" if available else "No disponible"
    avail_color = C.GREEN if available else C.RED_DIM

    provider_avatar = ft.Container(
        content=ft.Text(
            provider_initials.upper(), size=F_LABEL, weight="bold",
            color=C.TEXT, text_align=ft.TextAlign.CENTER,
        ),
        width=24, height=24, border_radius=12,
        bgcolor=C.AVATAR_BG,
        alignment=CENT,
    )

    footer_row = ft.Row(
        [
            ft.Row([avail_dot, ft.Text(avail_text, size=F_CAPTION, color=avail_color)], spacing=SPACE_XS),
            ft.Container(expand=True),
            ft.Row(
                [
                    provider_avatar,
                    ft.Text(provider_name, size=F_CAPTION, color=C.TEXT_MUTED),
                    ft.Text(f"· {rating}", size=F_CAPTION, color=C.GOLD),
                ],
                spacing=SPACE_XS,
            ),
        ],
        spacing=SPACE_SM,
    )
    content_items.append(footer_row)

    # Boton de accion
    content_items.append(ft.Container(height=SPACE_LG))
    content_items.append(
        ft.ElevatedButton(
            content=ft.Text("Reservar ahora", size=F_BODY, weight="bold"),
            bgcolor=C.GOLD, color=C.BG,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=RADIUS_MD),
                padding=pad(v=10, h=SPACE_LG),
            ),
        )
    )

    return ft.Container(
        content=ft.Column(content_items, spacing=0, tight=True),
        bgcolor=C.SURFACE,
        border=_b(1, C.BORDER_STRONG),
        border_radius=RADIUS_XL,
        padding=pad(v=SPACE_LG, h=SPACE_LG),
        width=340,
        ink=True,
    )
