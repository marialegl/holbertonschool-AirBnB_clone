#!/usr/bin/python3
"""Unittest for City"""

import unittest
from models.base_model import BaseModel
from models.city import City


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
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

if __name__ == '__main__':
    unittest.main()
