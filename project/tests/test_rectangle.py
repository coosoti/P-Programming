import unittest
from unittest.mock import patch
import json
from models.rectangle import Rectangle
from models.base import Base
import inspect


class TestRectangle(unittest.TestCase):
    """unittest for the Rectangle class"""

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(8, 8)
        cls.r2 = Rectangle(2, 3, 4)
        cls.base_functions = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_func_docstrings(self):
        """Tests for the existence of docstrings in all functions"""
        for func_name, func in self.base_functions:
            self.assertTrue(func.__doc__ is not None, f"Missing docstring for function: {func_name}")

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_save_to_file(self, mock_open):
        """Tests regular use of save_to_file"""
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        l = [r1, r2]

        with patch('models.rectangle.Rectangle.to_json_string') as mock_to_json:
            mock_to_json.return_value = 'json_string'
            Rectangle.save_to_file(l)

        mock_open.assert_called_once_with('Rectangle.json', 'w', encoding='utf-8')
        handle = mock_open()
        handle.write.assert_called_once_with('json_string')

    def test_save_to_file(self):
        """test regular use of save_to_file"""
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        l = [r1, r2]
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            ls = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

