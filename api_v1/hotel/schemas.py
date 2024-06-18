from pydantic import BaseModel, ConfigDict


class HotelBase(BaseModel):
    name: str
    location: str
    service: str
    rooms_quantity: int
    image_id: int

    # class Config:
    #     orm_mode = True


class HotelCreate(HotelBase):
    pass


class HotelResponse(HotelBase):
    id: int


class HotelUpdate(HotelBase):
    model_config = ConfigDict(from_attributes=True)
    name: str | None = None
    location: str | None = None
    service: str | None = None
    rooms_quantity: int | None = None
    image_id: int | None = None
