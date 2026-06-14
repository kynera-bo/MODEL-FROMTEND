import flet as ft
from theme import C, F_H3, F_BODY, F_CAPTION, F_LABEL
from theme import SPACE_SM, SPACE_MD
from theme import RADIUS_MD, RADIUS_LG, RADIUS_XL, RADIUS_PILL
from theme import pad, _b, icon, CENT
from features.showcase.showcase.ui.widgets.story_ring import story_group
from features.showcase.showcase.ui.widgets.post_card import post_card
from features.showcase.showcase.ui.widgets.marketplace_product_card import marketplace_product_card
from features.showcase.showcase.ui.widgets.marketplace_service_card import marketplace_service_card


STORY_DATA = [
    {"initials": "T", "label": "tu historia", "is_add": True},
    {"initials": "M", "label": "maria_lopez", "seen": False},
    {"initials": "C", "label": "carlos_r", "seen": False},
    {"initials": "A", "label": "ana_garcia", "seen": True},
    {"initials": "J", "label": "jose_m", "seen": False},
    {"initials": "L", "label": "laura_v", "seen": True},
    {"initials": "P", "label": "pedro_h", "seen": False},
    {"initials": "S", "label": "sofia_k", "seen": True},
]

PRODUCTS = [
    {"product_name": "Audifonos Premium", "price": "$129.99", "original_price": "$199.99", "image_url": "https://picsum.photos/seed/prod1/400/400", "rating": 4.8, "review_count": 342, "category": "Electronica", "seller_name": "TechStore", "seller_initials": "TS", "free_shipping": True, "orders_count": 2847},
    {"product_name": "Mochila Urbana 45L", "price": "$89.99", "image_url": "https://picsum.photos/seed/prod2/400/400", "rating": 4.6, "review_count": 215, "category": "Accesorios", "seller_name": "UrbanGear", "seller_initials": "UG", "orders_count": 1532},
    {"product_name": "Reloj Deportivo Pro", "price": "$249.99", "original_price": "$329.99", "image_url": "https://picsum.photos/seed/prod3/400/400", "rating": 4.9, "review_count": 528, "category": "Deportes", "seller_name": "FitTech", "seller_initials": "FT", "free_shipping": True, "orders_count": 4210},
    {"product_name": "Camara 4K Ultra HD", "price": "$459.99", "image_url": "https://picsum.photos/seed/prod4/400/400", "rating": 4.7, "review_count": 167, "category": "Tecnologia", "seller_name": "PhotoPro", "seller_initials": "PP", "orders_count": 893},
    {"product_name": "Silla Ergonómica", "price": "$349.99", "original_price": "$449.99", "image_url": "https://picsum.photos/seed/prod5/400/400", "rating": 4.5, "review_count": 89, "category": "Hogar", "seller_name": "ComfortPlus", "seller_initials": "CP", "free_shipping": True, "orders_count": 2105},
    {"product_name": "Kit Herramientas 200pz", "price": "$59.99", "image_url": "https://picsum.photos/seed/prod6/400/400", "rating": 4.4, "review_count": 432, "category": "Herramientas", "seller_name": "ToolMasters", "seller_initials": "TM", "orders_count": 5631},
]

SERVICES = [
    {"title": "Diseno Grafico Profesional", "description": "Logos, branding, social media. Resultados profesionales en 48h.", "icon_name": "brush", "tags": ["Branding", "Social Media"], "price_label": "Desde $50/h", "provider_name": "Ana Martinez", "provider_initials": "AM", "rating": 4.9, "review_count": 128, "location": "Remoto / NYC", "response_time": "< 1h", "image_url": "https://picsum.photos/seed/serv1/600/300"},
    {"title": "Desarrollo Web Full Stack", "description": "Sitios web, apps, APIs. React, Python, Node.js.", "icon_name": "code", "tags": ["Web", "Full Stack"], "price_label": "Desde $80/h", "provider_name": "Carlos Ruiz", "provider_initials": "CR", "rating": 4.8, "review_count": 94, "location": "Remoto / CDMX", "response_time": "< 2h", "image_url": "https://picsum.photos/seed/serv2/600/300"},
    {"title": "Consultoria Marketing Digital", "description": "Estrategia, SEO, Ads, redes sociales para tu negocio.", "icon_name": "trending_up", "tags": ["SEO", "Ads"], "price_label": "Desde $120/h", "provider_name": "Laura Vega", "provider_initials": "LV", "rating": 4.9, "review_count": 210, "location": "Remoto / Madrid", "response_time": "< 30min", "image_url": "https://picsum.photos/seed/serv3/600/300"},
]

