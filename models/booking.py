from datetime import date
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Computed, ForeignKey

from .base import BaseModel

if TYPE_CHECKING:
    from .room import Room
    from .user import User


class Booking(BaseModel):
    __tablename__ = 'bookings'

    date_from: Mapped[date]
    date_to: Mapped[date]
    price: Mapped[int]
    total_days: Mapped[int] = mapped_column(Computed('date_to - date_from'))
    total_price: Mapped[int] = mapped_column(Computed('total_days * price'))

    room_id: Mapped[int] = mapped_column(ForeignKey('rooms.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    room: Mapped['Room'] = relationship(back_populates='bookings')
    user: Mapped['User'] = relationship(back_populates='bookings')

    def __repr__(self):
        return f"<Booking(id='{self.id}')>"
