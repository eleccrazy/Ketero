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
    TEXT,
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

    # Required attributes to register a new hospital to the ketero App.
    name = Column(String(128), nullable=False)
    description = Column(TEXT, nullable=True)
    card_price = Column(Integer, nullable=False, default=0)
    number_of_doctors = Column(Integer, nullable=False, default=0)
    image_url = Column(String(20000), nullable=False)
    lattitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    number_of_departments = Column(Integer, nullable=False, default=0)
    number_of_awards = Column(Integer, nullable=True, default=0)
    number_of_research_labs = Column(Integer, nullable=True, default=0)
    email_address = Column(String(128), nullable=False)
    phone = Column(String(10), nullable=False)
    location = Column(String(20000), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)

    orders = relationship("Order", backref="hospital",
                          cascade="all, delete, delete-orphan")
    services = relationship("Service",
                            secondary=hospital_service,
                            viewonly=False)

    def __init__(self, *args, **kwargs):
        """Initializes Hospital object with super class constructor"""
        super().__init__(*args, **kwargs)
