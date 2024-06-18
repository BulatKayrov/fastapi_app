from pydantic import BaseModel


class HotelBase(BaseModel):
    name: str
    location: str
    service: str
    rooms_quantity: int
    image_id: int


class HotelCreate(HotelBase):
    pass


class HotelResponse(HotelBase):
    id: int
