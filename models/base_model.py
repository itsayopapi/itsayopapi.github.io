#!/usr/bin/python3
"""This is a Base Model for MindPal MVP"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class BaseModel(db.Model):
    """
    This is the models defines
    common attributes for all models
    """
    __tablename__ = 'base_model'
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, nullable=True,
                           default=(datetime.utcnow()))
    updated_on = db.Column(db.DateTime, nullable=False,
                           default=(datetime.utcnow()))


def __str__(self):
    """
    This returns a string representation 
    of the class name, id and a dictionary
    """
    info = type(self).__name__, self.id, self.__dict__
    return (info)


def __repr__(self):
    """Retuns the string representation """
    return self.__str__()


def save(self):
    """
    Method that updates the date_updated attribute with the current date.
    """
    self.date_created = datetime.utcnow()
    db.models.storage.new(self)
    db.models.storage.save()


def delete(self):
    """ This Method will delete data from the database"""
    db.models.storage.delete(self)
