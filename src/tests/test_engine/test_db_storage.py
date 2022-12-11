#!/usr/bin/python3

"""
File: test_db_storage.py
Desc: This module contains all possible testcases for the db_storage.py
      module in the models package. It uses the standard unittest.
Authors: Gizachew Bayness, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 11 2022
"""

from unittest import TestCase
import pep8


class TestDocstring(TestCase):
    """Tests docstrings"""

    def test_module_docstring(self):
        from engine import db_storage
        module = db_storage.__doc__
        self.assertIsNot(module, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(module) > 1,
                        "db_storage.py needs a docstring")

    def test_class_docstring(self):
        from engine.db_storage import Storage
        self.assertIsNot(Storage.__doc__, None,
                         "Storage class needs a docstring")
        self.assertTrue(len(Storage.__doc__) >= 1,
                        "Storage class needs a docstring")

    def test_function_docstrings(self):
        from engine.db_storage import Storage
        import inspect
        storage_funcs = inspect.getmembers(Storage, inspect.isfunction)
        for f in storage_funcs:
            with self.subTest(function=f):
                self.assertIsNot(
                    f[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(f[0])
                )
                self.assertTrue(
                    len(f[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(f[0]))

    class TestPep8(TestCase):
        """Tests the user.py and test_user.py module for pycodestyle"""

        def test_pep8_conformance(self):
            for path in ['engine/db_storage.py',
                         'tests/test_engine/test_db_storage.py']:
                with self.subTest(path=path):
                    errors = pep8.Checker(path).check_all()
                    self.assertEqual(errors, 0)
