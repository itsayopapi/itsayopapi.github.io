#!/usr/bin/python3
"""
This is a user class and it inherits from Base_model.
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class User(BaseModel, Base):
    """
    This is the user Class
    Attributes
        email: user email address
        password: user password
        first_name: user first name
        last_name: user last name
        conditions: choices of conditions for the users
    """
    if models.storate_c == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False, unique=True)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        conditions_id = Column(String(60), ForeignKey(
            'conditions.id'), nullable=False)

    else:
        first_name = ""
        last_name = ""
        password = ""
        email = ""
