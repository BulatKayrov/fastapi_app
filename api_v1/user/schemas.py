from pydantic import BaseModel, EmailStr


class UserRegisterOrLoginSchema(BaseModel):
    email: EmailStr
    password: str
