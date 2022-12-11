#!/usr/bin/python3

"""
File: test_user.py
Desc: This module contains all possible testcases for the user.py
      module in the models package. It uses the standard unittest.
Authors: Gizachew Baynss, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 11 2022
"""

from models.user import User, BaseModel, Base
from unittest import TestCase
import pep8


class TestObjectCreation(TestCase):
    """A class to test object creation and their properties"""

    def test_for_inheritance(self):
        user = User(
            first_name="Gizachew",
            last_name="Bayness",
            email="eleccrazy24@gmail.com",
            password="password",
            phone="0909090909"
        )
        self.assertTrue(isinstance(user, BaseModel))
        self.assertTrue(isinstance(user, User))
        self.assertTrue(isinstance(user, Base))

    def test_object_creation(self):
        user = User(
            first_name="Gizachew",
            last_name="Bayness",
            email="eleccrazy24@gmail.com",
            password="password",
            phone="0909090909"
        )
        keys = user.__dict__.keys()
        properties = ['first_name', 'last_name', 'email',
                      'password', 'phone', 'id',
                      'created_at', 'updated_at']
        for property in properties:
            self.assertIn(property, keys)

    def test_for_encrypted_md5_user_password(self):
        user = User(
            first_name="Gizachew",
            last_name="Bayness",
            email="eleccrazy24@gmail.com",
            password="password",
            phone="0909090909"
        )
        self.assertNotEqual(user.password, "password")
        self.assertEqual(len(user.password), 32)


class TestDocstring(TestCase):
    """Tests docstrings"""

    def test_module_docstring(self):
        from models import user
        module = user.__doc__
        self.assertIsNot(module, None,
                         "user.py needs a docstring")
        self.assertTrue(len(module) > 1,
                        "user.py needs a docstring")

    def test_class_docstring(self):
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")


class TestPep8(TestCase):
    """Tests the user.py and test_user.py module for pycodestyle"""

    def test_pep8_conformance(self):
        for path in ['models/user.py',
                     'tests/test_models/test_user.py']:
            with self.subTest(path=path):
                errors = pep8.Checker(path).check_all()
                self.assertEqual(errors, 0)