NOTIFICATIONS = [
    {"icon_name": "favorite", "text": "A Maria Lopez le gustó tu publicación", "time": "2 min", "icon_color": C.ERROR},
    {"icon_name": "chat", "text": "Carlos Ruiz te envió un mensaje", "time": "15 min", "icon_color": C.ACCENT},
    {"icon_name": "shopping_bag", "text": "Pedido #1234 confirmado — Audifonos", "time": "1 h", "icon_color": C.SUCCESS},
    {"icon_name": "notifications", "text": "Recordatorio: Junta directiva mañana", "time": "3 h", "icon_color": C.ACCENT},
]

MESSAGES = [
    {"name": "Maria Lopez", "message": "Te envie los documentos", "time": "10:32", "unread": 3, "online": True},
    {"name": "Carlos Ruiz", "message": "Perfecto, nos vemos a las 5", "time": "9:15", "online": True},
    {"name": "Ana Garcia", "message": "El reporte esta listo para revisar", "time": "ayer", "unread": 1},
]

PURCHASES = [
    {"item": "Audifonos Premium", "price": "$129.99", "status": "En camino", "status_color": C.ACCENT, "date": "12 jun"},
    {"item": "Mochila Urbana", "price": "$89.99", "status": "Entregado", "status_color": C.SUCCESS, "date": "8 jun"},
]


def _section_label(text: str) -> ft.Container:
    return ft.Container(
        content=ft.Row([
            ft.Text(text, size=F_H3, weight=ft.FontWeight.BOLD, color=C.TEXT),
            ft.Container(expand=True),
            ft.Text("Ver todo", size=F_CAPTION, color=C.ACCENT),
        ]),
        padding=pad(v=0, h=0),
    )


def _stat_card(icon_name: str, value: str, label: str) -> ft.Container:
    return ft.Container(
        content=ft.Column([
            icon(icon_name, size=20, color=C.ACCENT),
            ft.Container(height=6),
            ft.Text(value, size=F_H3, weight=ft.FontWeight.BOLD, color=C.TEXT),
            ft.Text(label, size=F_CAPTION, color=C.TEXT_DIM),
        ], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER, tight=True),
        bgcolor=C.SURFACE, border=_b(1, C.BORDER),
        border_radius=RADIUS_LG, padding=pad(v=12, h=SPACE_SM),
        ink=True, height=88,
    )


