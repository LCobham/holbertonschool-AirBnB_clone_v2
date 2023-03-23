#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import place_amenities as pl_am_association
from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place", secondary=pl_am_association,
                                   back_populates="amenities")
