from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship, relationships

from .base import BaseModel

if TYPE_CHECKING:
    from .room import Room


class Hotel(BaseModel):
    __tablename__ = 'hotels'

    name: Mapped[str]
    location: Mapped[str]
    service: Mapped[str]
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]

    rooms: Mapped[list['Room']] = relationship(back_populates='hotel')

    def __repr__(self):
        return f"<Hotel(name='{self.name}')>"
