from fastapi import Depends, HTTPException, status, Form
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.models import TokenResponse, UserInfo
from src.service import AuthService

bearer_scheme = HTTPBearer()

class AuthController:
    @staticmethod
    def read_root():
        return AuthService.get_read_root()

    @staticmethod
    def login(username: str = Form(...), password: str = Form(...)) -> TokenResponse:
        access_token = AuthService.authenticate_user(username, password)
        if not access_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Senha ou username inválido."
            )
        
        return TokenResponse(access_token=access_token)
    

    @staticmethod
    def protected_endpoint(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme))-> UserInfo:
        token = credentials.credentials
        user_info = AuthService.verify_token(token)

        if not user_info:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido.",
                headers={"WW-Authenticate": "Bearer"}
            )
        
        print(f'chegou aqui - {user_info}')
        return user_info