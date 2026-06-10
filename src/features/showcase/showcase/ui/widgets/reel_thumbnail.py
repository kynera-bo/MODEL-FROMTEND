"""
ReelThumbnail — Thumbnail de video corto vertical 9:16.
Overlay gradiente, views count, duracion badge.
"""
import flet as ft
from theme import C, F_CAPTION, F_LABEL, RADIUS_LG, RADIUS_PILL, SPACE_SM, SPACE_XS, pad, icon, CENT


def reel_thumbnail(
    video_title: str = "Mi nuevo producto favorito",
    views: int = 45200,
    duration: str = "0:32",
    thumbnail_color: str = C.SURFACE2,
) -> ft.Container:
    """Thumbnail de reel/short estilo TikTok/Instagram.

    Args:
        video_title: Titulo del video
        views: Cantidad de visualizaciones
        duration: Duracion en formato M:SS
        thumbnail_color: Color de fondo si no hay imagen
    """
    aspect_ratio = 9 / 16
    width = 180
    height = width / aspect_ratio

    # Badge de duracion
    duration_badge = ft.Container(
        content=ft.Text(duration, size=F_LABEL, color=C.TEXT, weight="bold",
                        font_family="monospace"),
        bgcolor="#99000000",
        border_radius=RADIUS_PILL,
        padding=pad(v=2, h=SPACE_SM),
        right=8, bottom=8,
    )

    # Overlay gradiente inferior
    overlay = ft.Container(
        gradient=ft.LinearGradient(
            colors=["transparent", "#99000000"],
            begin=ft.alignment.Alignment(0, 0),
            end=ft.alignment.Alignment(0, 1),
        ),
        border_radius=RADIUS_LG,
        height=height,
        width=width,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
    )

    # Contenido sobre el overlay
    overlay_content = ft.Container(
        content=ft.Column(
            [
                ft.Container(expand=True),
                ft.Row(
                    [
                        icon("play_arrow", size=12, color=C.TEXT),
                        ft.Text(
                            _format_views(views), size=F_CAPTION, color=C.TEXT,
                            weight="bold",
                        ),
                    ],
                    spacing=SPACE_XS,
                ),
                ft.Text(
                    video_title, size=F_CAPTION, color=C.TEXT,
                    max_lines=1, overflow=ft.TextOverflow.ELLIPSIS,
                ),
            ],
            spacing=SPACE_SM,
        ),
        padding=pad(v=SPACE_SM, h=SPACE_SM),
        height=height,
        width=width,
    )

    thumbnail = ft.Stack(
        [
            ft.Container(
                bgcolor=thumbnail_color,
                border_radius=RADIUS_LG,
                width=width,
                height=height,
                alignment=CENT,
                content=icon("play_circle_filled", size=40, color=C.TEXT_DIM),
            ),
            overlay,
            overlay_content,
            duration_badge,
        ],
        width=width,
        height=height,
    )

    return ft.Container(
        content=thumbnail,
        border_radius=RADIUS_LG,
        ink=True,
    )


def _format_views(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)
