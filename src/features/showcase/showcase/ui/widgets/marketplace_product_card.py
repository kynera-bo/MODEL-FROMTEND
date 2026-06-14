import flet as ft
from theme import C
from theme import RADIUS_XL, RADIUS_MD, RADIUS_PILL
from theme import pad, _b, icon


def marketplace_product_card(
    product_name: str = "Audifonos Premium",
    price: str = "$129.99",
    original_price: str | None = None,
    image_url: str | None = None,
    rating: float = 4.8,
    review_count: int = 342,
    category: str = "Electronica",
    in_stock: bool = True,
    seller_name: str = "TechStore",
    seller_initials: str = "TS",
    discount_percent: int | None = None,
    free_shipping: bool = False,
    orders_count: int = 1500,
) -> ft.Container:
    if discount_percent is None and original_price:
        op = float(original_price.replace("$", "").replace(",", ""))
        cp = float(price.replace("$", "").replace(",", ""))
        if op > 0:
            discount_percent = round((1 - cp / op) * 100)

    overlays = []
    if image_url:
        overlays.append(
            ft.Container(expand=True, content=ft.Image(src=image_url, fit=ft.BoxFit.COVER))
        )
    else:
        overlays.append(ft.Container(expand=True, bgcolor=C.SURFACE2))

    if discount_percent and discount_percent > 0:
        overlays.append(
            ft.Container(
                content=ft.Text(f"-{discount_percent}%", size=10, color=C.BG, weight="bold"),
                bgcolor=C.ERROR, border_radius=RADIUS_PILL, padding=pad(v=2, h=7),
                left=8, top=8,
            )
        )

    overlays.append(
        ft.Container(
            content=ft.Text(price, size=15, weight="bold", color=C.TEXT),
            bgcolor="#BB000000", border_radius=RADIUS_MD, padding=pad(v=3, h=8),
            right=8, top=8,
        )
    )

    stars = ft.Row([], spacing=1)
    for i in range(5):
        if rating >= i + 1:
            stars.controls.append(icon("star", size=11, color=C.ACCENT))
        elif rating >= i + 0.5:
            stars.controls.append(icon("star_half", size=11, color=C.ACCENT))
        else:
            stars.controls.append(icon("star_border", size=11, color=C.TEXT_DIM))

    price_items = [ft.Text(price, size=15, weight="bold", color=C.TEXT)]
    if original_price:
        price_items.append(
            ft.Text(original_price, size=11, color=C.TEXT_DIM,
                    style=ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH))
        )

    overlays.append(
        ft.Container(
            content=ft.Column([
                ft.Text(product_name, size=13, weight=ft.FontWeight.BOLD, color=C.TEXT,
                        max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                ft.Container(height=3),
                ft.Row([
                    stars,
                    ft.Text(f"{rating}", size=10, color=C.ACCENT, weight="bold"),
                    ft.Text(f"({review_count})", size=9, color=C.TEXT_DIM),
                ], spacing=3, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Container(height=3),
                ft.Row(price_items, spacing=5, vertical_alignment=ft.CrossAxisAlignment.CENTER),
            ], spacing=0, tight=True),
            bgcolor="#CC000000", border_radius=RADIUS_MD,
            left=0, right=0, bottom=0,
            padding=pad(v=8, h=10),
        )
    )

    if free_shipping:
        overlays.append(
            ft.Container(
                content=ft.Row([
                    icon("local_shipping", size=10, color=C.ACCENT),
                    ft.Text("Envio gratis", size=9, color=C.ACCENT, weight="bold"),
                ], spacing=2),
                bgcolor="#BB000000", border_radius=RADIUS_PILL, padding=pad(v=2, h=6),
                left=8, bottom=80,
            )
        )

    return ft.Container(
        content=ft.Stack(overlays, expand=True),
        expand=True,
        bgcolor=C.SURFACE, border=_b(1, C.BORDER), border_radius=RADIUS_XL,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        ink=True,
    )
