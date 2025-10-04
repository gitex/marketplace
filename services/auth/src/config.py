from antidote import injectable
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.auth_types import Algorithm


class Jwt(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="JWT_")

    alg: Algorithm = "HS256"
    secret_key: SecretStr = SecretStr(
        "Az8H28hPZ25uTCg67BOQRj1KnCiXfJV2pYoQ8bsLVuxVl3JVh16"
    )
    aud: str = "auth"
    iss: str = "auth"
    access_ttl_seconds: int = 60 * 15  # 15 minutes
    refresh_ttl_seconds: int = 60 * 60 * 24  # 1 day


@injectable
class Settings(BaseSettings):
    model_config = SettingsConfigDict()

    debug: bool = False
    app_name: str = "auth"

    jwt: Jwt = Jwt()


settings = Settings()
