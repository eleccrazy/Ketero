#!/usr/bin/python3

"""
File: test_service.py
Desc: This module contains all possible testcases for the service.py
      module in the models package. It uses the standard unittest.
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 11 2022
"""

from models.service import Service, BaseModel, Base
from unittest import TestCase
import pep8


class TestObjectCreation(TestCase):
    """A class to test object creation and their properties"""

    def test_for_inheritance(self):
        service = Service()
        self.assertTrue(isinstance(service, BaseModel))
        self.assertTrue(isinstance(service, Service))
        self.assertTrue(isinstance(service, Base))

    def test_object_creation(self):
        service = Service(name='Brain Surgery')
        keys = service.__dict__.keys()
        self.assertIn('name', keys)
        self.assertEqual(service.__dict__['name'], 'Brain Surgery')


class TestDocstring(TestCase):
    """Tests docstrings"""

    def test_module_docstring(self):
        from models import service
        module = service.__doc__
        self.assertIsNot(module, None,
                         "service.py needs a docstring")
        self.assertTrue(len(module) > 1,
                        "service.py needs a docstring")

    def test_class_docstring(self):
        self.assertIsNot(Service.__doc__, None,
                         "Service class needs a docstring")
        self.assertTrue(len(Service.__doc__) >= 1,
                        "Service class needs a docstring")


class TestPep8(TestCase):
    """Tests the service.py and test_service.py module for pycodestyle"""

    def test_pep8_conformance(self):
        for path in ['models/service.py',
                     'tests/test_models/test_service.py']:
            with self.subTest(path=path):
                errors = pep8.Checker(path).check_all()
                self.assertEqual(errors, 0)
