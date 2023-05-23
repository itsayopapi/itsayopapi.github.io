#!/usr/bin/python3
"""
This is a Strategy class and it inherits from Base_model.
"""
from models.base_model import Base_model, Base
from models import youtube, spotify
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Text, Integer


class Strategies(Base_model, Base):
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
    condition_id = Column(Integer(60), ForeignKey('strategy.id'))
    youtube_content = relationship('YoutubeContent', backref='strategies')
    spotify_content = relationship('SpotifyContent', backref='strategies')
