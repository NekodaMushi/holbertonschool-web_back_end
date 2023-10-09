#!/usr/bin/env python3

"""SQLAlchemy model named User for a database table named users"""

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """User class"""

    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    email = Column("email", String(250), nullable=False)
    hashed_password = Column("hashed_password", String(250), nullable=False)
    session_id = Column("session_id", String(250), nullable=True)
    reset_token = Column("reset_token", String(250), nullable=True)
