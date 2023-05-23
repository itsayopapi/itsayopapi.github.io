#!/usr/bin/python3
"""This is a Base Model for MindPal MVP"""
from sqlalchemy.ext.declarative import declarative_base
import models
from datetime import datetime
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

class BaseModel:
    """
    This is the models defines
    common attributes for all models
    """
id = Column(String(60), unique=True, nullable=True, primary_key=True)
date_created = Column(DateTime, nullable=True, default=(datetime.utcnow()))
date_updated = Column(DateTime, nullable=False, default=(datetime.utcnow()))

def __str__(self):
    """
    This returns a string representation 
    of the class name, id and a dictionary
    """
    info = type(self).__name__, self.id, self.__dict__
    return(info)

def __repr__(self):
    """Retuns the string representation """
    return self.__str__()

def save(self):
    """
    Method that updates the date_updated attribute with the current date.
    """
    self.date_created = datetime.utcnow()
    models.storage.new(self)
    models.storage.save()

def delete(self):
    """ This Method will delete data from the database"""
    models.storage.delete(self)