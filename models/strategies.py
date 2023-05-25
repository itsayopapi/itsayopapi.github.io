#!/usr/bin/python3
"""
This is a Strategy class and it inherits from Base_model.
"""
from models.base_model import BaseModel, Base
from models import youtube, spotify
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Text, Integer


class Strategies(BaseModel, Base):
    """
    This is a Strategy class
    Attributes:
        stategy_name: the name of the strategy
        strategy_text: the text to a strategy
        youtube_id : The id of a youtube content
        spotify_id : The id of the spotify content
    """
    __tablename__ = 'strategies'
    strategy_name = Column(String(255), nullable=False)
    strategy_text = Column(Text, nullable=False)
    conditions = relationship("Conditions", backref="strategies")
    youtube_id = Column(String(60), ForeignKey("youtube.id"))
    spotify_id = Column(String(60), ForeignKey("spotify.id"))
