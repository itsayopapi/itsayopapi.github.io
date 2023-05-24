#!/usr/bin/python3
"""
This is a user class and it inherits from Base_model.
"""
from models.base_model import Base_model, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class User(Base_model, Base):
    """
    This is the user Class
    Attributes
        email: user email address
        password: user password
        first_name: user first name
        last_name: user last name
        conditions: choices of conditions for the users
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    conditions_choice = relationship('conditions', backref='users')
