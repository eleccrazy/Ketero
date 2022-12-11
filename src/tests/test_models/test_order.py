#!/usr/bin/python3

"""
File: test_order.py
Desc: This module contains all possible testcases for the order.py
      module in the models package. It uses the standard unittest.
Authors: Gizachew Baynss, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 11 2022
"""

from models.order import Order, BaseModel, Base
from unittest import TestCase
import pep8


class TestObjectCreation(TestCase):
    """A class to test object creation"""

    def test_for_inheritance(self):
        order = Order()
        self.assertTrue(isinstance(order, BaseModel))
        self.assertTrue(isinstance(order, Order))
        self.assertTrue(isinstance(order, Base))


class TestDocstring(TestCase):
    """Tests docstrings"""

    def test_module_docstring(self):
        from models import order
        module = order.__doc__
        self.assertIsNot(module, None,
                         "order.py needs a docstring")
        self.assertTrue(len(module) > 1,
                        "order.py needs a docstring")

    def test_class_docstring(self):
        self.assertIsNot(Order.__doc__, None,
                         "Order class needs a docstring")
        self.assertTrue(len(Order.__doc__) >= 1,
                        "Order class needs a docstring")


class TestPep8(TestCase):
    """Tests the order.py and test_order.py module for pycodestyle"""

    def test_pep8_conformance(self):
        for path in ['models/order.py',
                     'tests/test_models/test_order.py']:
            with self.subTest(path=path):
                errors = pep8.Checker(path).check_all()
                self.assertEqual(errors, 0)
