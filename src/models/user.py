#!/usr/bin/python3
"""
file: user.py
Desc: User model
Authors: Gizachew Baynss, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 9 2022
"""
from models.base import BaseModel, Base
from sqlalchemy import (
    Column,
    String,
    ForeignKey
)
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """Represents a User"""
    __tablename__ = "users"
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    phone = Column(String(10), nullable=False, unique=True)
    orders = relationship("Order", backref="user")

    def __init__(self, *args, **kwargs):
        """Initializes User object with super class constructor"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)