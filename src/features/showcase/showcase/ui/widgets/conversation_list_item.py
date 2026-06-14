"""
ConversationListItem — Preview de conversacion estilo WhatsApp/Instagram.
Avatar con indicador online, nombre, ultimo mensaje, timestamp, badge no leidos.
"""
import flet as ft
from theme import C, F_BODY, F_CAPTION, F_MONO, F_LABEL, RADIUS_PILL, RADIUS_MD, SPACE_XS, SPACE_SM, SPACE_MD, pad, _b, icon, CENT


def conversation_list_item(
    avatar_initials: str = "M",
    name: str = "Maria Lopez",
    last_message: str = "Hola, como estas? Nos vemos manana...",
    timestamp: str = "10:32",
    unread_count: int = 0,
    online: bool = True,
    is_active: bool = False,
) -> ft.Container:
    """Preview de una conversacion en la lista de chats.

    Args:
        avatar_initials: Iniciales del avatar (1-2 chars)
        name: Nombre del contacto
        last_message: Preview del ultimo mensaje (se trunca)
        timestamp: Hora del ultimo mensaje
        unread_count: Cantidad de mensajes no leidos (0 = sin badge)
        online: Muestra dot verde de online
        is_active: Fondo activo para la conversacion seleccionada
    """
    online_dot = ft.Container(
        width=10, height=10,
        border_radius=5,
        bgcolor=C.ACCENT if online else C.TEXT_DIM,
        border=_b(2, C.BG),
        offset=ft.Offset(0.9, 0.9),
    ) if online else None

    avatar = ft.Stack(
        [
            ft.Container(
                content=ft.Text(
                    avatar_initials.upper(), size=F_BODY, weight="bold",
                    color=C.TEXT, text_align=ft.TextAlign.CENTER,
                ),
                width=48, height=48,
                border_radius=24,
                bgcolor=C.AVATAR_BG,
                border=_b(1.5, C.ACCENT_DIM if online else C.BORDER),
                alignment=CENT,
            ),
            online_dot or ft.Container(),
        ],
        width=48, height=48,
    )

    truncated_msg = last_message[:35] + "..." if len(last_message) > 35 else last_message

    text_col = ft.Column(
        [
            ft.Text(name, size=F_BODY, weight="bold", color=C.TEXT,
                    overflow=ft.TextOverflow.ELLIPSIS),
            ft.Text(truncated_msg, size=F_CAPTION, color=C.TEXT_MUTED,
                    overflow=ft.TextOverflow.ELLIPSIS),
        ],
        spacing=SPACE_XS, expand=True,
    )

    right_col_items = [
        ft.Text(timestamp, size=F_MONO, color=C.TEXT_DIM),
    ]
    if unread_count > 0:
        right_col_items.append(
            ft.Container(
                content=ft.Text(
                    str(unread_count) if unread_count < 100 else "99+",
                    size=F_LABEL, color=C.BG, weight="bold",
                    text_align=ft.TextAlign.CENTER,
                ),
                bgcolor=C.ERROR,
                border_radius=RADIUS_PILL,
                padding=pad(v=2, h=6),
            )
        )

    right_col = ft.Column(
        right_col_items,
        spacing=SPACE_XS,
        horizontal_alignment=ft.CrossAxisAlignment.END,
    )

    row = ft.Row(
        [avatar, text_col, right_col],
        spacing=SPACE_MD,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return ft.Container(
        content=row,
        bgcolor=C.ITEM_ACTIVE_BG if is_active else None,
        border_radius=RADIUS_MD,
        padding=pad(v=SPACE_SM, h=SPACE_MD),
        ink=True,
    )
