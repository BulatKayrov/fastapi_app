from sqlalchemy import delete, select

from models import Model, Booking
from models.db_helper import async_session


class BookingModel(Model):
    model = Booking

    @classmethod
    async def delete_booking(cls, pk: int, user_id: int):
        async with async_session() as session:
            stmt = delete(cls.model).filter_by(id=pk, user_id=user_id)
            await session.execute(stmt)
            await session.commit()
            return None
