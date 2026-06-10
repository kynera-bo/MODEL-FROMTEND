"""
ApiClient — Port (Protocol) + Adapter (HttpApiClient).
Features dependen del Protocol, nunca de httpx directamente.
"""
import httpx
from typing import Protocol


class ApiClient(Protocol):
    """Interface para cliente HTTP. Features dependen de este Protocol."""
    async def get(self, path: str, **kwargs) -> dict: ...
    async def post(self, path: str, json: dict) -> dict: ...
    async def put(self, path: str, json: dict) -> dict: ...
    async def delete(self, path: str) -> dict: ...


class ApiError(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class HttpApiClient:
    """Implementacion concreta con httpx."""

    def __init__(self, base_url: str):
        self._client = httpx.AsyncClient(base_url=base_url, timeout=30.0)

    async def get(self, path: str, **kwargs) -> dict:
        resp = await self._client.get(path, **kwargs)
        return self._handle_response(resp)

    async def post(self, path: str, json: dict) -> dict:
        resp = await self._client.post(path, json=json)
        return self._handle_response(resp)

    async def put(self, path: str, json: dict) -> dict:
        resp = await self._client.put(path, json=json)
        return self._handle_response(resp)

    async def delete(self, path: str) -> dict:
        resp = await self._client.delete(path)
        return self._handle_response(resp)

    def _handle_response(self, resp: httpx.Response) -> dict:
        if resp.status_code >= 400:
            detail = "Error"
            try:
                detail = resp.json().get("message", resp.json().get("detail", "Error"))
            except Exception:
                pass
            raise ApiError(detail, resp.status_code)
        return resp.json()

    async def close(self):
        await self._client.aclose()
