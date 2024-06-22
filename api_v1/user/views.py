from fastapi import APIRouter, Depends, HTTPException, status, Response, Request

from .schemas import UserRegisterOrLoginSchema
from .crud import UserModel
from .utils import get_password_hash, authenticate_user, create_access_token
from config import settings

router = APIRouter(prefix="/auth", tags=["Authentication & Authorization"])


@router.post("/register")
async def register_user(user: UserRegisterOrLoginSchema):
    existing_user = await UserModel.find_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    password_hash = get_password_hash(user.password)
    await UserModel.create(email=user.email, password=password_hash)
    return {'status': status.HTTP_201_CREATED}


@router.post("/login")
async def login_user(response: Response, user: UserRegisterOrLoginSchema):
    _user = await authenticate_user(email=user.email, password=user.password)
    if not _user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    token = create_access_token(data={'sub': user.email}, expires_minutes=5)
    response.set_cookie(key=settings.JWT_COOKIE_NAME, value=token, httponly=True)
    return {'status': status.HTTP_200_OK, 'token': token}

