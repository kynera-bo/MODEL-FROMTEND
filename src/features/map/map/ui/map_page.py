import flet as ft
import flet_map as ftm
import flet_geolocator as ftg
from theme import C, SPACE_XXL, pad, RADIUS_MD
from adapters.routing_adapter import get_route

INITIAL_LAT = 40.7128
INITIAL_LNG = -74.0060
INITIAL_ZOOM = 11

BUSINESSES = [
    {"id": "b1", "name": "Café Central", "photo": "https://picsum.photos/seed/cafe1/200/150", "lat": 40.714, "lng": -74.007},
    {"id": "b2", "name": "Librería NY", "photo": "https://picsum.photos/seed/libro1/200/150", "lat": 40.713, "lng": -74.008},
    {"id": "b3", "name": "Pizza Italia", "photo": "https://picsum.photos/seed/pizza1/200/150", "lat": 40.711, "lng": -74.005},
    {"id": "b4", "name": "Gimnasio Fit", "photo": "https://picsum.photos/seed/gym1/200/150", "lat": 40.715, "lng": -74.004},
    {"id": "b5", "name": "Farmacia 24h", "photo": "https://picsum.photos/seed/farma1/200/150", "lat": 40.710, "lng": -74.009},
]


def _near(lat1, lng1, lat2, lng2, eps=0.002):
    return abs(lat1 - lat2) < eps and abs(lng1 - lng2) < eps


