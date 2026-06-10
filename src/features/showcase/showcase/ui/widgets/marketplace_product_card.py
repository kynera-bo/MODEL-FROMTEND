"""
MarketplaceProductCard — Card de producto con imagen, precio en gold, rating, seller.
"""
import flet as ft
from theme import C, F_H3, F_BODY, F_CAPTION, F_LABEL, RADIUS_XL, RADIUS_LG, RADIUS_MD, RADIUS_PILL, SPACE_XS, SPACE_SM, SPACE_MD, SPACE_LG, pad, _b, icon, CENT


def marketplace_product_card(
    product_name: str = "Audifonos Premium",
    price: str = "$129.99",
    original_price: str = None,
    image_url: str = None,
    rating: float = 4.8,
    review_count: int = 342,
    category: str = "Electronica",
    in_stock: bool = True,
    seller_name: str = "TechStore",
    seller_initials: str = "TS",
) -> ft.Container:
    """Card de producto para marketplace.

    Args:
        product_name: Nombre del producto
        price: Precio actual (string con formato)
        original_price: Precio original tachado (opcional)
        image_url: Imagen del producto
        rating: Puntuacion de 0 a 5
        review_count: Cantidad de reviews
        category: Categoria del producto
        in_stock: Si esta en stock
        seller_name: Nombre del vendedor
        seller_initials: Iniciales del vendedor
    """
    content_items = []

    # Imagen con badge de precio
    if image_url:
        price_badge = ft.Container(
            content=ft.Text(price, size=F_H3, weight="bold", color=C.GOLD),
            bgcolor="#CC080504",
            border_radius=RADIUS_MD,
            padding=pad(v=4, h=SPACE_SM),
            right=8, top=8,
        )

        image_content = ft.Stack(
            [
                ft.Image(src=image_url, fit=ft.BoxFit.COVER),
                price_badge,
            ],
        )
        content_items.append(
            ft.Container(
                content=image_content,
                border_radius=RADIUS_LG,
                height=180,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            )
        )
        content_items.append(ft.Container(height=SPACE_MD))

    # Info principal
    content_items.append(
        ft.Text(product_name, size=F_H3, weight="bold", color=C.TEXT,
                max_lines=2, overflow=ft.TextOverflow.ELLIPSIS)
    )

    # Categoria + stock
    stock_dot = ft.Container(
        width=6, height=6, border_radius=3,
        bgcolor=C.GREEN if in_stock else C.RED,
    )
    stock_text = "En stock" if in_stock else "Agotado"
    stock_color = C.GREEN if in_stock else C.RED_DIM

    meta_row = ft.Row(
        [
            ft.Container(
                content=ft.Text(category.upper(), size=F_LABEL, color=C.GREEN,
                                weight="bold", font_family="monospace"),
                bgcolor=C.GREEN_FAINT,
                border_radius=RADIUS_PILL,
                padding=pad(v=2, h=SPACE_SM),
            ),
            ft.Text("·", color=C.TEXT_DIM),
            stock_dot,
            ft.Text(stock_text, size=F_CAPTION, color=stock_color),
        ],
        spacing=SPACE_SM,
    )
    content_items.append(ft.Container(height=SPACE_SM))
    content_items.append(meta_row)

    # Rating estrellas
    content_items.append(ft.Container(height=SPACE_SM))
    stars_row = _build_stars(rating)
    stars_row_items = [stars_row]
    stars_row_items.append(
        ft.Text(f"{rating} ({review_count})", size=F_CAPTION, color=C.TEXT_MUTED)
    )
    content_items.append(
        ft.Row(stars_row_items, spacing=SPACE_SM)
    )

    # Precios
    content_items.append(ft.Container(height=SPACE_SM))
    price_row_items = [
        ft.Text(price, size=F_H3, weight="bold", color=C.GOLD),
    ]
    if original_price:
        price_row_items.append(
            ft.Text(original_price, size=F_CAPTION, color=C.TEXT_DIM,
                    style=ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH))
        )
    content_items.append(
        ft.Row(price_row_items, spacing=SPACE_SM)
    )

    # Seller
    content_items.append(ft.Container(height=SPACE_MD))
    seller_avatar = ft.Container(
        content=ft.Text(
            seller_initials.upper(), size=F_LABEL, weight="bold",
            color=C.TEXT, text_align=ft.TextAlign.CENTER,
        ),
        width=24, height=24, border_radius=12,
        bgcolor=C.AVATAR_BG,
        alignment=CENT,
    )

    content_items.append(
        ft.Row(
            [
                seller_avatar,
                ft.Text(seller_name, size=F_CAPTION, color=C.TEXT_MUTED),
            ],
            spacing=SPACE_SM,
        )
    )

    return ft.Container(
        content=ft.Column(content_items, spacing=0, tight=True),
        bgcolor=C.SURFACE,
        border=_b(1, C.BORDER),
        border_radius=RADIUS_XL,
        padding=pad(v=SPACE_MD, h=SPACE_LG),
        width=280,
        ink=True,
    )


def _build_stars(rating: float) -> ft.Row:
    """Construye fila de estrellas con soporte de media estrella."""
    stars = []
    for i in range(5):
        if rating >= i + 1:
            stars.append(icon("star", size=14, color=C.GOLD))
        elif rating >= i + 0.5:
            stars.append(icon("star_half", size=14, color=C.GOLD))
        else:
            stars.append(icon("star_border", size=14, color=C.TEXT_DIM))
    return ft.Row(stars, spacing=2)
