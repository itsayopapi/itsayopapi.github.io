#!/usr/bin/python3
""" """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.conditions import Conditions
from models.spotify import SpotifyContent
from models.youtube import youtubeContent
from models.users import User
from models.strategies import Strategies
