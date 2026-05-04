import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Variáveis do Banco
    DB_DIALECT: str = "postgresql"
    DB_DRIVER: str = "psycopg2"
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int = 5432
    DB_NAME: str

    # Variáveis JWT

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    JWT_SECRET_KEY: str 

    @property
    def DATABASE_URL(self) -> str:
        """Montagem da URL"""
        return f"{self.DB_DIALECT}+{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = os.getenv("ENV_FILE",".env")


settings = Settings()