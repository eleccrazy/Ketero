#!/usr/bin/python3

"""
File: test_base.py
Desc: This module contains all possible testcases for the base.py
      module in the models package. It uses the standard unittest.
Authors: Gizachew Baynss, Joseph Tapano, and Helina Gebreyes
Date Created: Dec 9 2022
"""

from models.base import BaseModel
from unittest import TestCase
from datetime import datetime
import pep8


class TestObjectInstantiation(TestCase):
    """A class to test basic object creation"""

    def test_one_obj(self):
        b = BaseModel()
        self.assertEqual(BaseModel, type(b))

    def test_two_objs(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_type_of_id(self):
        b = BaseModel()
        self.assertEqual(type(b.id), str)

    def test_type_of_created_at(self):
        b = BaseModel()
        self.assertEqual(type(b.created_at), datetime)

    def test_type_of_updated_at(self):
        b = BaseModel()
        self.assertEqual(type(b.updated_at), datetime)

    def test_different_creation_time(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertGreater(b2.created_at, b1.created_at)

    def test_with_kwargs(self):
        utc = datetime.utcnow().isoformat()
        fmt = '%Y-%m-%dT%H:%M:%S.%f'
        b = BaseModel(id="hello", created_at=utc, updated_at=utc)
        self.assertEqual(b.id, "hello")
        self.assertEqual(b.created_at, datetime.strptime(utc, fmt))
        self.assertEqual(b.updated_at, datetime.strptime(utc, fmt))

    def test_with_args_kwargs(self):
        b = BaseModel(1, "love", id="98989797")
        self.assertEqual(b.id, "98989797")


class TestStrMethod(TestCase):
    """A class to test the str method"""

    def test_simple_str_representation(self):
        b = BaseModel()
        b_str = b.__str__()
        self.assertIn("[BaseModel] ({})".format(b.id), b_str)

    def test_str_with_possible_attributes(self):
        d = datetime.utcnow()
        d_repr = repr(d)
        b = BaseModel("Elec Crazy")
        b.created_at = b.updated_at = d
        b_str = b.__str__()
        self.assertIn("[BaseModel] ({})".format(b.id), b_str)
        self.assertIn("'id': '{}'".format(b.id), b_str)
        self.assertIn("'created_at': " + d_repr, b_str)
        self.assertIn("'updated_at': " + d_repr, b_str)


class TestDocstring(TestCase):
    """Tests docstrings"""

    def test_module_docstring(self):
        from models import base
        module = base.__doc__
        self.assertIsNot(module, None,
                         "base.py needs a docstring")
        self.assertTrue(len(module) > 1,
                        "base.py needs a docstring")

    def test_class_docstring(self):
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_function_docstrings(self):
        import inspect
        base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)
        for f in base_funcs:
            with self.subTest(function=f):
                self.assertIsNot(
                    f[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(f[0])
                )
                self.assertTrue(
                    len(f[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(f[0])
                )


class TestToDictMethod(TestCase):
    """Tests the to_dict method"""

    def test_to_dict(self):
        my_model = BaseModel()
        my_model.name = "Ketero"
        my_model.my_number = 777
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Ketero")
        self.assertEqual(d['my_number'], 777)

    def test_to_dict_values(self):
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        bm = BaseModel()
        new_d = bm.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], bm.updated_at.strftime(t_format))


class TestPep8(TestCase):
    """Tests the base.py and test_base.py module for pycodestyle"""

    def test_pep8_conformance(self):
        for path in ['models/base.py',
                     'tests/test_models/test_base.py']:
            with self.subTest(path=path):
                errors = pep8.Checker(path).check_all()
                self.assertEqual(errors, 0)
