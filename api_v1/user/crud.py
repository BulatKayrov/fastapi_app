from sqlalchemy import select

from models import Model, User
from models.db_helper import async_session


class UserModel(Model):
    model = User

    @classmethod
    async def find_by_email(cls, email: str):
        async with async_session() as session:
            stmt = select(cls.model).where(cls.model.email == email)
            result = await session.execute(stmt)
            return result.scalars().first()

    @classmethod
    async def create(cls, email: str, password: str, is_admin: bool = False):
        async with async_session() as session:
            user = cls.model(email=email, hashed_password=password, is_admin=is_admin)
            session.add(user)
            await session.commit()
            return user
