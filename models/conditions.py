#!/usr/bin/python3
"""
This is a conditions class and it inherits from Base_model.
"""
from models.base_model import Base_model, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class Conditions(Base_model, Base):
    """
    This class for conditions
    Attributes:
    condition_name : name
    Strategy_choice : strategy_id
    user_id : user_id
    """
    __tablename__ = "conditions"
    condition_name = Column(String(1024), nullable=False)
    strategy_choice = relationship(
        'strategies', backref='conditions', nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
