#!/usr/bin/python3
"""
This is a Strategy class and it inherits from Base_model.
"""
from models.base_model import Base_model, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class SpotifyContent(Base_model, Base):
    """
    Spotify Content class
    Attributes:
    content_tittle: the title of the content
    podcast_id: the id of the podcast
    strategy_id: the id of the strategy to
    use the content for.
    """
    __tablename__ = 'spotitifyContent'
    content_title = Column(String(60), nullable=False)
    podcast_id = Column(String(60), nullable=False)
    strategy_id = Column(String(60), ForeignKey('strategies.id'))
