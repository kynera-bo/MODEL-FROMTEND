"""
Showcase page — Vitrina de todos los componentes reutilizables.
Sub-navegacion interna por categorias via page.route.
"""
import flet as ft
from theme import C, F_H1, F_H2, F_H3, F_BODY, F_CAPTION, F_LABEL, F_MONO, \
    RADIUS_XL, RADIUS_LG, RADIUS_MD, \
    SPACE_XS, SPACE_SM, SPACE_MD, SPACE_LG, SPACE_XL, SPACE_XXL, \
    pad, _b, icon, divider, CENT

from features.showcase.showcase.ui.widgets.chat_bubble import chat_bubble
from features.showcase.showcase.ui.widgets.conversation_list_item import conversation_list_item
from features.showcase.showcase.ui.widgets.post_card import post_card
from features.showcase.showcase.ui.widgets.story_ring import story_ring, story_group
from features.showcase.showcase.ui.widgets.notification_item import notification_item
from features.showcase.showcase.ui.widgets.marketplace_product_card import marketplace_product_card
from features.showcase.showcase.ui.widgets.marketplace_service_card import marketplace_service_card
from features.showcase.showcase.ui.widgets.marketplace_barter_card import marketplace_barter_card
from features.showcase.showcase.ui.widgets.reservation_card import reservation_card
from features.showcase.showcase.ui.widgets.cart_item import cart_item
from features.showcase.showcase.ui.widgets.wishlist_heart import wishlist_heart
from features.showcase.showcase.ui.widgets.reel_thumbnail import reel_thumbnail
from features.showcase.showcase.ui.widgets.search_bar_premium import search_bar_premium
from features.showcase.showcase.ui.widgets.calendar_heatmap import calendar_heatmap
from features.showcase.showcase.ui.widgets.user_avatar_group import user_avatar_group, user_avatar_label_group


COMPONENTS = [
    {
        "section": "Mensajeria",
        "items": [
            {"id": "chat-bubble", "label": "Chat Bubble", "desc": "Burbuja de mensaje enviado/recibido"},
            {"id": "conversation-list", "label": "Conversation List", "desc": "Preview de conversacion"},
        ],
    },
    {
        "section": "Red Social",
        "items": [
            {"id": "post-card", "label": "Post Card", "desc": "Publicacion estilo Instagram"},
            {"id": "story-ring", "label": "Story Ring", "desc": "Anillo de historia con gradiente"},
            {"id": "reel-thumbnail", "label": "Reel Thumbnail", "desc": "Thumbnail de video corto 9:16"},
            {"id": "user-avatar-group", "label": "Avatar Group", "desc": "Grupo de avatares solapados"},
        ],
    },
    {
        "section": "Notificaciones",
        "items": [
            {"id": "notification-item", "label": "Notification Item", "desc": "5 variantes de notificacion"},
        ],
    },
    {
        "section": "Marketplace",
        "items": [
            {"id": "product-card", "label": "Product Card", "desc": "Card de producto con precio y rating"},
            {"id": "service-card", "label": "Service Card", "desc": "Card de servicio con tags y reserva"},
            {"id": "barter-card", "label": "Barter Card", "desc": "Card de trueque Ofrezco/Busco"},
            {"id": "reservation-card", "label": "Reservation Card", "desc": "Card de reserva con estados"},
            {"id": "cart-item", "label": "Cart Item", "desc": "Fila de carrito con stepper"},
            {"id": "wishlist-heart", "label": "Wishlist Heart", "desc": "Boton de favorito con contador"},
        ],
    },
    {
        "section": "Utilidades",
        "items": [
            {"id": "search-bar", "label": "Search Bar Premium", "desc": "Barra de busqueda con filtros"},
            {"id": "calendar-heatmap", "label": "Calendar Heatmap", "desc": "Mapa de calor tipo GitHub"},
        ],
    },
]


