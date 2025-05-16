from fastapi import FastAPI, Depends, Form
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.models import TokenResponse, UserInfo
from src.controller import AuthController

app = FastAPI()

bearer_scheme = HTTPBearer()

@app.get("/")
async def read_root():
    print('dentro')
    return AuthController.read_root()

@app.post("/login", response_model=TokenResponse)
async def login(username: str = Form(...), password: str = Form(...)):
    print('tenta login')
    return AuthController.login(username, password)

@app.get("/protected", response_model=UserInfo)
async def protected_endpoint(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    return AuthController.protected_endpoint(credentials)