from pydantic_settings import BaseSettings

class DevelopmentConfig(BaseSettings):
    
    DB_URL:str=""
    DB_NAME:str=""
    DB_USER:str=""
    DB_PASSWORD:str=""

    class Config:
        env_file = ".env"

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_URL}/{self.DB_NAME}"
        
settings = DevelopmentConfig()