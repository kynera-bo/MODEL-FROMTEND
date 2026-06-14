"""
RoutingAdapter — OSRM API para ruteo por calles entre dos o más puntos (waypoints).
"""
import httpx
from pydantic import BaseModel


class RouteResponse(BaseModel):
    coordinates: list[tuple[float, float]]
    distance_km: float
    duration_min: float


async def get_route(points: list[tuple[float, float]]) -> RouteResponse:
    if len(points) < 2:
        msg = "Se necesitan al menos 2 puntos"
        raise ValueError(msg)
    coords_str = ";".join(f"{lng},{lat}" for lat, lng in points)
    url = (
        f"https://router.project-osrm.org/route/v1/driving/"
        f"{coords_str}?geometries=geojson&overview=full&steps=false"
    )
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        route = data["routes"][0]
        raw_coords = route["geometry"]["coordinates"]
        distance = route["distance"] / 1000
        duration = route["duration"] / 60
        return RouteResponse(
            coordinates=[(c[1], c[0]) for c in raw_coords],
            distance_km=round(distance, 2),
            duration_min=round(duration, 1),
        )
