import flet as ft


data = {
    "badge": "RELACIONES",
    "title": "Círculos de Dunbar",
    "primary": [
        {"name": "Albert", "initials": "AH"},
        {"name": "Maria", "initials": "MR"},
    ],
    "secondary": [
        {"name": "Carlos", "initials": "CR"},
        {"name": "Ana", "initials": "AN"},
    ],
    "community": [
        {"name": "Pedro", "initials": "PD"},
        {"name": "Luis", "initials": "LS"},
    ],
}




class PersonBubble(ft.Container):

    def __init__(self, initials, tooltip_text, text_color, ring_color):
        super().__init__()

        self.initials = initials

        self.content = ft.Text(
            initials,
            size=9,
            weight=ft.FontWeight.BOLD,
            color=text_color,
        )

        self.tooltip = tooltip_text

        self.width = 32
        self.height = 32
        self.border_radius = 100

        self.alignment = ft.alignment.center

        self.gradient = ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[
                "rgba(255,255,255,0.08)",
                "rgba(255,255,255,0.02)",
            ],
        )

        self.border = ft.border.all(
            1,
            ring_color,
        )

        self.animate_scale = ft.Animation(
            200,
            ft.AnimationCurve.EASE_OUT,
        )

        self.scale = 1

        self.on_hover = self._hover

    def _hover(self, e):
        self.scale = 1.2 if e.data == "true" else 1
        self.update()


def create_circle(
    size,
    people,
    ring_color,
    bg_color,
    text_color,
    max_people,
):
    items = []

    for person in people:
        items.append(
            PersonBubble(
                person["initials"],
                person["name"],
                text_color,
                ring_color,
            )
        )

    if len(people) < max_people:
        items.append(
            ft.Container(
                width=32,
                height=32,
                border_radius=100,
                alignment=ft.alignment.center,
                border=ft.border.all(
                    1,
                    "rgba(255,255,255,0.15)",
                ),
                content=ft.Text(
                    "+",
                    size=12,
                    color="rgba(255,255,255,0.4)",
                ),
            )
        )

    return ft.Container(
        width=size,
        height=size,
        border_radius=size,
        alignment=ft.alignment.center,
        bgcolor=bg_color,
        border=ft.border.all(
            1,
            ring_color,
        ),
        content=ft.Wrap(
            controls=items,
            spacing=6,
            run_spacing=6,
            alignment=ft.WrapAlignment.CENTER,
            run_alignment=ft.WrapAlignment.CENTER,
        ),
    )


def SlideDunbarCircles(data, is_active=True):

    circles = [
        {
            "level": "Primario",
            "max": 15,
            "color": "rgba(255,255,255,0.9)",
            "bg": "rgba(255,255,255,0.04)",
            "ring": "rgba(255,255,255,0.12)",
            "desc": "Familia y mejores amigos",
            "people": data["primary"],
        },
        {
            "level": "Secundario",
            "max": 50,
            "color": "rgba(255,255,255,0.5)",
            "bg": "rgba(255,255,255,0.02)",
            "ring": "rgba(255,255,255,0.06)",
            "desc": "Amigos activos y colegas",
            "people": data["secondary"],
        },
        {
            "level": "Comunitario",
            "max": 150,
            "color": "rgba(255,255,255,0.2)",
            "bg": "rgba(255,255,255,0.01)",
            "ring": "rgba(255,255,255,0.03)",
            "desc": "Conocidos y escenas",
            "people": data["community"],
        },
    ]

    sizes = [200, 320, 440]

    stack = ft.Stack(
        width=440,
        height=440,
        controls=[
            ft.Container(
                left=(440 - sizes[2]) / 2,
                top=(440 - sizes[2]) / 2,
                content=create_circle(
                    sizes[2],
                    circles[2]["people"],
                    circles[2]["ring"],
                    circles[2]["bg"],
                    circles[2]["color"],
                    circles[2]["max"],
                ),
            ),
            ft.Container(
                left=(440 - sizes[1]) / 2,
                top=(440 - sizes[1]) / 2,
                content=create_circle(
                    sizes[1],
                    circles[1]["people"],
                    circles[1]["ring"],
                    circles[1]["bg"],
                    circles[1]["color"],
                    circles[1]["max"],
                ),
            ),
            ft.Container(
                left=(440 - sizes[0]) / 2,
                top=(440 - sizes[0]) / 2,
                content=create_circle(
                    sizes[0],
                    circles[0]["people"],
                    circles[0]["ring"],
                    circles[0]["bg"],
                    circles[0]["color"],
                    circles[0]["max"],
                ),
            ),
        ],
    )

    return ft.Container(
        width=640,
        padding=20,
        animate_opacity=450,
        opacity=1 if is_active else 0,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            controls=[
                ft.Container(
                    margin=ft.margin.only(bottom=6),
                    content=ft.Text(
                        data["badge"],
                        size=11,
                        weight=ft.FontWeight.W_600,
                    ),
                ),
                ft.Text(
                    data["title"],
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(
                    margin=ft.margin.only(bottom=36),
                    content=ft.Text(
                        "Circulos de confianza basados en el modelo Dunbar",
                        size=13,
                        color="grey",
                        text_align=ft.TextAlign.CENTER,
                    ),
                ),
                ft.Container(
                    height=480,
                    alignment=ft.alignment.center,
                    content=stack,
                ),
                ft.Row(
                    wrap=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=24,
                    controls=[
                        ft.Column(
                            spacing=2,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    c["level"],
                                    size=14,
                                    weight=ft.FontWeight.W_600,
                                    color=c["color"],
                                ),
                                ft.Text(
                                    f'{len(c["people"])}/{c["max"]} · {c["desc"]}',
                                    size=8,
                                    color="rgba(255,255,255,0.5)",
                                ),
                            ],
                        )
                        for c in circles
                    ],
                ),
            ],
        ),
    )