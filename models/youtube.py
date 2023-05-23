#!/usr/bin/python3
"""
This is a Youtube class and it inherits from Base_model.
"""
from models.base_model import Base_model, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer


class youtubeContent(Base_model, Base):
    """
    The youtube content class
    Atribute
    content_title = Tittle of the youtube content
    strategy = the strategy to use this content for.
    """
    __tablename__ = 'spotitifyContent'
    content_title = Column(String(60), nullable=False)
    video_id = Column(String(60), nullable=False)
    strategy_id = Column(Integer(60), ForeignKey('strategies.id'))
