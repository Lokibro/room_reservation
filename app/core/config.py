# app/core/config.py
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings


load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    app_title: str = "Бронирование переговорок"
    description: str = "Здесь можно всё!"
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()
