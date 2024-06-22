from fastapi import APIRouter, Request, Depends

from .crud import BookingModel
from .schemas import BookingBaseSchema, BookingCreateSchema

from api_v1.user.utils import get_current_user

router = APIRouter(prefix='/booking', tags=['booking'])


@router.get('/all')
async def get_booking(user=Depends(get_current_user)) -> list[BookingBaseSchema]:
    res = await BookingModel.find_all(user_id=user.id)
    return res


@router.post('/')
async def create_booking(booking: BookingCreateSchema, user=Depends(get_current_user)):
    data = booking.model_dump()
    data['user_id'] = user.id
    return await BookingModel.create(**data)
