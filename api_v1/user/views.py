from fastapi import APIRouter, HTTPException, status, Response

from config import settings
from tasks.user_tasks import send_message
from .crud import UserModel
from .schemas import UserRegisterSchema, UserLoginSchema
from .utils import get_password_hash, authenticate_user, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication & Authorization"])


@router.post("/register")
async def register_user(user: UserRegisterSchema):
    existing_user = await UserModel.find_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    password_hash = get_password_hash(user.password)
    user = await UserModel.create(email=user.email, password=password_hash, is_admin=user.is_admin)
    send_message.delay(str(user.email))
    return {'status': status.HTTP_201_CREATED}


@router.post("/login")
async def login_user(response: Response, user: UserLoginSchema):
    _user = await authenticate_user(email=user.email, password=user.password)
    if not _user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    token = create_access_token(data={'sub': user.email}, expires_minutes=5)
    response.set_cookie(key=settings.JWT_COOKIE_NAME, value=token, httponly=True)
    return {'status': status.HTTP_200_OK, 'token': token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie(key=settings.JWT_COOKIE_NAME)
    return {'status': status.HTTP_200_OK}

