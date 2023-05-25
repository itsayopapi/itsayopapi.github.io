#!/usr/bin/python3
"""
This is a Youtube class and it inherits from Base_model.
"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer


class YoutubeContent(BaseModel, Base):
    """
    The youtube content class
    Atribute
    content_title = Tittle of the youtube content
    strategy = the strategy to use this content for.
    """
    __tablename__ = 'youtubeContent'
    content_title = Column(String(60), nullable=False)
    video_url = Column(String(60), nullable=False)
    strategies = relationship("Strategies", backref="youtubeContent")
