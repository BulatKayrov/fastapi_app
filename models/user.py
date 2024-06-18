from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship
from .base import BaseModel

if TYPE_CHECKING:
    from .booking import Booking


class User(BaseModel):
    __tablename__ = 'users'

    email: Mapped[str]
    hashed_password: Mapped[str]

    bookings: Mapped[list['Booking']] = relationship(back_populates='user')

    def __repr__(self):
        return f"<User(email='{self.email}')>"
