#!/usr/bin/python3
"""
This is a conditions class and it inherits from Base_model.
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class Conditions(BaseModel, Base):
    """
    This class for conditions
    Attributes:
    condition_name : name
    Strategy_choice : strategy_id
    user_id : user_id
    """
    __tablename__ = "conditions"
    condition_name = Column(String(128), nullable=False)
    strategy_id = Column(String(60), ForeignKey('strategies.id'))
    users = relationship("User", backref="conditions")
