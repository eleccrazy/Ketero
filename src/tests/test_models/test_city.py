#!/usr/bin/python3

"""
File: test_city.py
Desc: This module contains all possible testcases for the city.py
      module in the models package. It uses the standard unittest.
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 11 2022
"""

from models.city import City, BaseModel, Base
from unittest import TestCase
import pep8


class TestObjectCreation(TestCase):
    """A class to test object creation and their properties"""

    def test_for_inheritance(self):
        city = City(name="Hawasa")
        self.assertTrue(isinstance(city, BaseModel))
        self.assertTrue(isinstance(city, City))
        self.assertTrue(isinstance(city, Base))

    def test_object_creation(self):
        city = City(name='Adama')
        keys = city.__dict__.keys()
        self.assertIn('name', keys)
        self.assertEqual(city.__dict__['name'], 'Adama')


class TestDocstring(TestCase):
    """Tests docstrings"""

    def test_module_docstring(self):
        from models import city
        module = city.__doc__
        self.assertIsNot(module, None,
                         "city.py needs a docstring")
        self.assertTrue(len(module) > 1,
                        "city.py needs a docstring")

    def test_class_docstring(self):
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")


class TestPep8(TestCase):
    """Tests the city.py and test_city.py module for pycodestyle"""

    def test_pep8_conformance(self):
        for path in ['models/city.py',
                     'tests/test_models/test_city.py']:
            with self.subTest(path=path):
                errors = pep8.Checker(path).check_all()
                self.assertEqual(errors, 0)
