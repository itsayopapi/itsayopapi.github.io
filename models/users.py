#!/usr/bin/python3
"""
This is a user class and it inherits from Base_model.
"""
from flask import Flask
from base_model import BaseModel
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(BaseModel):
    """
    This is the user Class
    Attributes
        email: user email address
        password: user password
        first_name: user first name
        last_name: user last name
        conditions: choices of conditions for the users
    """

    __tablename__ = 'users'
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    conditions_id = db.Column(db.String(60), db.ForeignKey(
        'conditions.id'), nullable=False)
