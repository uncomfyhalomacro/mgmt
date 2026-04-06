from pydantic import Field, BaseModel
from typing import Annotated
from pydantic_settings import BaseSettings, SettingsConfigDict

class AuthConfig(BaseModel):
    jwt_secret: Annotated[str, Field()] = ""
    cookie_secret: Annotated[str, Field()] = ""

class Settings(BaseSettings):
    auth: Annotated[AuthConfig, Field()] = AuthConfig()
    pg_url: Annotated[str, Field()] = "" 
    domains: Annotated[set[str], Field()] = set()
    api_root: Annotated[str, Field()] = "/api"
    port: Annotated[int, Field()] = 8080
    host: Annotated[str, Field()] = 'localhost'

    model_config = SettingsConfigDict()

settings = Settings()
