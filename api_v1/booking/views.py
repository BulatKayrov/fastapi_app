from fastapi import APIRouter

from .crud import BookingModel
from .schemas import BookingBaseSchema, BookingCreateSchema

router = APIRouter(prefix='/booking', tags=['booking'])


@router.get('/all')
async def get_booking() -> list[BookingBaseSchema]:
    return await BookingModel.find_all()


@router.post('/')
async def create_booking(booking: BookingCreateSchema):
    return await BookingModel.create(**booking.model_dump())
