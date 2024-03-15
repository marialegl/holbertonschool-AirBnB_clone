#!/usr/bin/python3
"""Unittest for User"""

import unittest
import pycodestyle
from models.user import User


class TestUser(unittest.TestCase):
    def test_user_instance(self):
        """Test if User instance is created"""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """Test if User attributes are present"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_inherits_base_model(self):
        """Test if User inherits from BaseModel"""
        user = User()
        self.assertTrue(issubclass(User, BaseModel))

if __name__ == '__main__':
    unittest.main()
