#!/usr/bin/python3
"""
file: hospital.py
Desc: Hospital model
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 9 2022
"""
from models.base import BaseModel, Base
from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    Integer,
    Float,
    Table
)
from sqlalchemy.orm import relationship


hospital_service = Table(
    'hospital_service',
    Base.metadata,
    Column('hospital_id', String(60),
           ForeignKey('hospitals.id', onupdate="CASCADE", ondelete="CASCADE"),
           primary_key=True),
    Column('service_id', String(60),
           ForeignKey('services.id', onupdate="CASCADE", ondelete="CASCADE"),
           primary_key=True,)
)


class Hospital(BaseModel, Base):
    """Representation for Hospitals"""

    __tablename__ = "hospitals"
    name = Column(String(128), nullable=False)
    description = Column(String(25000), nullable=True)
    card_price = Column(Integer, nullable=False, default=0)
    number_of_doctors = Column(Integer, nullable=False, default=0)
    image_url = Column(String(1024), nullable=False)
    lattitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)

    orders = relationship("Order", backref="hospital",
                          cascade="all, delete, delete-orphan")
    services = relationship("Service",
                            secondary=hospital_service,
                            viewonly=False)

    def __init__(self, *args, **kwargs):
        """Initializes Hospital object with super class constructor"""
        super().__init__(*args, **kwargs)
