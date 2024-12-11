'''routers/auth.py
Router for authentication path operaions
'''

from fastapi import APIRouter, HTTPException
from ..schemas.auth import LoginCreds, RegisCred
from ..schemas.user import UserResponse
from ..services.auth_service import AuthService


router = APIRouter(prefix='/auth')


@router.post('/register/')
def register_user(cred: RegisCred) -> UserResponse:
    
    try:
        user = AuthService.register_user(cred.dict())
    except:
        raise HTTPException(status_code=400, detail="Bad Request")

    return user.to_dict()


@router.post('/login/')
def login_user(cred: LoginCreds) -> UserResponse:
    user = AuthService.login_user(cred.dict())

    if user:
        return user
    raise HTTPException(status_code=401, detail="invalid credentials")
