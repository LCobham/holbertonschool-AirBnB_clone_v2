#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import place_amenity_association


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place",
                                   secondary=place_amenity_association)
