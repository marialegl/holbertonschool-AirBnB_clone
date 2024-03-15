#!/usr/bin/python3
"""Unittest for User"""

import unittest
import pycodestyle
from models.base_model import BaseModel
from models.user import User


class TestBaseModelpep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pycodestyle.StyleGuide(quiet=True)
        user_pep8 = "models/user.py"
        test_user_pep8 = "tests/test_models/test_user.py"
        result = style.check_files([user_pep8, test_user_pep8])
        self.assertEqual(result.total_errors, 0)


class TestUser(unittest.TestCase):
    def test_user_instance(self):
        """Test if User instance is created"""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """Test if User attributes are present"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_user_inherits_base_model(self):
        """Test if User inherits from BaseModel"""
        user = User()
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    unittest.main()
