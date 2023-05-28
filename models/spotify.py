#!/usr/bin/python3
"""
This is a Strategy class and it inherits from Base_model.
"""
from flask import Flask
import models
from base_model import BaseModel
from flask_sqlalchemy import SQLAlchemy
from app import app
from datetime import datetime

db = SQLAlchemy(app)


class SpotifyContent(BaseModel):
    """
    Spotify Content class
    Attributes:
    content_tittle: the title of the content
    podcast_id: the id of the podcast
    strategy_id: the id of the strategy to
    use the content for.
    """
    __tablename__ = 'spotitifyContent'
    content_title = db.Column(db.String(60), nullable=False)
    podcast_id = db.Column(db.String(60), nullable=False)
    strategies = db.relationship("Strategies", backref="spotitifyContent")
