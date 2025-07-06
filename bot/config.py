from pydantic_settings import BaseSettings
from pydantic import SecretStr
from dotenv import load_dotenv

load_dotenv()

class Config(BaseSettings):
    bot_token: SecretStr
    db_path: str = "../data/notebook.db"
    class Config:
        env_file = ".env"

def load_config():
    return Config()