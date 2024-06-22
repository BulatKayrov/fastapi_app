from fastapi import APIRouter

from .booking.views import router as booking_router
from .hotel.views import router as hotel_router
from .user.views import router as user_router

api_router = APIRouter(prefix='/api/v1')
api_router.include_router(user_router)
api_router.include_router(booking_router)
api_router.include_router(hotel_router)
