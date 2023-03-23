#!/usr/bin/python3
"""
    This module created the DBStorage class
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base


class DBStorage:
    """ DBStorage class """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("{}+{}://{}:{}@{}/{}".
                                      format("mysql", "mysqldb",
                                             os.environ.get("HBNB_MYSQL_USER"),
                                             os.environ.get("HBNB_MYSQL_PWD"),
                                             os.environ.get("HBNB_MYSQL_HOST"),
                                             os.environ.get("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if os.environ.get("HBNB_ENV") == "test":
            # drop all tables
            pass

    def all(self, cls=None):
        """
            Return all objs in the database if type(obj) == cls.
            If cls is set to None, return all objects in the db
        """
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {'User': User, 'Place': Place,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Review': Review}

        dictionary = {}

        if cls is None:
            class_list = (User, State, City, Amenity, Place, Review)
            for _cls in class_list:
                qry = self.__session.query(_cls)
        else:
            qry = self.__session.query(classes.get(cls))

        for obj in qry:
            dictionary[f"{type(obj).__name__}.{obj.id}"] = obj
        return dictionary

    def new(self, obj):
        """ Adds an object to the database """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes to the database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete an object from the database """
        if obj is not None:
            self.__session.query(type(obj)).get(obj.id).delete()

    def reload(self):
        """ Recreate all objects from the database """
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
