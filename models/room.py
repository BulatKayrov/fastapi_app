from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import BaseModel

if TYPE_CHECKING:
    from .hotel import Hotel
    from .booking import Booking


class Room(BaseModel):
    __tablename__ = 'rooms'

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    services: Mapped[str]
    quantity: Mapped[int]
    image_id: Mapped[int]

    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))
    hotel: Mapped['Hotel'] = relationship(back_populates='rooms')
    bookings: Mapped[list['Booking']] = relationship(back_populates='room')

    def __repr__(self):
        return f"<Room(name='{self.name}')>"
