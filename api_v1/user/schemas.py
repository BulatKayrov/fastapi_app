from pydantic import BaseModel, EmailStr


class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: str
    is_admin: bool | None = False


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
