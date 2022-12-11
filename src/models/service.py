#!/usr/bin/python3
"""
file: service.py
Desc: Service model
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 9 2022
"""
from models.base import BaseModel, Base
from sqlalchemy import (
    Column,
    String,
    ForeignKey
)


class Service(BaseModel, Base):
    """Represents a Service given by a hospital"""
    __tablename__ = "services"
    name = Column(String(128), nullable=False, unique=True)

    def __init__(self, *args, **kwargs):
        """Initializes Service object with super class constructor"""
        super().__init__(*args, **kwargs)
