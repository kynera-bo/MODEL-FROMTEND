"""
CartItem — Fila de carrito con imagen, stepper de cantidad, precio y subtotal.
"""
import flet as ft
from theme import C, F_H3, F_BODY, F_CAPTION, F_LABEL, RADIUS_MD, RADIUS_PILL, SPACE_XS, SPACE_SM, SPACE_MD, SPACE_LG, pad, _b, icon, CENT


def cart_item(
    product_name: str = "Audifonos Premium",
    variant: str = "Negro mate",
    image_url: str = None,
    unit_price: float = 129.99,
    original_price: float = None,
    quantity: int = 1,
    max_quantity: int = 10,
) -> ft.Container:
    """Fila de carrito de compras.

    Args:
        product_name: Nombre del producto
        variant: Variante o color
        image_url: Imagen del producto
        unit_price: Precio unitario
        original_price: Precio original (con descuento)
        quantity: Cantidad actual
        max_quantity: Cantidad maxima
    """
    content_items = []

    # Imagen del producto
    if image_url:
        img = ft.Container(
            content=ft.Image(src=image_url, fit=ft.BoxFit.COVER),
            width=72, height=72,
            border_radius=RADIUS_MD,
            border=_b(1, C.BORDER),
        )
    else:
        img = ft.Container(
            content=icon("inventory_2", size=28, color=C.TEXT_DIM),
            width=72, height=72,
            border_radius=RADIUS_MD,
            border=_b(1, C.BORDER),
            bgcolor=C.SURFACE2,
            alignment=CENT,
        )

    # Info del producto
    price_row_items = [
        ft.Text(f"${unit_price:.2f}", size=F_BODY, weight="bold", color=C.TEXT),
    ]
    if original_price and original_price > unit_price:
        discount_pct = int((1 - unit_price / original_price) * 100)
        price_row_items.append(
            ft.Container(
                content=ft.Text(f"-{discount_pct}%", size=F_LABEL, color=C.GREEN,
                                weight="bold", font_family="monospace"),
                bgcolor=C.GREEN_FAINT,
                border_radius=RADIUS_PILL,
                padding=pad(v=2, h=SPACE_SM),
            )
        )

    info_col = ft.Column(
        [
            ft.Text(product_name, size=F_BODY, weight="bold", color=C.TEXT,
                    overflow=ft.TextOverflow.ELLIPSIS),
            ft.Text(variant, size=F_CAPTION, color=C.TEXT_MUTED),
            ft.Container(height=SPACE_XS),
            ft.Row(price_row_items, spacing=SPACE_SM),
        ],
        spacing=SPACE_XS,
        expand=True,
    )

    # Stepper de cantidad
    stepper = _quantity_stepper(quantity, max_quantity)

    # Subtotal
    subtotal = unit_price * quantity
    subtotal_text = ft.Text(
        f"${subtotal:.2f}", size=F_H3, weight="bold", color=C.GREEN,
    )

    # Delete
    delete_btn = ft.IconButton(
        icon=icon("delete_outline", size=18, color=C.RED_DIM).icon,
        icon_size=18, icon_color=C.RED_DIM,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=RADIUS_PILL)),
    )

    top_row = ft.Row(
        [img, info_col, ft.Container(width=SPACE_MD), subtotal_text, delete_btn],
        spacing=SPACE_MD,
    )

    # Stepper abajo en mobile o al lado en desktop (responsive con wrap)
    stepper_row = ft.Row([stepper], spacing=0)

    content_items.append(top_row)
    content_items.append(ft.Container(height=SPACE_MD))
    content_items.append(stepper_row)

    return ft.Container(
        content=ft.Column(content_items, spacing=0, tight=True),
        bgcolor=C.SURFACE,
        border=_b(1, C.BORDER),
        border_radius=RADIUS_MD,
        padding=pad(v=SPACE_MD, h=SPACE_LG),
    )


def _quantity_stepper(quantity: int, max_qty: int) -> ft.Container:
    """Stepper - / N / + con estilo gold."""

    def minus_style():
        return ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=6),
            bgcolor=C.GOLD_FAINT,
            padding=pad(v=0, h=0),
        )

    def plus_style():
        return ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=6),
            bgcolor=C.GOLD_FAINT,
            padding=pad(v=0, h=0),
        )

    minus_btn = ft.IconButton(
        icon=icon("remove", size=16, color=C.GOLD).icon,
        icon_size=16, icon_color=C.GOLD,
        width=32, height=32,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=RADIUS_MD),
            bgcolor=C.GOLD_FAINT,
            padding=pad(v=0, h=0),
        ),
    )

    quantity_label = ft.Container(
        content=ft.Text(
            str(quantity), size=F_BODY, weight="bold", color=C.TEXT,
            text_align=ft.TextAlign.CENTER,
        ),
        width=40, height=32,
        alignment=CENT,
        border=_b(1, C.GOLD_DIM),
        border_radius=RADIUS_MD,
    )

    plus_btn = ft.IconButton(
        icon=icon("add", size=16, color=C.GOLD).icon,
        icon_size=16, icon_color=C.GOLD,
        width=32, height=32,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=RADIUS_MD),
            bgcolor=C.GOLD_FAINT,
            padding=pad(v=0, h=0),
        ),
    )

    return ft.Container(
        content=ft.Row(
            [minus_btn, quantity_label, plus_btn],
            spacing=SPACE_XS,
        ),
        border=_b(1, C.GOLD_DIM),
        border_radius=RADIUS_MD,
        padding=pad(v=4, h=SPACE_XS),
    )
