
from dishka import Provider, Scope, provide
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB: str = "auth_service"

    BOT_TOKEN: SecretStr

    USER_SERVICE_GRPC_HOST: str
    USER_SERVICE_GRPC_PORT: int

    B2_KEY_ID: str
    B2_APPLICATION_KEY: str
    B2_PHOTOS_BUCKET_NAME: str

    model_config = SettingsConfigDict(
        env_file=('stack.env', '.env'),
        extra="ignore"
    )


class SettingsProvider(Provider):
    @provide(scope=Scope.APP)
    def get_settings(self) -> Settings:
        return Settings()

