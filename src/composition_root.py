"""
Composition Root — ONLY place where objects are instantiated.
Frozen Container with manual dependency injection.
"""
from dataclasses import dataclass
from shared.config import Settings
from adapters.api_client import HttpApiClient
from adapters.auth_adapter import AuthSession
from features.auth.login.application.auth_service import AuthService


@dataclass(frozen=True)
class Container:
    settings: Settings
    auth_session: AuthSession
    api_client: HttpApiClient
    auth_service: AuthService


_container: Container | None = None


def init_container(settings: Settings = None) -> Container:
    global _container

    if settings is None:
        settings = Settings()

    # Adapters
    api_client = HttpApiClient(base_url=settings.API_BASE_URL)

    # Auth
    auth_session = AuthSession()
    auth_service = AuthService(api_client)

    _container = Container(
        settings=settings,
        auth_session=auth_session,
        api_client=api_client,
        auth_service=auth_service,
    )
    return _container


def get_container() -> Container:
    if _container is None:
        raise RuntimeError("Container not initialized. Call init_container() first.")
    return _container
