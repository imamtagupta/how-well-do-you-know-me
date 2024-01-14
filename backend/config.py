from pydantic_settings import BaseSettings

class DevelopementConfig(BaseSettings):
    DB_URL:str
    DB_NAME:str
    DB_USER:str
    DB_PASSWORD:str

settings = DevelopementConfig()