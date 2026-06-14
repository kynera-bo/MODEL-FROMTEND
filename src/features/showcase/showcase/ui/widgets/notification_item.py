"""
NotificationItem — Componente de notificacion con 5 variantes.
Mensaje, evento, tarea, actividad, sistema.
Cada una con icono, color acento, titulo, descripcion, timestamp y estado leido.
"""
import flet as ft
from theme import C, F_CAPTION, F_BODY, F_MONO, RADIUS_MD, RADIUS_PILL, SPACE_SM, SPACE_MD, SPACE_LG, pad, _b, icon, CENT


NOTIFICATION_TYPES = {
    "message": {
        "icon": "chat",
        "color": C.ACCENT,
        "bg": C.ACCENT_FAINT,
        "label": "Mensaje",
    },
    "event": {
        "icon": "event",
        "color": C.ACCENT,
        "bg": C.ACCENT_FAINT,
        "label": "Evento",
    },
    "task": {
        "icon": "check_circle",
        "color": C.ACCENT,
        "bg": "#1ACE93D8",
        "label": "Tarea",
    },
    "activity": {
        "icon": "trending_up",
        "color": C.ACCENT,
        "bg": "#1A64B5F6",
        "label": "Actividad",
    },
    "system": {
        "icon": "info",
        "color": C.ERROR,
        "bg": C.ERROR_BG,
        "label": "Sistema",
    },
}


def notification_item(
    notif_type: str = "message",
    title: str = "Nuevo mensaje",
    description: str = "Maria te envio un mensaje",
    timestamp: str = "ahora",
    unread: bool = True,
    action_label: str = None,
) -> ft.Container:
    """Item de notificacion con variante segun tipo.

    Args:
        notif_type: "message" | "event" | "task" | "activity" | "system"
        title: Titulo de la notificacion
        description: Descripcion corta
        timestamp: Tiempo relativo
        unread: Muestra dot azul de no leido
        action_label: Texto del boton de accion (opcional, ej: "Ver")
    """
    cfg = NOTIFICATION_TYPES.get(notif_type, NOTIFICATION_TYPES["message"])
    icon_color = cfg["color"]
    icon_bg = cfg["bg"]

    icon_circle = ft.Container(
        content=icon(cfg["icon"], size=16, color=icon_color),
        width=36, height=36, border_radius=18,
        bgcolor=icon_bg,
        alignment=CENT,
    )

    text_col = ft.Column(
        [
            ft.Row(
                [
                    ft.Text(title, size=F_BODY, weight="bold", color=C.TEXT),
                    ft.Container(width=SPACE_SM),
                    ft.Text(cfg["label"], size=F_MONO, color=icon_color,
                            weight="bold", font_family="monospace"),
                ],
                spacing=0,
            ),
            ft.Text(description, size=F_CAPTION, color=C.TEXT_MUTED),
            ft.Row(
                [
                    ft.Text(timestamp, size=F_MONO, color=C.TEXT_DIM),
                ] + ([
                    ft.Container(width=SPACE_LG),
                    ft.TextButton(
                        content=ft.Text(action_label, size=F_CAPTION, weight="bold"),
                        style=ft.ButtonStyle(
                            color=C.ACCENT,
                            padding=pad(v=2, h=SPACE_SM),
                            shape=ft.RoundedRectangleBorder(radius=RADIUS_MD),
                        ),
                    ),
                ] if action_label else []),
                spacing=0,
            ),
        ],
        spacing=2,
        expand=True,
    )

    unread_dot = ft.Container(
        width=8, height=8, border_radius=4,
        bgcolor=C.ACCENT,
    ) if unread else ft.Container(width=8, height=8)

    row = ft.Row(
        [icon_circle, text_col, unread_dot],
        spacing=SPACE_MD,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    return ft.Container(
        content=row,
        bgcolor=C.ITEM_ACTIVE_BG if unread else None,
        border_radius=RADIUS_MD,
        padding=pad(v=SPACE_SM, h=SPACE_MD),
        ink=True,
    )
