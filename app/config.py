from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str = "local"
    database_url: str = ""
    rabbitmq_url: str = ""
    redis_url: str = ""
    sendgrid_api_key: str = ""
    notify_from_email: str = ""
    frontend_url: str = ""
    
    class Config:
        env_file = ".env"

settings = Settings()
