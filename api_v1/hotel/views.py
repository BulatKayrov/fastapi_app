from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_cache.decorator import cache

from api_v1.user.utils import get_current_user
from models import User
from .crud import HotelModel
from .schemas import HotelResponse, HotelCreate, HotelUpdate

router = APIRouter(prefix="/hotel", tags=["hotel"])


@router.get("/", response_model=list[HotelResponse])
@cache(expire=10)
async def get_hotels():
    res = await HotelModel.find_all()
    return res


@router.post("/", response_model=HotelResponse)
async def create_hotel(hotel: HotelCreate, current_user: User = Depends(get_current_user)):
    if current_user.is_admin:
        res = await HotelModel.create(**hotel.dict())
        return res
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")


@router.put('/{pk}')
async def update_hotel(pk: int, hotel: HotelUpdate, current_user: User = Depends(get_current_user)):
    if current_user.is_admin:
        res = await HotelModel.update(data=hotel, pk=pk, partial=True)
        return res
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
