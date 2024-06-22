from datetime import datetime, timedelta

from fastapi import HTTPException, status, Request, Depends
from jose import jwt, JWTError
from passlib.context import CryptContext

from api_v1.user.crud import UserModel
from config import settings


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str):
    return password_context.hash(password)


def verify_password(password: str, hashed_password: str):
    return password_context.verify(password, hashed_password)


async def authenticate_user(email: str, password: str):
    _user = await UserModel.find_by_email(email=email)
    if not _user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if _user and verify_password(password=password, hashed_password=_user.hashed_password):
        return _user
    return None


def create_access_token(data: dict, expires_minutes: int = 3):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(claims=to_encode, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def get_token(request: Request):
    return request.cookies.get(settings.JWT_COOKIE_NAME)


async def get_current_user(token: str | None = Depends(get_token)):
    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token not found")

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")

    expire = payload.get("exp")
    if (not expire) and (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")

    email: str = payload.get("sub")
    if email is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email not found")

    user: UserModel = await UserModel.find_by_email(email)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
