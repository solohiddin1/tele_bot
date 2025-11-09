from pydantic_settings import BaseSettings
# from typing import 
from pathlib import Path
from dotenv import load_dotenv

# from database.db import PASSWORD

load_dotenv(dotenv_path=Path(__file__).parent/ ".env")

class Settings(BaseSettings):
    TOKEN: str
    OWNER: str
    YOU_TUBE_API: str
    YOU_TUBE_SEARCH: str
    # database_url: str = DATABASE_URL
    DATABASE_URL: str
    # DBNAME: str

    # PORT: str
    # PASSWORD: str
    # USER

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()