#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self, id):
        """ Get all cities of the db which are in the state """
        from models import storage

        storageType = os.environ.get("HBNB_TYPE_STORAGE")
        if storageType == "db":
            return self.cities

        elif storageType == "file":
            res = []
            objs = storage.all()
            for id, obj in objs.items():
                if type(obj) is City and obj.state_id == id:
                    res.append(obj)
            return res
