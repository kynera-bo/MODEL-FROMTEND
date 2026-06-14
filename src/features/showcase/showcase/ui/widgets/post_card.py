"""
PostCard — Publicacion estilo red social.
Header de usuario, contenido texto, imagen, barra de acciones, likes.
"""
import flet as ft
from theme import C, F_H3, F_BODY, F_CAPTION, RADIUS_XL, RADIUS_LG, RADIUS_PILL, SPACE_XS, SPACE_SM, SPACE_MD, SPACE_LG, pad, _b, icon, CENT


def post_card(
    username: str = "maria.lopez",
    display_name: str = "Maria Lopez",
    avatar_initials: str = "ML",
    timestamp: str = "2 horas",
    content: str = "Acabo de descubrir este marketplace increible! Los productos son de primera calidad y la experiencia de compra es simplemente genial.",
    image_url: str | None = None,
    likes_count: int = 2847,
    liked: bool = False,
) -> ft.Container:
    """Publicacion completa estilo Instagram/Facebook.

    Args:
        username: @ del usuario
        display_name: Nombre visible
        avatar_initials: Iniciales del avatar
        timestamp: Tiempo relativo
        content: Texto de la publicacion
        image_url: Imagen adjunta (opcional)
        likes_count: Cantidad de likes
        liked: Si el usuario actual dio like
    """
    avatar = ft.Container(
        content=ft.Text(
            avatar_initials.upper(), size=F_CAPTION, weight="bold",
            color=C.TEXT, text_align=ft.TextAlign.CENTER,
        ),
        width=40, height=40, border_radius=20,
        bgcolor=C.AVATAR_BG,
        alignment=CENT,
    )

    header = ft.Row(
        [
            avatar,
            ft.Column(
                [
                    ft.Text(display_name, size=F_H3, weight="bold", color=C.TEXT),
                    ft.Text(f"@{username} · {timestamp}", size=F_CAPTION, color=C.TEXT_DIM),
                ],
                spacing=0,
            ),
        ],
        spacing=SPACE_SM,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    content_items = [header]

    content_items.append(ft.Container(height=SPACE_MD))
    content_items.append(
        ft.Text(content, size=F_BODY, color=C.TEXT_MUTED)
    )

    if image_url:
        content_items.append(ft.Container(height=SPACE_MD))
        content_items.append(
            ft.Container(
                content=ft.Image(src=image_url, fit=ft.BoxFit.COVER),
                border_radius=RADIUS_LG,
                border=_b(1, C.BORDER),
                height=280,
            )
        )

    content_items.append(ft.Container(height=SPACE_LG))

    # Barra de acciones: like, comment, share, bookmark
    heart_icon_name = "favorite" if liked else "favorite_border"
    heart_color = C.ERROR if liked else C.TEXT_MUTED

    actions = ft.Row(
        [
            ft.IconButton(
                icon=icon(heart_icon_name, size=22, color=heart_color).icon,
                icon_size=22, icon_color=heart_color,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=RADIUS_PILL)),
            ),
            ft.IconButton(
                icon=icon("chat", size=20, color=C.TEXT_MUTED).icon,
                icon_size=20, icon_color=C.TEXT_MUTED,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=RADIUS_PILL)),
            ),
            ft.IconButton(
                icon=icon("send", size=20, color=C.TEXT_MUTED).icon,
                icon_size=20, icon_color=C.TEXT_MUTED,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=RADIUS_PILL)),
            ),
            ft.Container(expand=True),
            ft.IconButton(
                icon=icon("bookmark_border", size=20, color=C.TEXT_MUTED).icon,
                icon_size=20, icon_color=C.TEXT_MUTED,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=RADIUS_PILL)),
            ),
        ],
        spacing=0,
    )

    content_items.append(actions)
    content_items.append(ft.Container(height=SPACE_SM))

    likes_text = ft.Text(
        f"{likes_count:,} Me gusta".replace(",", "."),
        size=F_CAPTION, weight="bold", color=C.TEXT,
    )
    content_items.append(likes_text)

    content_items.append(ft.Container(height=SPACE_XS))

    caption_text = content[:60] + "..." if len(content) > 60 else content
    caption = ft.Text(
        spans=[
            ft.TextSpan(
                display_name,
                style=ft.TextStyle(size=F_CAPTION, weight="bold", color=C.TEXT),
            ),
            ft.TextSpan(
                f" {caption_text}",
                style=ft.TextStyle(size=F_CAPTION, color=C.TEXT_MUTED),
            ),
        ],
    )
    content_items.append(caption)

    content_items.append(ft.Container(height=SPACE_SM))
    content_items.append(
        ft.Text(
            "Ver los 42 comentarios",
            size=F_CAPTION, color=C.TEXT_DIM,
        )
    )

    return ft.Container(
        content=ft.Column(content_items, spacing=0),
        bgcolor=C.SURFACE,
        border=_b(1, C.BORDER),
        border_radius=RADIUS_XL,
        padding=pad(v=SPACE_MD, h=SPACE_LG),
        expand=True,
    )
