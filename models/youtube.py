#!/usr/bin/python3
"""
This is a Youtube class and it inherits from Base_model.
"""
from flask import Flask
from base_model import BaseModel
from flask_sqlalchemy import SQLAlchemy
from KamvaMindPal.app import app
from datetime import datetime

db = SQLAlchemy(app)


class YoutubeContent(BaseModel):
    """
    The youtube content class
    Atribute
    content_title = Tittle of the youtube content
    strategy = the strategy to use this content for.
    """
    __tablename__ = 'youtubeContent'
    content_title = db.Column(db.String(60), nullable=False)
    video_url = db.Column(db.String(60), nullable=False)
    strategies = db.relationship("Strategies", backref="youtubeContent")
