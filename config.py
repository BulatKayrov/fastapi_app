from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str

    # jwt
    SECRET_KEY: str
    ALGORITHM: str
    JWT_COOKIE_NAME: str

    # redis
    REDIS_HOST: str
    REDIS_PORT: int

    # celery
    BROKER_NAME: str = 'redis'

    # smtp
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: str
    SMTP_TLS: bool = False
    SMTP_SSL: bool = False

    @property
    def db_url(self) -> str:
        return f'sqlite+aiosqlite:///{self.DB_NAME}.sqlite3'

    @property
    def redis_url(self) -> str:
        return f'redis://{self.REDIS_HOST}:{self.REDIS_PORT}'

    @property
    def broker_url(self) -> str:
        return f'{self.BROKER_NAME}://{self.REDIS_HOST}:{self.REDIS_PORT}/0'

    @property
    def backend_url(self) -> str:
        return f'{self.BROKER_NAME}://{self.REDIS_HOST}:{self.REDIS_PORT}/0'

    class Config:
        env_file = '.env'


settings = Settings()
