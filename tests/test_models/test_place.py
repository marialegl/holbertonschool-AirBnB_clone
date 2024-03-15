#!/usr/bin/python3
"""Unittest for Place"""

import unittest
import pycodestyle
from models.base_model import BaseModel
from models.place import Place


class TestBaseModelpep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pycodestyle.StyleGuide(quiet=True)
        place_pep8 = "models/place.py"
        test_place_pep8 = "tests/test_models/test_place.py"
        result = style.check_files([place_pep8, test_place_pep8])
        self.assertEqual(result.total_errors, 0)


class TestPlace(unittest.TestCase):
    def test_place_instance(self):
        """Test if Place instance is created"""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_inherits_base_model(self):
        """Test if Place inherits from BaseModel"""
        place = Place()
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_attributes(self):
        """Test if Place attributes are present"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))


if __name__ == "__main__":
    unittest.main()
