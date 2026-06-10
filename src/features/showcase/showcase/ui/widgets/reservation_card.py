"""
ReservationCard — Card de reserva con fecha destacada, estado y acciones.
"""
import flet as ft
from theme import C, F_H1, F_H3, F_BODY, F_CAPTION, F_LABEL, F_MONO, RADIUS_XL, RADIUS_LG, RADIUS_MD, RADIUS_PILL, SPACE_XS, SPACE_SM, SPACE_MD, SPACE_LG, pad, _b, icon, CENT


RESERVATION_STATUS = {
    "confirmed": ("CONFIRMADA", C.GREEN, C.GREEN_FAINT, "check"),
    "pending": ("PENDIENTE", C.GOLD, C.GOLD_FAINT, "schedule"),
    "cancelled": ("CANCELADA", C.RED, C.RED_FAINT, "close"),
}


def reservation_card(
    service_name: str = "Masaje Relajante 60min",
    provider_name: str = "Spa Serenidad",
    provider_initials: str = "SS",
    rating: float = 4.7,
    day: str = "15",
    month: str = "JUN",
    year: str = "2026",
    time: str = "3:00 PM",
    duration: str = "1h",
    location: str = "Av. Principal 123, La Paz",
    status: str = "confirmed",
    price: str = "Bs. 180",
) -> ft.Container:
    """Card de reserva con fecha destacada y estado.

    Args:
        service_name: Nombre del servicio reservado
        provider_name: Nombre del proveedor
        provider_initials: Iniciales del proveedor
        rating: Puntuacion
        day: Dia numerico
        month: Mes abreviado (3 letras)
        year: Ano
        time: Hora de la reserva
        duration: Duracion estimada
        location: Direccion o lugar
        status: "confirmed" | "pending" | "cancelled"
        price: Precio de la reserva
    """
    status_label, status_color, status_bg, status_icon = RESERVATION_STATUS.get(
        status, RESERVATION_STATUS["pending"]
    )

    content_items = []

    # Top row: fecha destacada + info principal
    date_block = ft.Container(
        content=ft.Column(
            [
                ft.Text(day, size=F_H1, weight="bold", color=C.GOLD, text_align=ft.TextAlign.CENTER),
                ft.Text(month.upper(), size=F_LABEL, color=C.TEXT_DIM, weight="bold",
                        font_family="monospace", text_align=ft.TextAlign.CENTER),
                ft.Text(year, size=F_MONO, color=C.TEXT_DIM, text_align=ft.TextAlign.CENTER),
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        width=56, height=80,
        bgcolor=C.GOLD_FAINT,
        border_radius=RADIUS_MD,
        border=_b(1, C.GOLD_DIM),
        alignment=CENT,
        padding=pad(v=SPACE_SM, h=SPACE_XS),
    )

    status_badge = ft.Container(
        content=ft.Row(
            [
                icon(status_icon, size=10, color=status_color),
                ft.Text(status_label, size=F_LABEL, color=status_color,
                        weight="bold", font_family="monospace"),
            ],
            spacing=SPACE_XS,
        ),
        bgcolor=status_bg,
        border_radius=RADIUS_PILL,
        padding=pad(v=3, h=SPACE_SM),
    )

    info_col = ft.Column(
        [
            ft.Text(service_name, size=F_H3, weight="bold", color=C.TEXT),
            ft.Text(f"{time} · {duration}", size=F_CAPTION, color=C.TEXT_MUTED),
            ft.Row(
                [
                    icon("location_on", size=12, color=C.TEXT_DIM),
                    ft.Text(location, size=F_CAPTION, color=C.TEXT_DIM,
                            overflow=ft.TextOverflow.ELLIPSIS),
                ],
                spacing=SPACE_XS,
            ),
            ft.Container(height=SPACE_XS),
            status_badge,
        ],
        spacing=SPACE_XS,
        expand=True,
    )

    top_row = ft.Row(
        [date_block, info_col],
        spacing=SPACE_MD,
    )
    content_items.append(top_row)

    # Divider
    content_items.append(ft.Container(height=SPACE_MD))
    content_items.append(
        ft.Divider(color=C.BORDER, height=1)
    )
    content_items.append(ft.Container(height=SPACE_MD))

    # Footer: provider + price + actions
    provider_avatar = ft.Container(
        content=ft.Text(
            provider_initials.upper(), size=F_LABEL, weight="bold",
            color=C.TEXT, text_align=ft.TextAlign.CENTER,
        ),
        width=28, height=28, border_radius=14,
        bgcolor=C.AVATAR_BG,
        alignment=CENT,
    )

    provider_info = ft.Row(
        [
            provider_avatar,
            ft.Column(
                [
                    ft.Text(provider_name, size=F_CAPTION, weight="bold", color=C.TEXT),
                    ft.Text(f"{rating} estrellas", size=F_MONO, color=C.GOLD),
                ],
                spacing=0,
            ),
        ],
        spacing=SPACE_XS,
    )

    price_text = ft.Text(price, size=F_H3, weight="bold", color=C.GREEN)

    footer_row = ft.Row(
        [
            provider_info,
            ft.Container(expand=True),
            price_text,
            ft.Container(width=SPACE_MD),
            ft.IconButton(
                icon=icon("more_vert", size=18, color=C.TEXT_DIM).icon,
                icon_size=18, icon_color=C.TEXT_DIM,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=RADIUS_PILL)),
            ),
        ],
        spacing=SPACE_SM,
    )
    content_items.append(footer_row)

    # Acciones contextuales
    content_items.append(ft.Container(height=SPACE_MD))
    if status == "confirmed":
        actions = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Text("Reprogramar", size=F_CAPTION),
                    bgcolor="transparent", color=C.TEXT_MUTED,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=RADIUS_MD),
                        side=_b(1, C.BORDER_HOVER),
                        padding=pad(v=8, h=SPACE_LG),
                    ),
                ),
                ft.ElevatedButton(
                    content=ft.Text("Cancelar", size=F_CAPTION, color=C.RED),
                    bgcolor=C.RED_FAINT,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=RADIUS_MD),
                        padding=pad(v=8, h=SPACE_LG),
                    ),
                ),
            ],
            spacing=SPACE_SM,
        )
    elif status == "pending":
        actions = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Text("Confirmar", size=F_CAPTION),
                    bgcolor=C.GREEN, color=C.BG,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=RADIUS_MD),
                        padding=pad(v=8, h=SPACE_LG),
                    ),
                ),
                ft.ElevatedButton(
                    content=ft.Text("Cancelar", size=F_CAPTION, color=C.RED),
                    bgcolor="transparent",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=RADIUS_MD),
                        side=_b(1, C.RED_DIM),
                        padding=pad(v=8, h=SPACE_LG),
                    ),
                ),
            ],
            spacing=SPACE_SM,
        )
    else:
        actions = ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Text("Reservar de nuevo", size=F_CAPTION),
                    bgcolor=C.GREEN, color=C.BG,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=RADIUS_MD),
                        padding=pad(v=8, h=SPACE_LG),
                    ),
                ),
            ],
            spacing=SPACE_SM,
        )
    content_items.append(actions)

    return ft.Container(
        content=ft.Column(content_items, spacing=0, tight=True),
        bgcolor=C.SURFACE,
        border=_b(1, C.BORDER),
        border_radius=RADIUS_XL,
        padding=pad(v=SPACE_LG, h=SPACE_LG),
        width=420,
        ink=True,
    )