def map_content(page: ft.Page) -> ft.Container:

    status_ref = ft.Ref[ft.Text]()
    event_ref = ft.Ref[ft.Text]()
    map_ref = ft.Ref[ftm.Map]()
    marker_ref = ft.Ref[ftm.MarkerLayer]()
    biz_ref = ft.Ref[ftm.MarkerLayer]()
    my_ref = ft.Ref[ftm.MarkerLayer]()
    route_line_ref = ft.Ref[ftm.PolylineLayer]()
    biz_name_ref = ft.Ref[ft.TextField]()
    form_ref = ft.Ref[ft.Container]()
    geo = getattr(page, "_geolocator", None)
    tap_circles = []
    pending_biz_coords: list[tuple[float, float] | None] = [None]
    businesses = list(BUSINESSES)
    tracking = [False]
    my_pos: list[tuple[float, float] | None] = [None]
    route_to_here_active = [False]
    my_route_line_ref = ft.Ref[ftm.PolylineLayer]()
    dest_marker_ref = ft.Ref[ftm.MarkerLayer]()

    def _rebuild_biz_markers():
        if not biz_ref.current:
            return
        ms = []
        for b in businesses:
            ms.append(ftm.Marker(
                content=ft.Container(
                    content=ft.Row([
                        ft.Icon(ft.Icons.STORE, color=C.ACCENT, size=16),
                        ft.Text(b["name"][:10], size=9, color=C.TEXT, no_wrap=True),
                    ], spacing=2),
                    bgcolor=C.SURFACE, border_radius=8, padding=pad(v=2, h=6),
                ),
                coordinates=ftm.MapLatitudeLongitude(latitude=b["lat"], longitude=b["lng"]),
                width=80, height=26,
            ))
        biz_ref.current.markers = ms
        page.update()

    def st(msg):
        if status_ref.current:
            status_ref.current.value = msg
            page.update()

    business_layer = ftm.MarkerLayer(ref=biz_ref, markers=[])
    my_layer = ftm.MarkerLayer(ref=my_ref, markers=[])
    dest_layer = ftm.MarkerLayer(ref=dest_marker_ref, markers=[])
    route_line_layer = ftm.PolylineLayer(ref=route_line_ref, polylines=[])
    my_route_layer = ftm.PolylineLayer(ref=my_route_line_ref, polylines=[])
    marker_layer = ftm.MarkerLayer(
        ref=marker_ref,
        markers=[
            ftm.Marker(
                content=ft.Icon(ft.Icons.LOCATION_ON, color=ft.Colors.RED),
                coordinates=ftm.MapLatitudeLongitude(latitude=40.7128, longitude=-74.0060),
            ),
        ],
    )
    _rebuild_biz_markers()

    circle_ref = ft.Ref[ftm.CircleLayer]()
    initial_circle = ftm.CircleMarker(
        radius=10,
        coordinates=ftm.MapLatitudeLongitude(latitude=40.72, longitude=-74.01),
        color=ft.Colors.with_opacity(0.3, ft.Colors.BLUE),
        border_color=ft.Colors.BLUE,
        border_stroke_width=3,
    )
    circle_layer = ftm.CircleLayer(
        ref=circle_ref,
        circles=[initial_circle],
    )

    polygon_layer = ftm.PolygonLayer(
        polygons=[
            ftm.PolygonMarker(
                label="Sector",
                label_text_style=ft.TextStyle(
                    color=ft.Colors.BLACK, size=13, weight=ft.FontWeight.BOLD,
                ),
                color=ft.Colors.with_opacity(0.3, ft.Colors.GREEN),
                coordinates=[
                    ftm.MapLatitudeLongitude(latitude=40.72, longitude=-74.02),
                    ftm.MapLatitudeLongitude(latitude=40.72, longitude=-73.99),
                    ftm.MapLatitudeLongitude(latitude=40.70, longitude=-73.99),
                    ftm.MapLatitudeLongitude(latitude=40.70, longitude=-74.02),
                ],
            ),
        ],
    )

    polyline_layer = ftm.PolylineLayer(
        polylines=[
            ftm.PolylineMarker(
                stroke_width=4,
                border_stroke_width=1,
                border_color=ft.Colors.WHITE,
                color=ft.Colors.BLUE,
                stroke_pattern=ftm.SolidStrokePattern(),
                coordinates=[
                    ftm.MapLatitudeLongitude(latitude=40.72, longitude=-74.02),
                    ftm.MapLatitudeLongitude(latitude=40.71, longitude=-74.01),
                    ftm.MapLatitudeLongitude(latitude=40.70, longitude=-74.00),
                ],
            ),
            ftm.PolylineMarker(
                stroke_width=4,
                border_stroke_width=1,
                border_color=ft.Colors.WHITE,
                color=ft.Colors.RED,
                stroke_pattern=ftm.DashedStrokePattern(segments=[20, 10]),
                coordinates=[
                    ftm.MapLatitudeLongitude(latitude=40.70, longitude=-74.00),
                    ftm.MapLatitudeLongitude(latitude=40.69, longitude=-73.99),
                    ftm.MapLatitudeLongitude(latitude=40.68, longitude=-73.98),
                ],
            ),
            ftm.PolylineMarker(
                stroke_width=4,
                border_stroke_width=1,
                border_color=ft.Colors.WHITE,
                color=ft.Colors.GREEN,
                stroke_pattern=ftm.DottedStrokePattern(spacing_factor=2.0),
                coordinates=[
                    ftm.MapLatitudeLongitude(latitude=40.68, longitude=-73.98),
                    ftm.MapLatitudeLongitude(latitude=40.67, longitude=-73.97),
                    ftm.MapLatitudeLongitude(latitude=40.66, longitude=-73.96),
                ],
            ),
        ],
    )

    overlay_layer = ftm.OverlayImageLayer(
        overlay_images=[
            ftm.OverlayImage(
                src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/OpenStreetMap_logo.svg/200px-OpenStreetMap_logo.svg.png",
                opacity=0.5,
                bounds=ftm.MapLatitudeLongitudeBounds(
                    corner_1=ftm.MapLatitudeLongitude(latitude=40.74, longitude=-74.03),
                    corner_2=ftm.MapLatitudeLongitude(latitude=40.69, longitude=-73.97),
                ),
            ),
        ],
    )

    async def _route_businesses(e):
        if len(businesses) < 2:
            st("Se necesitan al menos 2 negocios para crear una ruta")
            return
        st(f"Calculando ruta entre {len(businesses)} negocios...")
        try:
            points = [(b["lat"], b["lng"]) for b in businesses]
            result = await get_route(points)
            coords = [
                ftm.MapLatitudeLongitude(latitude=lat, longitude=lng)
                for lat, lng in result.coordinates
            ]
            if route_line_ref.current:
                route_line_ref.current.polylines = [
                    ftm.PolylineMarker(
                        stroke_width=5,
                        border_stroke_width=1.5,
                        border_color=ft.Colors.WHITE,
                        color=C.ACCENT,
                        stroke_pattern=ftm.SolidStrokePattern(),
                        coordinates=coords,
                    ),
                ]
                page.update()
            st(f"Ruta: {result.distance_km} km · {result.duration_min} min")
        except Exception as ex:
            st(f"Error al calcular ruta: {ex}")

    def _clear_route(e):
        if route_line_ref.current:
            route_line_ref.current.polylines = []
        if my_route_line_ref.current:
            my_route_line_ref.current.polylines = []
        if dest_marker_ref.current:
            dest_marker_ref.current.markers = []
        page.update()
        st("Rutas eliminadas")

    def _toggle_route_to_here(e):
        route_to_here_active[0] = not route_to_here_active[0]
        if route_to_here_active[0]:
            st("Modo ruta: toca el mapa para marcar destino")
        else:
            st("Modo ruta desactivado")

    async def _route_to_here(dest_lat: float, dest_lng: float):
        st("Obteniendo ubicación...")
        try:
            if geo and my_pos[0] is None:
                p = await geo.get_current_position()
                my_pos[0] = (p.latitude, p.longitude)
            origin = my_pos[0]
            if origin is None:
                st("No se pudo obtener tu ubicación. Activa GPS primero.")
                return
            st("Calculando ruta...")
            result = await get_route([origin, (dest_lat, dest_lng)])
            coords = [
                ftm.MapLatitudeLongitude(latitude=lat, longitude=lng)
                for lat, lng in result.coordinates
            ]
            if my_route_line_ref.current:
                my_route_line_ref.current.polylines = [
                    ftm.PolylineMarker(
                        stroke_width=5,
                        border_stroke_width=1.5,
                        border_color=ft.Colors.WHITE,
                        color=ft.Colors.GREEN,
                        stroke_pattern=ftm.SolidStrokePattern(),
                        coordinates=coords,
                    ),
                ]
            if dest_marker_ref.current:
                dest_marker_ref.current.markers = [
                    ftm.Marker(
                        content=ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.Icons.LOCATION_ON, color=ft.Colors.RED, size=18),
                                ft.Text("Destino", size=9, color=C.TEXT, no_wrap=True),
                            ], spacing=2),
                            bgcolor=C.SURFACE, border_radius=8, padding=pad(v=2, h=6),
                        ),
                        coordinates=ftm.MapLatitudeLongitude(latitude=dest_lat, longitude=dest_lng),
                        width=80, height=26,
                    ),
                ]
            page.update()
            st(f"Ruta desde ubicación: {result.distance_km} km · {result.duration_min} min")
        except Exception as ex:
            st(f"Error: {ex}")
            route_to_here_active[0] = False

    def on_hover(e: ftm.MapHoverEvent):
        if event_ref.current:
            event_ref.current.value = "hover"
            page.update()

    def on_pointer_down(e: ftm.MapPointerEvent):
        if event_ref.current:
            event_ref.current.value = "ptr_down"
            page.update()

    def on_pointer_up(e: ftm.MapPointerEvent):
        if event_ref.current:
            event_ref.current.value = "ptr_up"
            page.update()

    def on_long_press(e: ftm.MapTapEvent):
        tap_circles.append(
            ftm.CircleMarker(
                radius=8,
                coordinates=e.coordinates,
                color=ft.Colors.with_opacity(0.5, ft.Colors.RED),
                border_color=ft.Colors.RED,
                border_stroke_width=2,
            )
        )
        if circle_ref.current:
            circle_ref.current.circles = tap_circles + [initial_circle]
            page.update()
        st(f"long press ({e.coordinates.latitude:.4f}, {e.coordinates.longitude:.4f})")

    def on_tap(e: ftm.MapTapEvent):
        tap_circles.append(
            ftm.CircleMarker(
                radius=4,
                coordinates=e.coordinates,
                color=ft.Colors.with_opacity(0.6, ft.Colors.CYAN),
                border_color=ft.Colors.CYAN,
                border_stroke_width=1,
            )
        )
        if circle_ref.current:
            circle_ref.current.circles = tap_circles + [initial_circle]
            page.update()
        _set_pending_coords(e)
        lat, lng = e.coordinates.latitude, e.coordinates.longitude
        for b in businesses:
            if _near(lat, lng, b["lat"], b["lng"]):
                _show_biz_popup(b)
                return
        if route_to_here_active[0]:
            page.run_task(_route_to_here, lat, lng)
            return
        st(f"({lat:.4f}, {lng:.4f})")

    def on_secondary_tap(e: ftm.MapTapEvent):
        if marker_ref.current:
            ms = list(marker_ref.current.markers)
            ms.append(
                ftm.Marker(
                    content=ft.Icon(ft.Icons.FLAG, color=ft.Colors.ORANGE, size=20),
                    coordinates=e.coordinates,
                )
            )
            marker_ref.current.markers = ms
            page.update()
        st(f"(derecha {e.coordinates.latitude:.4f}, {e.coordinates.longitude:.4f})")

    def on_event(e: ftm.MapEvent):
        important = {"tap", "secondaryTap", "longPress", "doubleTapZoom", "rotateStart", "rotateEnd", "hover"}
        if e.source and e.source.value in important and event_ref.current:
            event_ref.current.value = e.source.value
            page.update()

    def on_position_change(e: ftm.MapPositionChangeEvent):
        st(f"Zoom {e.camera.zoom:.1f} | ({e.coordinates.latitude:.4f}, {e.coordinates.longitude:.4f})")

    async def gps(e):
        st("GPS: obteniendo posición...")
        try:
            if not geo:
                st("Error: Geolocator no disponible")
                return
            p = await geo.get_current_position()
            lat, lng = p.latitude, p.longitude
            my_pos[0] = (lat, lng)
            if marker_ref.current:
                marker_ref.current.markers = [
                    ftm.Marker(
                        content=ft.Icon(ft.Icons.MY_LOCATION, color=ft.Colors.BLUE, size=28),
                        coordinates=ftm.MapLatitudeLongitude(latitude=lat, longitude=lng),
                    ),
                ]
                page.update()
            if map_ref.current:
                await map_ref.current.center_on(
                    ftm.MapLatitudeLongitude(latitude=lat, longitude=lng), 15,
                )
            st(f"GPS: {lat:.5f}, {lng:.5f}")
        except Exception as ex:
            st(f"Error GPS: {ex}")

    def _on_my_position(e: ftg.GeolocatorPositionChangeEvent):
        if not tracking[0]:
            return
        lat, lng = e.position.latitude, e.position.longitude
        if my_ref.current:
            my_ref.current.markers = [
                ftm.Marker(
                    content=ft.Icon(ft.Icons.MY_LOCATION, color=ft.Colors.BLUE, size=28),
                    coordinates=ftm.MapLatitudeLongitude(latitude=lat, longitude=lng),
                ),
            ]
            page.update()

    async def _toggle_tracking(e):
        if not geo:
            st("Geolocator no disponible")
            return
        if tracking[0]:
            tracking[0] = False
            geo.on_position_change = None
            if my_ref.current:
                my_ref.current.markers = []
                page.update()
            st("Tracking detenido")
            return
        st("Iniciando seguimiento...")
        try:
            geo.on_position_change = _on_my_position
            p = await geo.get_current_position()
            lat, lng = p.latitude, p.longitude
            my_pos[0] = (lat, lng)
            tracking[0] = True
            if my_ref.current:
                my_ref.current.markers = [
                    ftm.Marker(
                        content=ft.Icon(ft.Icons.MY_LOCATION, color=ft.Colors.BLUE, size=28),
                        coordinates=ftm.MapLatitudeLongitude(latitude=lat, longitude=lng),
                    ),
                ]
                page.update()
            if map_ref.current:
                await map_ref.current.center_on(
                    ftm.MapLatitudeLongitude(latitude=lat, longitude=lng), 15,
                )
            st("Tracking activo — mover para actualizar")
        except Exception as ex:
            st(f"Error tracking: {ex}")

    async def reset_view(e):
        ml = map_ref.current
        if ml:
            await ml.center_on(
                ftm.MapLatitudeLongitude(latitude=INITIAL_LAT, longitude=INITIAL_LNG),
                INITIAL_ZOOM,
            )

    def _show_biz_popup(b):
        def on_visit(e):
            print(f"NEGOCIO: {b['name']} (id={b['id']})")
            dlg.open = False
            page.update()

        def on_delete(e):
            businesses[:] = [x for x in businesses if x["id"] != b["id"]]
            _rebuild_biz_markers()
            dlg.open = False
            page.update()
            st(f"Eliminado: {b['name']}")

        dlg = ft.AlertDialog(
            title=ft.Text(b["name"], weight=ft.FontWeight.BOLD),
            content=ft.Column([
                ft.Image(src=b["photo"], width=200, height=150, fit=ft.BoxFit.COVER, border_radius=8),
                ft.Container(height=4),
                ft.Text(f"ID: {b['id']}", size=11, color=C.TEXT_MUTED),
                ft.Row([
                    ft.Button("Visitar", on_click=on_visit, icon=ft.Icons.OPEN_IN_NEW),
                    ft.TextButton("Eliminar", on_click=on_delete, icon=ft.Icons.DELETE, style=ft.ButtonStyle(color=ft.Colors.RED)),
                ], spacing=8),
            ], spacing=4, width=220, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        )
        page.show_dialog(dlg)

    def _toggle_form(e):
        if form_ref.current:
            form_ref.current.visible = not form_ref.current.visible
            page.update()

    def _add_biz_from_form(e):
        name = (biz_name_ref.current.value or "").strip()
        coords = pending_biz_coords[0]
        if not name:
            st("Escribe un nombre")
            return
        if not coords:
            st("Primero da click en el mapa para ubicarlo")
            return
        bid = f"b{len(businesses) + 1}"
        businesses.append({"id": bid, "name": name, "photo": f"https://picsum.photos/seed/{bid}/200/150", "lat": coords[0], "lng": coords[1]})
        _rebuild_biz_markers()
        biz_name_ref.current.value = ""
        pending_biz_coords[0] = None
        st(f"Agregado: {name}")

    def _set_pending_coords(e: ftm.MapTapEvent):
        if form_ref.current and form_ref.current.visible:
            pending_biz_coords[0] = (e.coordinates.latitude, e.coordinates.longitude)
            st(f"Ubicación: {e.coordinates.latitude:.4f}, {e.coordinates.longitude:.4f}")

    my_map = ftm.Map(
        ref=map_ref,
        expand=True,
        initial_center=ftm.MapLatitudeLongitude(latitude=INITIAL_LAT, longitude=INITIAL_LNG),
        initial_zoom=INITIAL_ZOOM,
        max_zoom=18,
        min_zoom=3,
        initial_camera_fit=ftm.CameraFit(
            bounds=ftm.MapLatitudeLongitudeBounds(
                corner_1=ftm.MapLatitudeLongitude(latitude=40.74, longitude=-74.03),
                corner_2=ftm.MapLatitudeLongitude(latitude=40.68, longitude=-73.96),
            ),
        ),
        interaction_configuration=ftm.InteractionConfiguration(
            flags=ftm.InteractionFlag.ALL
        ),
        on_tap=on_tap,
        on_secondary_tap=on_secondary_tap,
        on_long_press=on_long_press,
        on_hover=on_hover,
        on_pointer_down=on_pointer_down,
        on_pointer_up=on_pointer_up,
        on_pointer_cancel=on_pointer_up,
        on_event=on_event,
        on_position_change=on_position_change,
        layers=[
            ftm.TileLayer(
                url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                user_agent_package_name="GestosApp",
            ),
            ftm.RichAttribution(
                attributions=[
                    ftm.TextSourceAttribution(
                        text="OpenStreetMap contributors",
                        prepend_copyright=False,
                        on_click=lambda e: page.launch_url("https://www.openstreetmap.org/copyright"),
                    ),
                ],
                alignment=ftm.AttributionAlignment.BOTTOM_LEFT,
                permanent_height=24,
            ),
            business_layer,
            my_layer,
            dest_layer,
            marker_layer,
            route_line_layer,
            my_route_layer,
            circle_layer,
            polygon_layer,
            polyline_layer,
            overlay_layer,
        ],
    )

    biz_form = ft.Container(
        ref=form_ref,
        visible=False,
        content=ft.Row([
            ft.TextField(ref=biz_name_ref, hint_text="Nombre del negocio", expand=True, height=36, text_size=13, border_radius=RADIUS_MD),
            ft.Button("Agregar", on_click=_add_biz_from_form, icon=ft.Icons.ADD, height=36),
        ], spacing=6),
        padding=pad(v=4, h=0),
    )

    top = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Text("Mapa", size=18, weight=ft.FontWeight.BOLD, color=C.TEXT),
                ft.Container(expand=True),
                ft.Button("Route Negocios", on_click=lambda e: page.run_task(_route_businesses, e), icon=ft.Icons.ROUTE, height=32, style=ft.ButtonStyle(bgcolor=C.ACCENT, color=ft.Colors.WHITE)),
                ft.TextButton("Route Here", on_click=_toggle_route_to_here),
                ft.TextButton("Clear", on_click=_clear_route),
                ft.TextButton("Negocios", on_click=_toggle_form),
                ft.TextButton("Compartir", on_click=lambda e: page.run_task(_toggle_tracking, e)),
                ft.TextButton("GPS", on_click=lambda e: page.run_task(gps, e)),
                ft.TextButton("Reset", on_click=lambda e: page.run_task(reset_view, e)),
            ]),
            biz_form,
        ]),
        padding=pad(v=8, h=0),
    )

    status = ft.Container(
        content=ft.Row([
            ft.Text(ref=status_ref, value="Listo.", size=11, color=C.TEXT_MUTED, expand=True),
            ft.Text(ref=event_ref, value="", size=11, color=C.ACCENT),
        ]),
        padding=pad(v=4, h=0),
    )

    return ft.Container(
        expand=True,
        padding=SPACE_XXL,
        content=ft.Column([
            top,
            ft.Container(expand=True, content=my_map),
            status,
        ], spacing=0, expand=True),
    )


class MapPage:
    def build(self, page: ft.Page) -> ft.Container:
        return map_content(page)
