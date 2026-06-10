"""
WishlistHeart — Boton de favorito animado con transicion outline a relleno.
"""
import flet as ft
from theme import C, F_CAPTION, RADIUS_PILL, SPACE_XS, pad, icon, CENT


def wishlist_heart(
    liked: bool = False,
    count: int = 128,
    size: int = 36,
) -> ft.Container:
    """Boton de favorito con contador.

    Args:
        liked: Estado actual del corazon
        count: Cantidad de favoritos
        size: Tamaño del icono
    """
    heart_color = C.RED if liked else C.TEXT_MUTED
    heart_icon_name = "favorite" if liked else "favorite_border"

    heart = ft.IconButton(
        icon=icon(heart_icon_name, size=size, color=heart_color).icon,
        icon_size=size, icon_color=heart_color,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=RADIUS_PILL),
            bgcolor=C.RED_FAINT if liked else None,
        ),
    )

    count_text = ft.Text(
        str(count), size=F_CAPTION, color=C.RED if liked else C.TEXT_MUTED,
        weight="bold",
    )

    return ft.Container(
        content=ft.Row(
            [heart, count_text],
            spacing=SPACE_XS,
        ),
        padding=pad(v=2, h=4),
        border_radius=RADIUS_PILL,
        ink=True,
    )
