from fastapi import HTTPException, status
from keycloak.exceptions import KeycloakAuthenticationError
from src.config import keycloak_openid
from src.models import UserInfo

class AuthService:
    @staticmethod
    def authenticate_user(username: str, password: str) -> str:
        try:
            token = keycloak_openid.token(username, password)
            return token["access_token"]
        except KeycloakAuthenticationError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Erro no username ou senha"
            )
        
    @staticmethod
    def verify_token(token: str) -> UserInfo:
        try:
            user_info = keycloak_openid.userinfo(token)
            print(user_info)
            if not user_info:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido."
                )
            return UserInfo(
                preferred_username=user_info.get('preferred_username'),
                email=user_info.get('email'),
                full_name=user_info.get('name')
            )
        except KeycloakAuthenticationError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Não pôde validar credenciais"
            )