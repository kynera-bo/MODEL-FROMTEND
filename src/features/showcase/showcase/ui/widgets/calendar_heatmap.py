"""
CalendarHeatmap — Mapa de calor tipo GitHub (grid de dias coloreados por actividad).
"""
import flet as ft
from theme import C, F_CAPTION, F_LABEL, F_MONO, RADIUS_SM, SPACE_XS, SPACE_SM, SPACE_MD, pad, _b, CENT
import random


HEAT_COLORS = [
    C.SURFACE2,            # 0: sin actividad
    C.ACCENT_FAINT,        # 1: baja
    "#3D8CC878",           # 2: media-baja
    "#6D8CC878",           # 3: media
    C.ACCENT,              # 4: alta
]

DAYS = ["Lun", "", "Mie", "", "Vie", "", ""]


def calendar_heatmap(
    weeks: int = 20,
    data: list[list[int]] = None,
    year: int = 2026,
) -> ft.Container:
    """Mapa de calor de actividad tipo GitHub.

    Args:
        weeks: Cantidad de semanas a mostrar
        data: Matriz 7xN con valores 0-4 por dia
        year: Ano a mostrar
    """
    if data is None:
        data = _generate_mock_data(weeks)

    content_items = []

    # Header con labels de meses (simplificado)
    month_labels = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
                    "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    # Distribuir meses aproximadamente cada 4.3 semanas
    month_row_items = []
    for i, month in enumerate(month_labels):
        pos = i * (weeks / 12) + 0.5
        month_row_items.append(
            ft.Container(
                content=ft.Text(month, size=F_LABEL, color=C.TEXT_DIM,
                                font_family="monospace"),
                width=14 * (weeks / 12),
            )
        )
    content_items.append(ft.Row(month_row_items, spacing=0))
    content_items.append(ft.Container(height=SPACE_XS))

    # Grid de calor
    heat_rows = []
    for row_idx in range(7):
        cells = []
        for col_idx in range(len(data[row_idx]) if row_idx < len(data) else 0):
            value = data[row_idx][col_idx] if row_idx < len(data) else 0
            color = HEAT_COLORS[min(value, 4)]
            day_label = DAYS[row_idx]
            if day_label:
                cells.append(
                    ft.Container(
                        content=ft.Text(
                            day_label, size=F_LABEL, color=C.TEXT_DIM,
                            font_family="monospace", text_align=ft.TextAlign.RIGHT,
                        ),
                        width=24,
                    )
                )
            else:
                cells.append(ft.Container(width=24))

            cells.append(
                ft.Container(
                    width=11, height=11,
                    bgcolor=color,
                    border_radius=RADIUS_SM,
                    border=_b(0.5, C.SURFACE),
                )
            )
        heat_rows.append(
            ft.Row(cells, spacing=1)
        )

    content_items.append(
        ft.Column(heat_rows, spacing=1)
    )

    # Leyenda
    content_items.append(ft.Container(height=SPACE_SM))
    legend_items = [
        ft.Text("Menos", size=F_MONO, color=C.TEXT_DIM),
    ]
    for color in HEAT_COLORS:
        legend_items.append(
            ft.Container(
                width=11, height=11,
                bgcolor=color,
                border_radius=RADIUS_SM,
            )
        )
    legend_items.append(
        ft.Text("Mas", size=F_MONO, color=C.TEXT_DIM),
    )
    content_items.append(
        ft.Row(legend_items, spacing=SPACE_XS)
    )

    return ft.Container(
        content=ft.Column(content_items, spacing=SPACE_XS, tight=True),
        bgcolor=C.SURFACE,
        border=_b(1, C.BORDER),
        border_radius=RADIUS_SM,
        padding=pad(v=SPACE_MD, h=SPACE_MD),
    )


def _generate_mock_data(weeks: int) -> list[list[int]]:
    """Genera datos de actividad simulados."""
    data = []
    for day in range(7):
        row = []
        for week in range(weeks):
            r = random.random()
            if r < 0.3:
                row.append(0)
            elif r < 0.55:
                row.append(1)
            elif r < 0.75:
                row.append(2)
            elif r < 0.9:
                row.append(3)
            else:
                row.append(4)
        data.append(row)
    return data
