#!/usr/bin/python3
"""
This is a conditions class and it inherits from Base_model.
"""
from flask import Flask
from base_model import BaseModel
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Conditions(BaseModel):
    """
    This class for conditions
    Attributes:
    condition_name : name
    Strategy_choice : strategy_id
    user_id : user_id
    """
    __tablename__ = "conditions"
    condition_name = db.Column(db.String(128), nullable=False)
    strategy_id = db.Column(db.String(60), db.ForeignKey('strategies.id'))
    users = db.relationship("User", backref="conditions")
