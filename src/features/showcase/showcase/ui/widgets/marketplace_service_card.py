import flet as ft
from theme import C
from theme import RADIUS_XL, RADIUS_MD, RADIUS_PILL
from theme import SPACE_MD
from theme import pad, _b, icon, CENT


def marketplace_service_card(
    title: str = "Diseno Grafico Profesional",
    description: str = "Logos, branding, social media. Resultados profesionales en 48h.",
    icon_name: str = "brush",
    tags: list[str] | None = None,
    price_label: str = "Desde $50/h",
    available: bool = True,
    provider_name: str = "Ana Martinez",
    provider_initials: str = "AM",
    rating: float = 4.9,
    review_count: int = 128,
    location: str = "Remoto / NYC",
    response_time: str = "< 1h",
    image_url: str | None = None,
) -> ft.Container:
    if tags is None:
        tags = ["Branding", "Social Media"]

    overlays = []
    if image_url:
        overlays.append(
            ft.Container(expand=True, content=ft.Image(src=image_url, fit=ft.BoxFit.COVER))
        )
        overlays.append(
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    colors=["transparent", "#CC000000"],
                    begin=ft.alignment.Alignment(0, 0.3),
                    end=ft.alignment.Alignment(0, 1),
                ),
            ),
        )
        overlay_content = ft.Container(
            content=ft.Row([
                icon(icon_name, size=16, color=C.TEXT),
                ft.Text(price_label, size=14, weight="bold", color=C.TEXT),
            ], spacing=4),
            left=10, top=10,
        )
        overlays.append(overlay_content)
        overlays.append(
            ft.Container(
                content=ft.Text(response_time, size=9, color=C.ACCENT, weight="bold"),
                bgcolor="#BB000000", border_radius=RADIUS_PILL, padding=pad(v=2, h=6),
                right=8, bottom=8,
            )
        )
    else:
        overlays.append(
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=icon(icon_name, size=32, color=C.ACCENT),
                        width=60, height=60, border_radius=30,
                        bgcolor=C.ACCENT_FAINT, border=_b(1.5, C.ACCENT_DIM), alignment=CENT,
                    ),
                    ft.Container(height=6),
                    ft.Text(price_label, size=15, weight="bold", color=C.TEXT),
                    ft.Text(response_time, size=10, color=C.ACCENT),
                ], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER, tight=True),
                expand=True, alignment=CENT, bgcolor=C.SURFACE2,
            )
        )

    chips = [
        ft.Container(
            content=ft.Text(t.upper(), size=8, color=C.ACCENT, weight="bold"),
            bgcolor=C.ACCENT_FAINT, border_radius=RADIUS_PILL, padding=pad(v=2, h=6),
        )
        for t in tags
    ]
    prov = ft.Container(
        content=ft.Text(provider_initials.upper(), size=8, weight="bold", color=C.TEXT, text_align=ft.TextAlign.CENTER),
        width=18, height=18, border_radius=9, bgcolor=C.AVATAR_BG, alignment=CENT,
    )
    stars = ft.Row([], spacing=1)
    for i in range(5):
        if rating >= i + 1:
            stars.controls.append(icon("star", size=10, color=C.ACCENT))
        elif rating >= i + 0.5:
            stars.controls.append(icon("star_half", size=10, color=C.ACCENT))
        else:
            stars.controls.append(icon("star_border", size=10, color=C.TEXT_DIM))

    overlays.append(
        ft.Container(
            content=ft.Column([
                ft.Text(title, size=13, weight=ft.FontWeight.BOLD, color=C.TEXT,
                        max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                ft.Container(height=3),
                ft.Row(chips, spacing=4, wrap=True, run_spacing=3),
                ft.Container(height=3),
                ft.Row([
                    prov,
                    ft.Text(provider_name, size=9, color=C.TEXT_MUTED,
                            max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Container(expand=True),
                    stars,
                    ft.Text(f"{rating}", size=9, color=C.ACCENT, weight="bold"),
                ], spacing=3, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Container(height=4),
                ft.Button(
                    "Reservar",
                    height=28,
                    style=ft.ButtonStyle(
                        bgcolor=C.ACCENT, color=C.BG,
                        shape=ft.RoundedRectangleBorder(radius=RADIUS_MD),
                        padding=pad(v=4, h=SPACE_MD),
                    ),
                ),
            ], spacing=0, tight=True),
            bgcolor="#CC000000", border_radius=RADIUS_MD,
            left=0, right=0, bottom=0,
            padding=pad(v=8, h=10),
        )
    )

    return ft.Container(
        content=ft.Stack(overlays, expand=True),
        expand=True,
        bgcolor=C.SURFACE, border=_b(1, C.BORDER_STRONG), border_radius=RADIUS_XL,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        ink=True,
    )
