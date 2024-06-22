from datetime import date

from pydantic import BaseModel


class BookingBaseSchema(BaseModel):
    date_from: date
    date_to: date
    price: int
    total_days: int
    total_price: int
    room_id: int
    user_id: int


class BookingCreateSchema(BaseModel):
    date_from: date
    date_to: date
    price: int
    room_id: int


class BookingResponseSchema(BookingBaseSchema):
    id: int
