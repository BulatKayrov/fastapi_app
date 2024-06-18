from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import HotelCreate
from models import Hotel


async def get_hotels(session: AsyncSession):
    stmt = select(Hotel)
    result = await session.execute(stmt)
    return result.scalars().all()


async def create_hotel(session: AsyncSession, hotel: HotelCreate):
    hotel = Hotel(**hotel.model_dump())
    session.add(hotel)
    await session.commit()
    return hotel