def showcase_content(page: ft.Page) -> ft.Container:
    route = page.route
    comp_id = None
    if route.startswith("/showcase/") and len(route) > len("/showcase/"):
        comp_id = route[len("/showcase/"):]

    sidebar_items = _build_sidebar(page, comp_id)

    sidebar = ft.Container(
        content=ft.Column(sidebar_items, spacing=0, scroll=ft.ScrollMode.AUTO, expand=True),
        bgcolor=C.SURFACE,
        border=_b(1, C.BORDER),
        border_radius=RADIUS_LG,
        padding=pad(v=SPACE_MD, h=0),
        width=260,
        expand=False,
    )

    right_content = _render_component(comp_id) if comp_id else _render_grid_overview()
    right = ft.Container(
        content=right_content,
        expand=True,
        padding=pad(l=SPACE_XL),
    )

    layout = ft.Row(
        [sidebar, right],
        spacing=0,
        expand=True,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

    return ft.Container(
        content=layout,
        padding=SPACE_XXL,
        expand=True,
    )


def _build_sidebar(page, active_id):
    items = []

    # Boton de volver a overview
    if active_id:
        items.append(
            ft.Container(
                content=ft.Row(
                    [
                        icon("chevron_up", size=14, color=C.GREEN),
                        ft.Text("VER TODOS", size=F_LABEL, color=C.GREEN,
                                weight="bold", font_family="monospace"),
                    ],
                    spacing=SPACE_SM,
                ),
                padding=pad(v=SPACE_SM, h=SPACE_MD),
                on_click=lambda e: page.go("/showcase"),
                ink=True,
            )
        )
        items.append(divider())

    title = ft.Container(
        content=ft.Text("COMPONENTES", size=F_LABEL, color=C.GOLD, weight="bold",
                        font_family="monospace"),
        padding=pad(v=SPACE_SM, h=SPACE_MD),
    )
    items.append(title)
    items.append(divider())

    for section in COMPONENTS:
        items.append(ft.Container(height=SPACE_SM))
        items.append(
            ft.Text(
                section["section"].upper(),
                size=F_LABEL, color=C.TEXT_DIM, weight="bold", font_family="monospace",
            )
        )
        items.append(ft.Container(height=SPACE_XS))
        items.append(
            ft.Container(padding=pad(l=SPACE_MD, h=SPACE_MD))
        )

        for comp in section["items"]:
            is_active = active_id == comp["id"]
            bg = C.ITEM_ACTIVE_BG if is_active else None
            text_color = C.TEXT if is_active else C.TEXT_MUTED

            items.append(
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(comp["label"], size=F_BODY, weight="bold", color=text_color),
                            ft.Text(comp["desc"], size=F_MONO,
                                    color=C.TEXT_DIM if is_active else C.TEXT_DIM2),
                        ],
                        spacing=SPACE_XS,
                    ),
                    bgcolor=bg,
                    border=_b(1, C.GREEN if is_active else "transparent"),
                    border_radius=RADIUS_MD,
                    padding=pad(v=SPACE_SM, h=SPACE_MD),
                    on_click=lambda e, cid=comp["id"]: page.go(f"/showcase/{cid}"),
                    ink=True,
                )
            )
    return items


def _render_component(comp_id):
    renderers = {
        "chat-bubble": _render_chat_bubble,
        "conversation-list": _render_conversation_list,
        "post-card": _render_post_card,
        "story-ring": _render_story_ring,
        "notification-item": _render_notification_item,
        "product-card": _render_product_card,
        "service-card": _render_service_card,
        "barter-card": _render_barter_card,
        "reservation-card": _render_reservation_card,
        "cart-item": _render_cart_item,
        "wishlist-heart": _render_wishlist_heart,
        "reel-thumbnail": _render_reel_thumbnail,
        "search-bar": _render_search_bar,
        "calendar-heatmap": _render_calendar_heatmap,
        "user-avatar-group": _render_avatar_group,
    }
    renderer = renderers.get(comp_id)
    if renderer:
        return renderer()
    return ft.Text("Componente no encontrado", color=C.TEXT_MUTED)


def _render_grid_overview():
    cards = []
    for section in COMPONENTS:
        cards.append(
            ft.Text(section["section"], size=F_H2, weight="bold", color=C.GOLD)
        )
        cards.append(ft.Container(height=SPACE_MD))
        row_items = []
        for comp in section["items"]:
            row_items.append(_preview_card(comp))
        cards.append(
            ft.ResponsiveRow(row_items, spacing=SPACE_MD, run_spacing=SPACE_MD)
        )
        cards.append(ft.Container(height=SPACE_XL))

    return ft.Column(cards, spacing=0, scroll=ft.ScrollMode.AUTO)


def _preview_card(comp):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(comp["label"], size=F_H3, weight="bold", color=C.TEXT),
                ft.Text(comp["desc"], size=F_CAPTION, color=C.TEXT_MUTED),
            ],
            spacing=SPACE_XS,
        ),
        bgcolor=C.SURFACE,
        border=_b(1, C.BORDER),
        border_radius=RADIUS_LG,
        padding=pad(v=SPACE_MD, h=SPACE_LG),
        width=240,
        ink=True,
        col={"sm": 12, "md": 6, "lg": 4},
    )


