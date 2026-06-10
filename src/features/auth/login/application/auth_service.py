"""
AuthService — Use case: login, logout.
"""
from shared.kernel.result import Result
from features.auth.login.dto.login_dto import LoginRequest, LoginResponse
from adapters.api_client import ApiClient, ApiError


class AuthService:
    def __init__(self, api_client: ApiClient) -> None:
        self._api = api_client

    async def login(self, credentials: LoginRequest) -> Result[LoginResponse]:
        try:
            data = await self._api.post("/auth/login", {
                "email": credentials.email,
                "password": credentials.password,
            })
            return Result.ok(LoginResponse(
                token=data.get("token", "demo-token"),
                user_id=data.get("user_id", "demo"),
                role=data.get("role", "owner"),
                display_name=data.get("display_name", "Admin Demo"),
            ))
        except ApiError as e:
            return Result.fail(e.message)

    async def logout(self) -> Result[None]:
        try:
            await self._api.post("/auth/logout", {})
            return Result.ok(None)
        except ApiError:
            return Result.ok(None)
