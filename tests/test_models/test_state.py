#!/usr/bin/python3
"""Unittest for State"""

import unittest
from models.base_model import BaseModel
from models.state import State
import pycodestyle


class TestBaseModelpep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pycodestyle.StyleGuide(quiet=True)
        state_pep8 = "models/state.py"
        test_state_pep8 = "tests/test_models/test_state.py"
        result = style.check_files([state_pep8, test_state_pep8])
        self.assertEqual(result.total_errors, 0)


class TestState(unittest.TestCase):
    def test_state_instance(self):
        """Test if State instance is created"""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_inherits_base_model(self):
        """Test if State inherits from BaseModel"""
        state = State()
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_attribute_name(self):
        """Test if State has 'name' attribute"""
        state = State()
        self.assertTrue(hasattr(state, "name"))


if __name__ == "__main__":
    unittest.main()
