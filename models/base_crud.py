from sqlalchemy import select, delete

from .db_helper import async_session


class Model:
    """Base class for all models, basic methods implemented CRUD"""
    model = None

    @classmethod
    async def find_all(cls, **kwargs):
        async with async_session() as session:
            stmt = select(cls.model).filter_by(**kwargs)
            result = await session.execute(stmt)
            return result.scalars().all()

    @classmethod
    async def find_by_id(cls, pk: int):
        async with async_session() as session:
            stmt = select(cls.model).where(cls.model.id == pk)
            result = await session.execute(stmt)
            return result.scalars().first()

    @classmethod
    async def create(cls, **kwargs):
        async with async_session() as session:
            stmt = cls.model(**kwargs)
            session.add(stmt)
            await session.commit()
            return stmt

    @classmethod
    async def update(cls, data, pk: int, partial: bool = False):
        async with async_session() as session:

            stmt = select(cls.model).where(cls.model.id == pk)
            result = await session.execute(stmt)
            obj = result.scalars().first()

            for key, value in data.model_dump(exclude_none=partial).items():
                setattr(obj, key, value)

            await session.commit()
            await session.refresh(obj)
            return obj
