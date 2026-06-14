"""
ChatBubble — Burbuja de mensaje individual.
Variantes: enviado (right, verde) y recibido (left, surface).
Soporta texto, imagen adjunta, timestamp y estado de lectura.
"""
import flet as ft
from theme import C, F_BODY, F_MONO, F_CAPTION, RADIUS_LG, RADIUS_MD, SPACE_SM, SPACE_MD, pad, _b, icon


def chat_bubble(
    text: str,
    sent: bool = True,
    timestamp: str = "10:32 AM",
    read: bool = True,
    image_url: str = None,
) -> ft.Container:
    """Burbuja de chat individual.

    Args:
        text: Texto del mensaje
        sent: True = enviado (derecha, verde), False = recibido (izquierda)
        timestamp: Hora del mensaje
        read: Estado de lectura (doble check verde si True)
        image_url: URL de imagen adjunta (opcional)
    """
    bubble_bg = C.ACCENT_FAINT if sent else C.SURFACE
    border_color = C.ACCENT_DIM if sent else C.BORDER
    align = ft.MainAxisAlignment.END if sent else ft.MainAxisAlignment.START

    content_items = []

    if image_url:
        content_items.append(
            ft.Container(
                content=ft.Image(src=image_url, fit=ft.BoxFit.COVER),
                border_radius=RADIUS_MD,
                width=200,
                height=140,
            )
        )
        content_items.append(ft.Container(height=SPACE_SM))

    content_items.append(
        ft.Text(text, size=F_BODY, color=C.TEXT, selectable=True)
    )

    footer_items = [
        ft.Text(timestamp, size=F_MONO, color=C.TEXT_DIM),
    ]
    if sent:
        check_icon = icon("check", size=14, color=C.ACCENT if read else C.TEXT_DIM)
        footer_items.append(check_icon)
        if read:
            footer_items.append(icon("check", size=14, color=C.ACCENT))

    content_items.append(
        ft.Row(footer_items, spacing=4, alignment=ft.MainAxisAlignment.END)
    )

    return ft.Container(
        content=ft.Column(content_items, spacing=SPACE_SM, tight=True),
        bgcolor=bubble_bg,
        border=_b(1, border_color),
        border_radius=ft.border_radius.BorderRadius(
            top_left=RADIUS_LG,
            top_right=RADIUS_LG,
            bottom_left=RADIUS_LG if sent else 4,
            bottom_right=4 if sent else RADIUS_LG,
        ),
        padding=pad(v=10, h=SPACE_MD),
        width=280,
    )
