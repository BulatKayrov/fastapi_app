from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str

    @property
    def db_url(self) -> str:
        return f'sqlite+aiosqlite:///{self.DB_NAME}.sqlite3'

    class Config:
        env_file = '.env'


settings = Settings()
