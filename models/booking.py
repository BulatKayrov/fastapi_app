from datetime import date
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property

from .base import BaseModel

if TYPE_CHECKING:
    from .room import Room
    from .user import User


class Booking(BaseModel):
    __tablename__ = 'bookings'

    date_to: Mapped[date]
    date_from: Mapped[date]
    price: Mapped[int]

    @hybrid_property
    def total_days(self):
        return (self.date_from - self.date_to).days

    @hybrid_property
    def total_price(self):
        return self.total_days * self.price

    room_id: Mapped[int] = mapped_column(ForeignKey('rooms.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    room: Mapped['Room'] = relationship(back_populates='bookings')
    user: Mapped['User'] = relationship(back_populates='bookings')

    def __repr__(self):
        return f"<Booking(id='{self.id}')>"
