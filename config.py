from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    """
    Base settings for the application
    """

    # Database
    DB_HOST_DEV: str    # for development to docker compose
    DB_HOST_LOCAL: str  # from docker image
    DB_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

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
        """
        Dynamically build the database url based on the environment variables
        :return: database url
        """
        return f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.DB_HOST_LOCAL}:{self.DB_PORT}/{self.POSTGRES_DB}'

    @property
    def redis_url(self) -> str:
        """
        Dynamically build the redis url based on the environment variables
        :return: redis url
        """
        return f'redis://{self.REDIS_HOST}:{self.REDIS_PORT}'

    @property
    def broker_url(self) -> str:
        """
        Dynamically build the broker url based on the environment variables
        :return: broker url
        """
        return f'{self.BROKER_NAME}://{self.REDIS_HOST}:{self.REDIS_PORT}/0'

    @property
    def backend_url(self) -> str:
        """
        Dynamically build the backend url based on the environment variables
        :return: backend url
        """
        return f'{self.BROKER_NAME}://{self.REDIS_HOST}:{self.REDIS_PORT}/0'

    class Config:
        env_file = '.env'


settings = Settings()