def _compact_notif(icon_name: str, text: str, time: str, icon_color: str) -> ft.Container:
    return ft.Container(
        content=ft.Row([
            ft.Container(content=icon(icon_name, size=15, color=icon_color), width=26, alignment=CENT),
            ft.Column([
                ft.Text(text, size=F_CAPTION, color=C.TEXT, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
            ], spacing=0, expand=True),
            ft.Text(time, size=F_LABEL, color=C.TEXT_DIM),
        ], spacing=6, vertical_alignment=ft.CrossAxisAlignment.CENTER),
        padding=pad(v=5, h=0), ink=True,
    )


def _compact_contact(name: str, message: str, time: str, unread: int = 0, online: bool = False) -> ft.Container:
    initials = "".join(w[0] for w in name.split()[:2]).upper()
    badge = None
    if unread > 0:
        badge = ft.Container(
            content=ft.Text(str(unread) if unread < 100 else "99+", size=F_LABEL, color=C.BG, weight="bold", text_align=ft.TextAlign.CENTER),
            bgcolor=C.ERROR, border_radius=RADIUS_PILL, padding=pad(v=1, h=5),
        )
    dot = ft.Container(width=7, height=7, border_radius=4, bgcolor=C.ACCENT if online else C.TEXT_DIM, border=_b(1.5, C.SURFACE), offset=ft.Offset(0.6, 0.6))
    return ft.Container(
        content=ft.Row([
            ft.Stack([
                ft.Container(
                    content=ft.Text(initials, size=F_CAPTION, weight="bold", color=C.TEXT, text_align=ft.TextAlign.CENTER),
                    width=30, height=30, border_radius=15, bgcolor=C.AVATAR_BG, alignment=CENT, border=_b(1, C.BORDER),
                ),
                dot if online else ft.Container(width=7, height=7),
            ], width=30, height=30),
            ft.Column([
                ft.Text(name, size=F_CAPTION, weight="bold", color=C.TEXT, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                ft.Row([
                    ft.Text(message[:20] + "..." if len(message) > 20 else message, size=F_LABEL, color=C.TEXT_MUTED, expand=True, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Text(time, size=F_LABEL, color=C.TEXT_DIM),
                ], spacing=3),
            ], spacing=0, expand=True),
            badge or ft.Container(),
        ], spacing=6, vertical_alignment=ft.CrossAxisAlignment.CENTER),
        padding=pad(v=5, h=0), ink=True,
    )


def _compact_event(day: str, month: str, title: str, time_loc: str) -> ft.Container:
    return ft.Container(
        content=ft.Row([
            ft.Container(
                content=ft.Column([
                    ft.Text(day, size=15, weight="bold", color=C.TEXT, text_align=ft.TextAlign.CENTER),
                    ft.Text(month.upper(), size=F_LABEL, color=C.TEXT_DIM, text_align=ft.TextAlign.CENTER),
                ], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER, tight=True),
                width=36, height=36, border_radius=RADIUS_MD, bgcolor=C.ACCENT_FAINT, alignment=CENT,
            ),
            ft.Column([
                ft.Text(title, size=F_CAPTION, weight="bold", color=C.TEXT, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                ft.Text(time_loc, size=F_LABEL, color=C.TEXT_DIM, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
            ], spacing=0, expand=True),
        ], spacing=8, vertical_alignment=ft.CrossAxisAlignment.CENTER),
        padding=pad(v=5, h=0), ink=True,
    )


def _compact_purchase(item: str, price: str, status: str, status_color: str, date: str) -> ft.Container:
    return ft.Container(
        content=ft.Row([
            ft.Column([
                ft.Text(item, size=F_CAPTION, color=C.TEXT, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                ft.Text(f"{price} · {date}", size=F_LABEL, color=C.TEXT_DIM),
            ], spacing=0, expand=True),
            ft.Container(
                content=ft.Text(status, size=F_LABEL, color=status_color, weight="bold"),
                bgcolor=C.ACCENT_FAINT if status_color == C.ACCENT else C.SUCCESS_BG,
                border_radius=RADIUS_PILL, padding=pad(v=1, h=6),
            ),
        ], spacing=6, vertical_alignment=ft.CrossAxisAlignment.CENTER),
        padding=pad(v=5, h=0), ink=True,
    )


def _profile_summary() -> ft.Container:
    return ft.Container(
        content=ft.Row([
            ft.Container(
                content=ft.Text("K", size=F_H3, weight="bold", color=C.TEXT, text_align=ft.TextAlign.CENTER),
                width=38, height=38, border_radius=19, bgcolor=C.ACCENT_FAINT, alignment=CENT,
                border=_b(1.5, C.ACCENT),
            ),
            ft.Column([
                ft.Text("Kynera Dev", size=F_CAPTION, weight="bold", color=C.TEXT),
                ft.Text("Plan Premium", size=F_LABEL, color=C.ACCENT, weight="bold"),
            ], spacing=0, expand=True),
            ft.Container(
                content=icon("edit", size=15, color=C.TEXT_DIM),
                width=28, height=28, border_radius=14, bgcolor=C.SURFACE2, alignment=CENT, ink=True,
            ),
        ], spacing=8, vertical_alignment=ft.CrossAxisAlignment.CENTER),
        padding=pad(v=4, h=0), ink=True,
    )


def _sidebar_section(title: str, content: ft.Control) -> ft.Container:
    return ft.Container(
        content=ft.Column([
            ft.Text(title, size=F_BODY, weight=ft.FontWeight.BOLD, color=C.TEXT),
            ft.Container(height=8),
            content,
        ], spacing=0, tight=True),
        bgcolor=C.SURFACE,
        border_radius=RADIUS_XL, padding=pad(v=10, h=12),
    )


def home_content(page: ft.Page) -> ft.Container:
    is_desktop = True
    try:
        is_desktop = page.width >= 768 if page.width else True
    except Exception:
        pass

    stories = story_group(STORY_DATA)

    stats = ft.ResponsiveRow([
        ft.Container(_stat_card("people_outlined", "12.4K", "Seguidores"), col={"xs": 6, "sm": 6, "md": 3, "lg": 3}),
        ft.Container(_stat_card("schedule", "847", "Horas"), col={"xs": 6, "sm": 6, "md": 3, "lg": 3}),
        ft.Container(_stat_card("star_border", "4.8", "Rating"), col={"xs": 6, "sm": 6, "md": 3, "lg": 3}),
        ft.Container(_stat_card("people_outlined", "3.2K", "Contactos"), col={"xs": 6, "sm": 6, "md": 3, "lg": 3}),
    ], spacing=8, run_spacing=8)

    posts = ft.Column([
        post_card(
            username="maria.lopez", display_name="Maria Lopez",
            avatar_initials="ML", timestamp="2 horas",
            content="Acabo de descubrir este marketplace increible! Los productos son de primera calidad y la experiencia de compra es simplemente genial.",
            image_url="https://picsum.photos/seed/post1/600/400",
            likes_count=2847, liked=True,
        ),
        ft.Container(height=SPACE_MD),
        post_card(
            username="carlos.r", display_name="Carlos Ruiz",
            avatar_initials="CR", timestamp="5 horas",
            content="Nuevo proyecto en marcha! Muy emocionado por lo que viene. Gracias a todo el equipo.",
            image_url="https://picsum.photos/seed/post2/600/400",
            likes_count=1523, liked=False,
        ),
        ft.Container(height=SPACE_MD),
        post_card(
            username="ana_garcia", display_name="Ana Garcia",
            avatar_initials="AG", timestamp="1 dia",
            content="Evento exclusivo esta noche. Vamos a celebrar los logros de este trimestre.",
            image_url=None,
            likes_count=892, liked=False,
        ),
    ], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    products_grid = ft.GridView(
        max_extent=340,
        child_aspect_ratio=1.0,
        spacing=12,
        run_spacing=12,
        controls=[marketplace_product_card(**p) for p in PRODUCTS],
    )

    services_grid = ft.GridView(
        max_extent=340,
        child_aspect_ratio=1.0,
        spacing=12,
        run_spacing=12,
        controls=[marketplace_service_card(**s) for s in SERVICES],
    )

    notifications = ft.Column([_compact_notif(**n) for n in NOTIFICATIONS], spacing=0)
    contacts = ft.Column([_compact_contact(**c) for c in MESSAGES], spacing=0)
    purchases = ft.Column([_compact_purchase(**p) for p in PURCHASES], spacing=0)
    events = ft.Column([
        _compact_event("15", "JUN", "Junta directiva", "10:00 AM · Sala principal"),
        _compact_event("18", "JUN", "Workshop UX", "3:00 PM · Sala B"),
    ], spacing=3)

    right_bar = ft.Column([
        ft.Container(height=8),
        _sidebar_section("Perfil", _profile_summary()),
        ft.Container(height=8),
        _sidebar_section("Notificaciones", notifications),
        ft.Container(height=8),
        _sidebar_section("Mensajes", contacts),
        ft.Container(height=8),
        _sidebar_section("Compras recientes", purchases),
        ft.Container(height=8),
        _sidebar_section("Proximos eventos", events),
        ft.Container(height=20),
    ], spacing=0, tight=True, scroll=ft.ScrollMode.AUTO, expand=True)

    right_container = ft.Container(content=right_bar, width=280)

    feed = ft.Column([
        ft.Container(height=SPACE_MD),
        _section_label("Estadisticas"),
        ft.Container(height=SPACE_SM),
        stats,
        ft.Container(height=20),
        _section_label("Historias"),
        ft.Container(height=SPACE_SM),
        stories,
        ft.Container(height=20),
        _section_label("Publicaciones"),
        ft.Container(height=SPACE_SM),
        posts,
        ft.Container(height=20),
        _section_label("Productos"),
        ft.Container(height=SPACE_SM),
        products_grid,
        ft.Container(height=20),
        _section_label("Servicios"),
        ft.Container(height=SPACE_SM),
        services_grid,
        ft.Container(height=40),
    ], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       scroll=ft.ScrollMode.AUTO, expand=True)

    if is_desktop:
        feed_container = ft.Container(content=feed, expand=True, padding=pad(l=16))
        return feed_container, right_container
    else:
        return ft.Container(content=feed, expand=True), None


class DashboardPage:
    def build(self, page: ft.Page) -> tuple:
        return home_content(page)


dashboard_content = home_content
