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


class Strategies(BaseModel):
    """
    This is a Strategy class
    Attributes:
        stategy_name: the name of the strategy
        strategy_text: the text to a strategy
        youtube_id : The id of a youtube content
        spotify_id : The id of the spotify content
    """
    __tablename__ = 'strategies'
    strategy_name = db.Column(db.String(255), nullable=False)
    strategy_text = db.Column(db.Text, nullable=False)
    conditions = db.relationship("Conditions", backref="strategies")
    youtube_id = db.Column(db.String(60), db.ForeignKey("youtube.id"))
    spotify_id = db.Column(db.String(60), db.ForeignKey("spotify.id"))
