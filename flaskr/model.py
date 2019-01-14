import os
from sqlalchemy import Column, Integer, Text, String, ForeignKey, DateTime
from datetime import datetime
from flaskr.db import Base


class Recipe(Base):

    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    type = Column(Integer, nullable=False)
    title = Column(String)
    filename = Column(Text)
    url = Column(String)
    description = Column(String)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.now, onupdate=datetime.now)


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.now, onupdate=datetime.now)
