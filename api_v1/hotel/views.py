from fastapi import APIRouter, Depends, HTTPException

from models import get_session
from . import crud
from .schemas import HotelResponse, HotelCreate

router = APIRouter(prefix="/hotel", tags=["hotel"])


@router.get("/", response_model=list[HotelResponse])
async def get_hotels(session=Depends(get_session)):
    result = await crud.get_hotels(session=session)
    return result


@router.post("/", response_model=HotelResponse)
async def create_hotel(hotel: HotelCreate, session=Depends(get_session)):
    result = await crud.create_hotel(session=session, hotel=hotel)
    return result
