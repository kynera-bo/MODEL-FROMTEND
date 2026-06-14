"""
StoryRing — Anillo de historia con gradiente arcoiris.
Variantes: visto, no visto, add story. Layout horizontal scrollable.
"""
import flet as ft
from theme import C, F_CAPTION, RADIUS_PILL, SPACE_SM, pad, gradient_border, CENT, icon


def story_ring(
    initials: str = "M",
    label: str = "tu_historia",
    seen: bool = False,
    is_add: bool = False,
    size: int = 64,
) -> ft.Container:
    """Anillo de historia individual.

    Args:
        initials: Iniciales del avatar
        label: Texto debajo del anillo
        seen: True = anillo gris (visto), False = gradiente arcoiris
        is_add: Versión "agregar historia" con icono +
        size: Tamaño del contenedor (default 64)
    """
    inner_size = size - 8
    font_size = max(10, inner_size // 3)

    if is_add:
        inner = ft.Container(
            content=icon("add", size=18, color=C.ACCENT),
            width=inner_size, height=inner_size,
            border_radius=inner_size // 2,
            bgcolor=C.ACCENT_FAINT,
            alignment=CENT,
        )
    else:
        inner = ft.Container(
            content=ft.Text(
                initials.upper(), size=font_size, weight="bold",
                color=C.TEXT, text_align=ft.TextAlign.CENTER,
            ),
            width=inner_size, height=inner_size,
            border_radius=inner_size // 2,
            bgcolor=C.AVATAR_BG,
            alignment=CENT,
        )

    if seen:
        ring = ft.Container(
            content=inner,
            border=ft.border.Border(
                top=ft.border.BorderSide(2.5, C.TEXT_DIM),
                left=ft.border.BorderSide(2.5, C.TEXT_DIM),
                right=ft.border.BorderSide(2.5, C.TEXT_DIM),
                bottom=ft.border.BorderSide(2.5, C.TEXT_DIM),
            ),
            border_radius=size // 2,
            padding=3,
        )
    else:
        ring = gradient_border(
            content=inner,
            width=2.5,
            radius=size // 2,
            bgcolor="transparent",
            padding=pad(v=1, h=1),
        )

    return ft.Container(
        content=ft.Column(
            [
                ring,
                ft.Text(
                    label[:12], size=F_CAPTION, color=C.TEXT_MUTED,
                    text_align=ft.TextAlign.CENTER,
                    overflow=ft.TextOverflow.ELLIPSIS,
                ),
            ],
            spacing=SPACE_SM,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            tight=True,
        ),
        width=size + 16,
        ink=True if not is_add else False,
    )


def story_group(stories: list[dict]) -> ft.Row:
    """Grupo de historias en layout horizontal scrollable.

    Cada dict debe tener: initials, label, seen (bool), is_add (bool opcional)
    """
    items = [story_ring(**s) for s in stories]
    return ft.Row(items, spacing=SPACE_SM, scroll=ft.ScrollMode.AUTO)
