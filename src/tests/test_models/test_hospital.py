#!/usr/bin/python3

"""
File: test_hospital.py
Desc: This module contains all possible testcases for the hospital.py
      module in the models package. It uses the standard unittest.
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 11 2022
"""

from models.hospital import Hospital, BaseModel, Base
from unittest import TestCase
import pep8


class TestObjectCreation(TestCase):
    """A class to test object creation and their properties"""

    def test_for_inheritance(self):
        hospital = Hospital(
            name="Paulos",
            description="Just for fun",
            card_price=300,
            number_of_doctors=32,
            image_url="http://testme/paulos.png",
            lattitude=876.76,
            longitude=77.77
        )
        self.assertTrue(isinstance(hospital, BaseModel))
        self.assertTrue(isinstance(hospital, Hospital))
        self.assertTrue(isinstance(hospital, Base))

    def test_object_creation(self):
        hospital = Hospital(
            name="Paulos",
            description="Just for fun",
            card_price=300,
            number_of_doctors=32,
            image_url="http://testme/paulos.png",
            lattitude=876.76,
            longitude=77.77
        )
        keys = hospital.__dict__.keys()
        properties = ['name', 'number_of_doctors', 'card_price',
                      'description', 'lattitude', 'longitude',
                      'image_url', 'id', 'created_at', 'updated_at']
        for property in properties:
            self.assertIn(property, keys)


class TestDocstring(TestCase):
    """Tests docstrings"""

    def test_module_docstring(self):
        from models import hospital
        module = hospital.__doc__
        self.assertIsNot(module, None,
                         "hospital.py needs a docstring")
        self.assertTrue(len(module) > 1,
                        "hospital.py needs a docstring")

    def test_class_docstring(self):
        self.assertIsNot(Hospital.__doc__, None,
                         "Hospital class needs a docstring")
        self.assertTrue(len(Hospital.__doc__) >= 1,
                        "Hospital class needs a docstring")


class TestPep8(TestCase):
    """Tests the hospital.py and test_hospital.py module for pycodestyle"""

    def test_pep8_conformance(self):
        for path in ['models/hospital.py',
                     'tests/test_models/test_hospital.py']:
            with self.subTest(path=path):
                errors = pep8.Checker(path).check_all()
                self.assertEqual(errors, 0)
