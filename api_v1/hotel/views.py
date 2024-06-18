from fastapi import APIRouter, Depends, HTTPException
from .schemas import HotelResponse, HotelCreate, HotelUpdate
from .crud import HotelModel

router = APIRouter(prefix="/hotel", tags=["hotel"])


@router.get("/", response_model=list[HotelResponse])
async def get_hotels():
    res = await HotelModel.find_all()
    return res


@router.post("/", response_model=HotelResponse)
async def create_hotel(hotel: HotelCreate):
    res = await HotelModel.create(**hotel.dict())
    return res


@router.put('/{pk}')
async def update_hotel(pk: int, hotel: HotelUpdate):
    res = await HotelModel.update(data=hotel, pk=pk, partial=True)
    return res
