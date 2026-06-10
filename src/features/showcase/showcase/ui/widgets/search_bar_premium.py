"""
SearchBarPremium — Barra de busqueda estilizada con filtros y busquedas recientes.
"""
import flet as ft
from theme import C, F_BODY, F_CAPTION, F_LABEL, RADIUS_MD, RADIUS_PILL, SPACE_XS, SPACE_SM, SPACE_MD, pad, _b, gradient_border, icon


def search_bar_premium(
    placeholder: str = "Buscar productos, servicios...",
    recent_searches: list[str] = None,
    filters: list[str] = None,
) -> ft.Container:
    """Barra de busqueda premium con filtros y busquedas recientes.

    Args:
        placeholder: Texto placeholder del campo
        recent_searches: Lista de busquedas recientes (max 5)
        filters: Lista de filtros activos
    """
    if recent_searches is None:
        recent_searches = ["Audifonos bluetooth", "Camisetas", "Diseno grafico"]
    if filters is None:
        filters = ["Categoria", "Precio", "Ubicacion", "Rating"]

    content_items = []

    # Campo de busqueda
    search_field = ft.TextField(
        hint_text=placeholder,
        bgcolor=C.SURFACE,
        border_color="transparent",
        border_radius=RADIUS_MD,
        color=C.TEXT,
        text_size=F_BODY,
        cursor_color=C.GOLD,
        content_padding=pad(v=10, h=SPACE_MD),
        height=48,
        expand=True,
        prefix_icon=icon("search", size=18, color=C.TEXT_DIM).icon,
        suffix_icon=ft.IconButton(
            icon=icon("tune", size=18, color=C.GOLD).icon,
            icon_size=18, icon_color=C.GOLD,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=RADIUS_PILL)),
        ),
    )

    search_row = gradient_border(
        content=search_field,
        colors=[C.BORDER, C.GOLD_DIM, C.GREEN_DIM, C.BORDER],
        width=1.0,
        radius=RADIUS_MD + 1,
        bgcolor=C.SURFACE,
        padding=0,
    )
    content_items.append(search_row)

    # Chips de filtros
    content_items.append(ft.Container(height=SPACE_SM))
    filter_chips = [
        ft.Container(
            content=ft.Row(
                [
                    ft.Text(f, size=F_CAPTION, color=C.TEXT_MUTED),
                    icon("chevron_down", size=12, color=C.TEXT_DIM),
                ],
                spacing=SPACE_XS,
            ),
            bgcolor=C.SURFACE2,
            border=_b(1, C.BORDER),
            border_radius=RADIUS_PILL,
            padding=pad(v=4, h=SPACE_SM),
            ink=True,
        )
        for f in filters
    ]
    content_items.append(
        ft.Row(filter_chips, spacing=SPACE_SM, scroll=ft.ScrollMode.AUTO)
    )

    # Busquedas recientes
    if recent_searches:
        content_items.append(ft.Container(height=SPACE_MD))
        content_items.append(
            ft.Text("BUSQUEDAS RECIENTES", size=F_LABEL, color=C.TEXT_DIM,
                    weight="bold", font_family="monospace")
        )
        content_items.append(ft.Container(height=SPACE_SM))

        recent_items = []
        for term in recent_searches:
            recent_items.append(
                ft.Container(
                    content=ft.Row(
                        [
                            icon("history", size=14, color=C.TEXT_DIM),
                            ft.Text(term, size=F_CAPTION, color=C.TEXT_MUTED),
                        ],
                        spacing=SPACE_SM,
                    ),
                    padding=pad(v=SPACE_SM, h=0),
                    ink=True,
                )
            )
        content_items.append(
            ft.Column(recent_items, spacing=SPACE_XS)
        )

    return ft.Container(
        content=ft.Column(content_items, spacing=0, tight=True),
        padding=pad(v=SPACE_SM, h=0),
    )
