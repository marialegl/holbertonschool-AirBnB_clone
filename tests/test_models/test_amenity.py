#!/usr/bin/python3
"""Unittest for BaseModel"""

import unittest
import pycodestyle
from models import amenity
from models.amenity import Amenity


class Test_Base_Model_Pep8(unittest.TestCase):
    """Validate Pep8"""

    def test_pep8(self):
        """
        test for base_model file for validar pep8 style
        """

        style = pycodestyle.StyleGuide(quiet=False)
        amenity_pep8 = "models/base_model.py"
        test_amenity_pep8 = "tests/test_models/test_amenity.py"
        result = style.check_files([amenity_pep8, test_amenity_pep8])
        self.assertEqual(result.total_errors, 0)


class TestAmenity(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)
