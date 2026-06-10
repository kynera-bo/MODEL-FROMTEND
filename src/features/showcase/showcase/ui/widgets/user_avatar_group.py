"""
UserAvatarGroup — Grupo de avatares solapados con contador "+N".
"""
import flet as ft
from theme import C, F_CAPTION, F_LABEL, RADIUS_PILL, pad, _b, CENT


def user_avatar_group(
    users: list[dict],
    max_visible: int = 4,
    size: int = 32,
) -> ft.Row:
    """Grupo de avatares solapados con contador +N.

    Args:
        users: Lista de dicts con 'initials' y opcional 'color' (hex)
        max_visible: Maximo de avatares visibles antes del contador
        size: Tamaño de cada avatar en px

    Returns un Row con los avatares solapados.
    """
    avatar_items = []
    overlap = size // 3

    for i, user in enumerate(users[:max_visible]):
        avatar_bg = user.get("color", C.AVATAR_BG)
        avatar = ft.Container(
            content=ft.Text(
                user["initials"].upper()[:2],
                size=max(8, size // 3),
                weight="bold",
                color=C.TEXT,
                text_align=ft.TextAlign.CENTER,
            ),
            width=size, height=size,
            border_radius=size // 2,
            bgcolor=avatar_bg,
            border=_b(2, C.BG),
            alignment=CENT,
        )
        avatar_items.append(
            ft.Container(
                content=avatar,
                margin=ft.margin.Margin(left=-(overlap) if i > 0 else 0, top=0, right=0, bottom=0),
            )
        )

    remaining = len(users) - max_visible
    if remaining > 0:
        counter = ft.Container(
            content=ft.Text(
                f"+{remaining}", size=max(8, size // 3), weight="bold",
                color=C.TEXT_MUTED, text_align=ft.TextAlign.CENTER,
            ),
            width=size, height=size,
            border_radius=size // 2,
            bgcolor=C.SURFACE2,
            border=_b(2, C.BG),
            alignment=CENT,
        )
        avatar_items.append(
            ft.Container(
                content=counter,
                margin=ft.margin.Margin(left=-(overlap), top=0, right=0, bottom=0),
            )
        )

    return ft.Row(avatar_items, spacing=0, vertical_alignment=ft.CrossAxisAlignment.CENTER)


def user_avatar_label_group(
    users: list[dict],
    label: str = "Les gusta",
    max_visible: int = 3,
    size: int = 28,
) -> ft.Row:
    """Grupo de avatares con label descriptivo al lado.

    Ejemplo: [Avatars] "Maria, Carlos y 12 mas les gusta"
    """
    avatars = user_avatar_group(users, max_visible=max_visible, size=size)

    names = [u.get("name", u.get("initials", "?")) for u in users[:2]]
    total = len(users)

    if total <= 2:
        label_text = f"{' y '.join(names)} {label}"
    else:
        label_text = f"{', '.join(names)} y {total - 2} mas {label}"

    return ft.Row(
        [
            avatars,
            ft.Text(label_text, size=F_CAPTION, color=C.TEXT_MUTED),
        ],
        spacing=4,
    )
