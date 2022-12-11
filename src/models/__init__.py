#!/usr/bin/python3
"""Initializes the models package"""

from engine.db_storage import Storage
storage = Storage()
storage.reload()
