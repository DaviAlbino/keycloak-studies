from pydantic_settings import BaseSettings
from pydantic import Field
from keycloak import KeycloakOpenID

class Settings(BaseSettings):
    def auth(self):
        return