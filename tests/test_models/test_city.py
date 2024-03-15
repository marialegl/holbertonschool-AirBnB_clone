#!/usr/bin/python3
"""Unittest for City"""

import unittest
from models.base_model import BaseModel
from models.city import City
import pycodestyle


class TestBaseModelpep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pycodestyle.StyleGuide(quiet=True)
        city_pep8 = "models/city.py"
        test_city_pep8 = "tests/test_models/test_city.py"
        result = style.check_files([city_pep8, test_city_pep8])
        self.assertEqual(result.total_errors, 0)


class TestCity(unittest.TestCase):
    def test_city_instance(self):
        """Test if City instance is created"""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_inherits_base_model(self):
        """Test if City inherits from BaseModel"""
        city = City()
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_attributes(self):
        """Test if City attributes are present"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))


if __name__ == "__main__":
    unittest.main()
