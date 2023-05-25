#!/usr/bin/python3
""" """
import models
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.conditions import Conditions
from models.spotify import SpotifyContent
from models.youtube import youtubeContent
from models.users import User
from models.strategies import Strategies

classes = {"Conditions": Conditions, "SpotifyContent": SpotifyContent,
           "youtubeContent": youtubeContent, "User": User,
           "Strategies": Strategies}


class DBStorage:
    """ """
    __engine = None
    __session = None


def __init__(self):
    """Instantiating DBStorage objects"""
    MINDPAL_MYSQL_USER = getenv('MINDPAL_MYSQL_USER')
    MINDPAL_MYSQL_PWD = getenv('MINDPAL_MYSQL_PWD')
    MINDPAL_MYSQL_HOST = getenv('MINDPAL_MYSQL_HOST')
    MINDPAL_MYSQL_DB = getenv('MINDPAL_MYSQL_DB')
    MINDPAL_ENV = getenv('MINDPAL_ENV')
    self.__engine = create_engine('mysql+mysql://{}:{}@{}/{}'.
                                  format(MINDPAL_MYSQL_USER,
                                         MINDPAL_MYSQL_PWD,
                                         MINDPAL_MYSQL_HOST,
                                         MINDPAL_MYSQL_DB))


def all(self):
    pass


def new(self, object):
    """ """
    self.__session.add(object)


def save(self):
    """"""
    self.__session.commit()


def delete(self, object=None):
    """"""
    if object is not None:
        self.__session.delete(object)


def reload(self):
    """"""
    pass


def close(self):
    """"""
    self.__session.remove()


def get(self, cls, id):
    """"""
    if cls not in classes.values():
        return None
    
    
def count(self):
    """ """
    pass
