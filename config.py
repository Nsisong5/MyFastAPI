from pydantic_settings import BaseSettings

class Settings(BaseSettings):
     database_user_password: str
     database_username :str
     database_host_name :str
     database: str
 
     database_name : str
     
     class Config:
          env_file= ".env"

settings  = Settings()                 