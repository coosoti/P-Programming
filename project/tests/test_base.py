#!/usr/bin/python3

import inspect
import json
from models import base
from models.base import Base
from unittest.mock import patch
import unittest

class TestBase(unittest.TestCase):
    """unittest class for the Base class"""

    @classmethod
    def setUpClass(cls):
        """Importing all functions from Base class"""
        cls.base_functions = inspect.getmembers(Base, inspect.isfunction)
    
    def test_func_docstrings(self):
        """Tests for the existence of docstrings in all functions"""
        for func_name, func in self.base_functions:
            self.assertTrue(func.__doc__ is not None, f"Missing docstring for function: {func_name}")

    def test_to_json_string(self):
        dict1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        dict2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_str = Base.to_json_string([dict1, dict2])
        self.assertIsInstance(json_str, str)
        d = json.loads(json_str) #convert back to list objects of two dictionaries
        self.assertEqual(d, [dict1, dict2])



if __name__ == '__main__':
    unittest.main()