def _section_title(title: str, subtitle: str) -> ft.Column:
    return ft.Column(
        [
            ft.Text(title, size=F_H1, weight="bold", color=C.TEXT),
            ft.Text(subtitle, size=F_BODY, color=C.TEXT_MUTED),
            ft.Container(height=SPACE_XL),
        ],
        spacing=SPACE_XS,
    )


def _render_chat_bubble():
    return ft.Column(
        [
            _section_title("Chat Bubble", "Burbuja de mensaje con variantes enviado/recibido"),
            ft.Text("ENVIADO", size=F_LABEL, color=C.TEXT_DIM, font_family="monospace"),
            ft.Container(height=SPACE_SM),
            ft.Row([
                ft.Container(expand=True),
                chat_bubble("Hola! Como estas?", sent=True, timestamp="10:32 AM", read=True),
            ]),
            ft.Container(height=SPACE_LG),
            ft.Text("ENVIADO CON IMAGEN", size=F_LABEL, color=C.TEXT_DIM, font_family="monospace"),
            ft.Container(height=SPACE_SM),
            ft.Row([
                ft.Container(expand=True),
                chat_bubble("Mira esta foto!", sent=True, timestamp="10:35 AM", read=False,
                            image_url="https://picsum.photos/200/140"),
            ]),
            ft.Container(height=SPACE_LG),
            ft.Text("RECIBIDO", size=F_LABEL, color=C.TEXT_DIM, font_family="monospace"),
            ft.Container(height=SPACE_SM),
            chat_bubble("Todo bien! Nos vemos a las 3?", sent=False, timestamp="10:33 AM", read=False),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


def _render_conversation_list():
    chats = [
        {"avatar_initials": "M", "name": "Maria L.", "last_message": "Hola, como estas? Nos vemos manana", "timestamp": "10:32", "unread_count": 3, "online": True, "is_active": True},
        {"avatar_initials": "C", "name": "Carlos Dev", "last_message": "Listo el diseno! Te envio los archivos", "timestamp": "09:15", "unread_count": 0, "online": True},
        {"avatar_initials": "A", "name": "Ana Martinez", "last_message": "Perfecto, confirmado para el viernes", "timestamp": "Ayer", "unread_count": 1, "online": False},
        {"avatar_initials": "GT", "name": "Grupo Trabajo", "last_message": "Juan: Yo llevo las bebidas y algo mas", "timestamp": "Ayer", "unread_count": 12, "online": False},
        {"avatar_initials": "P", "name": "Pedro Sanchez", "last_message": "Gracias por la info!", "timestamp": "Lun", "unread_count": 0, "online": False},
    ]
    items = [conversation_list_item(**c) for c in chats]
    return ft.Column(
        [
            _section_title("Conversation List", "Preview de conversaciones estilo WhatsApp/Instagram"),
            ft.Container(
                content=ft.Column(items, spacing=0),
                bgcolor=C.SURFACE,
                border=_b(1, C.BORDER),
                border_radius=RADIUS_XL,
                padding=pad(v=SPACE_SM, h=0),
                width=380,
            ),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


def _render_post_card():
    return ft.Column(
        [
            _section_title("Post Card", "Publicacion estilo red social con interacciones"),
            post_card(
                username="maria.lopez", display_name="Maria Lopez",
                avatar_initials="ML", timestamp="2 horas",
                content="Acabo de descubrir este marketplace increible! Los productos son de primera calidad y la experiencia de compra es simplemente genial. Super recomendado!",
                likes_count=2847, liked=True,
            ),
            ft.Container(height=SPACE_LG),
            post_card(
                username="carlos.dev", display_name="Carlos Dev",
                avatar_initials="CD", timestamp="5 horas",
                content="Nuevo servicio de desarrollo web disponible. Construimos tu sitio desde cero con las mejores tecnologias.",
                likes_count=523, liked=False,
            ),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


def _render_story_ring():
    stories = [
        {"initials": "M", "label": "tu_historia", "seen": False, "is_add": True},
        {"initials": "M", "label": "maria.lopez", "seen": False},
        {"initials": "C", "label": "carlos.dev", "seen": False},
        {"initials": "A", "label": "ana.mtz", "seen": True},
        {"initials": "P", "label": "pedro.s", "seen": True},
        {"initials": "L", "label": "laura.g", "seen": False},
        {"initials": "D", "label": "diego.r", "seen": True},
        {"initials": "S", "label": "sofia.m", "seen": False},
    ]
    return ft.Column(
        [
            _section_title("Story Ring", "Anillo de historias con gradiente arcoiris y variantes"),
            story_group(stories),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


def _render_notification_item():
    notifications = [
        {"notif_type": "message", "title": "Nuevo mensaje", "description": "Maria te envio un mensaje", "timestamp": "ahora", "unread": True, "action_label": "Ver"},
        {"notif_type": "event", "title": "Recordatorio", "description": "Reunion de equipo manana a las 3:00 PM", "timestamp": "hace 30m", "unread": True, "action_label": "Detalles"},
        {"notif_type": "task", "title": "Tarea completada", "description": "Diseno UI - Version final aprobada", "timestamp": "hace 2h", "unread": False},
        {"notif_type": "activity", "title": "Tu publicacion", "description": "Alcanzo 500 visualizaciones en 24h", "timestamp": "hace 5h", "unread": True, "action_label": "Ver"},
        {"notif_type": "system", "title": "Actualizacion", "description": "Nuevos terminos y condiciones disponibles", "timestamp": "hace 1d", "unread": False},
    ]
    items = [notification_item(**n) for n in notifications]
    return ft.Column(
        [
            _section_title("Notification Item", "5 variantes de notificacion con iconos y colores semanticos"),
            ft.Container(
                content=ft.Column(items, spacing=SPACE_XS),
                bgcolor=C.SURFACE,
                border=_b(1, C.BORDER),
                border_radius=RADIUS_XL,
                padding=pad(v=SPACE_SM, h=SPACE_SM),
                width=420,
            ),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


def _render_product_card():
    return ft.Column(
        [
            _section_title("Product Card", "Card de producto con precio en gold, rating y seller"),
            ft.Row(
                [
                    marketplace_product_card(
                        product_name="Audifonos Premium NC",
                        price="$129.99", original_price="$179.99",
                        category="Electronica", rating=4.8, review_count=342,
                        seller_name="TechStore", seller_initials="TS",
                    ),
                    ft.Container(width=SPACE_LG),
                    marketplace_product_card(
                        product_name="Zapatillas Running Pro",
                        price="$89.99", category="Deportes",
                        rating=4.5, review_count=128, in_stock=False,
                        seller_name="SportWorld", seller_initials="SW",
                    ),
                ],
                spacing=0, wrap=True, run_spacing=SPACE_MD,
            ),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


def _render_service_card():
    return ft.Column(
        [
            _section_title("Service Card", "Card de servicio con icono, tags y boton de reserva"),
            ft.Row(
                [
                    marketplace_service_card(
                        title="Diseno Grafico Profesional",
                        description="Logos, branding, social media y mas. Resultados profesionales en 48h.",
                        icon_name="brush", tags=["Branding", "Social Media", "Logos"],
                        price_label="Desde $50/h",
                        provider_name="Ana Martinez", provider_initials="AM", rating=4.9,
                    ),
                    ft.Container(width=SPACE_LG),
                    marketplace_service_card(
                        title="Desarrollo Web Fullstack",
                        description="Sitios web modernos con React, Node.js y bases de datos.",
                        icon_name="code", tags=["React", "Node.js", "PostgreSQL"],
                        price_label="$2,500/proyecto", available=False,
                        provider_name="Carlos Dev", provider_initials="CD", rating=4.7,
                    ),
                ],
                spacing=0, wrap=True, run_spacing=SPACE_MD,
            ),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


def _render_barter_card():
    return ft.Column(
        [
            _section_title("Barter Card", "Card de trueque con layout Ofrezco <-> Busco"),
            ft.Row(
                [
                    marketplace_barter_card(
                        offer_item="iPhone 13 128GB", offer_category="Tecnologia",
                        seek_item="MacBook Air M1", seek_category="Computadoras",
                        status="open", match_percent=85,
                        username="carlos.dev", user_initials="CD", timestamp="hace 3h",
                    ),
                    ft.Container(width=SPACE_LG),
                    marketplace_barter_card(
                        offer_item="Clases de Guitarra", offer_category="Educacion",
                        seek_item="Clases de Ingles", seek_category="Idiomas",
                        status="negotiating", match_percent=62,
                        username="ana.mtz", user_initials="AM", timestamp="hace 6h",
                    ),
                ],
                spacing=0, wrap=True, run_spacing=SPACE_MD,
            ),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


def _render_reservation_card():
    return ft.Column(
        [
            _section_title("Reservation Card", "Card de reserva con fecha destacada y estados"),
            ft.Row(
                [
                    reservation_card(
                        service_name="Masaje Relajante 60min",
                        provider_name="Spa Serenidad", provider_initials="SS",
                        rating=4.7, day="15", month="JUN", year="2026",
                        time="3:00 PM", duration="1h",
                        location="Av. Principal 123, La Paz",
                        status="confirmed", price="Bs. 180",
                    ),
                    ft.Container(width=SPACE_LG),
                    reservation_card(
                        service_name="Corte de Cabello Premium",
                        provider_name="Barberia Elite", provider_initials="BE",
                        rating=4.9, day="18", month="JUN", year="2026",
                        time="10:30 AM", duration="45m",
                        location="Calle Secundaria 456",
                        status="pending", price="Bs. 65",
                    ),
                ],
                spacing=0, wrap=True, run_spacing=SPACE_MD,
            ),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


def _render_cart_item():
    return ft.Column(
        [
            _section_title("Cart Item", "Fila de carrito con imagen, stepper de cantidad y subtotal"),
            cart_item(product_name="Audifonos Premium Noise Cancelling", variant="Negro mate", unit_price=129.99, original_price=179.99, quantity=2),
            ft.Container(height=SPACE_MD),
            cart_item(product_name="Camiseta Algodon Organico", variant="Blanco / Talla M", unit_price=29.99, quantity=3),
            ft.Container(height=SPACE_MD),
            cart_item(product_name="Teclado Mecanico RGB", variant="Switch Brown", unit_price=89.99, quantity=1),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


def _render_wishlist_heart():
    return ft.Column(
        [
            _section_title("Wishlist Heart", "Boton de favorito con contador y estados liked/unliked"),
            ft.Container(height=SPACE_MD),
            ft.Row(
                [
                    wishlist_heart(liked=True, count=128),
                    ft.Container(width=SPACE_XL),
                    wishlist_heart(liked=False, count=42),
                    ft.Container(width=SPACE_XL),
                    wishlist_heart(liked=True, count=1547, size=48),
                ],
            ),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


def _render_reel_thumbnail():
    return ft.Column(
        [
            _section_title("Reel Thumbnail", "Thumbnail de video corto vertical 9:16"),
            ft.Row(
                [
                    reel_thumbnail(video_title="Mi nuevo setup 2026", views=45200, duration="0:32"),
                    ft.Container(width=SPACE_LG),
                    reel_thumbnail(video_title="Tutorial: Como usar el marketplace", views=1280000, duration="1:45"),
                    ft.Container(width=SPACE_LG),
                    reel_thumbnail(video_title="Unboxing sorpresa", views=8700, duration="0:15"),
                ],
                spacing=0, wrap=True, run_spacing=SPACE_MD,
            ),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


def _render_search_bar():
    return ft.Column(
        [
            _section_title("Search Bar Premium", "Barra de busqueda con borde gradiente y filtros"),
            ft.Container(
                content=search_bar_premium(
                    placeholder="Buscar productos, servicios...",
                    recent_searches=["Audifonos bluetooth", "Camisetas algodon", "Diseno grafico", "Clases de guitarra"],
                    filters=["Categoria", "Precio", "Ubicacion", "Rating"],
                ),
                width=500,
            ),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


def _render_calendar_heatmap():
    return ft.Column(
        [
            _section_title("Calendar Heatmap", "Mapa de calor de actividad tipo GitHub"),
            calendar_heatmap(weeks=20),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


def _render_avatar_group():
    users = [
        {"initials": "ML", "name": "Maria Lopez"},
        {"initials": "CD", "name": "Carlos Dev"},
        {"initials": "AM", "name": "Ana Martinez"},
        {"initials": "PS", "name": "Pedro Sanchez"},
        {"initials": "LG", "name": "Laura Gomez"},
        {"initials": "DR", "name": "Diego Ruiz"},
        {"initials": "SM", "name": "Sofia Mendez"},
    ]
    return ft.Column(
        [
            _section_title("User Avatar Group", "Grupo de avatares solapados con contador +N"),
            ft.Container(height=SPACE_MD),
            ft.Text("Grupo de avatares (4 visibles)", size=F_CAPTION, color=C.TEXT_DIM),
            ft.Container(height=SPACE_SM),
            user_avatar_group(users, max_visible=4, size=36),
            ft.Container(height=SPACE_XL),
            ft.Text("Con label descriptivo", size=F_CAPTION, color=C.TEXT_DIM),
            ft.Container(height=SPACE_SM),
            user_avatar_label_group(users, label="les gusta esto", max_visible=3, size=32),
            ft.Container(height=SPACE_XL),
            ft.Text("Solo 2 usuarios", size=F_CAPTION, color=C.TEXT_DIM),
            ft.Container(height=SPACE_SM),
            user_avatar_label_group(users[:2], label="comentaron", max_visible=3, size=32),
        ],
        spacing=0, scroll=ft.ScrollMode.AUTO,
    )


class ShowcasePage:
    def build(self, page: ft.Page) -> ft.Container:
        return showcase_content(page)
