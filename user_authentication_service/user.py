#!/usr/bin/env python3


from sqlalchemy import create_engine, ForeignKey, Column, String, Interger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column("id", Interger, primary_key=True)
    email = Column("email", String, nullable=False)
    hashed_password = Column("hashed_password", String, nullable=False)
    session_id = Column("session_id", String, nullable=True)
    reset_token = Column("reset_token", String, nullable=True)
