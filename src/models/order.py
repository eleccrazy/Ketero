#!/usr/bin/python3
"""
file: order.py
Desc: Order model
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 9 2022
"""
from models.base import BaseModel, Base
from sqlalchemy import (
    Column,
    String,
    ForeignKey
)


class Order(BaseModel, Base):
    """Represents Orders"""
    __tablename__ = "orders"
    hospital_id = Column(String(60), ForeignKey('hospitals.id'),
                         nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes Order object with super class constructor"""
        super().__init__(*args, **kwargs)
