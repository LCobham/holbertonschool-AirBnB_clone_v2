#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import os

place_amenities = Table('place_amenity', Base.metadata,
                        Column('place_id', String(60),
                               ForeignKey("places.id"),
                               nullable=False),
                        Column('amenity_id', String(60),
                               ForeignKey("amenities.id"),
                               nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary=place_amenities,
                             viewonly=False,
                             back_populates="place_amenities")

    @property
    def reviews(self):
        """ Getter method for reviews """
        storageType = os.environ.get("HBNB_TYPE_STORAGE")

        if storageType == "db":
            return self.reviews

        elif storageType == "file":
            res = []
            objs = storage.all()
            for id, obj in objs.items():
                if type(obj) is Review and obj.place_id == self.id:
                    res.append(obj)
            return res

    """ @property
    def amenities(self):
        storageType = os.environ.get("HBNB_TYPE_STORAGE")

        if storageType == "db":
            return self.amenities

        elif storageType == "file":
            res = []
            objs = storage.all()
            for id, obj in objs.items():
                if type(obj) is Amenity and obj.place_id == self.id:
                    res.append(obj)
            return res """
