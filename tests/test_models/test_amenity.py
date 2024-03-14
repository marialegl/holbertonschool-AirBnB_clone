#!/usr/bin/python3
"""Unittest for BaseModel"""

import unittest
import pycodestyle
from models.base_model import BaseModel


class Test_Base_Model_Pep8(unittest.TestCase):
    """Validate Pep8"""

    def test_pep8(self):
        """
        test for base_model file for validar pep8 style
        """

        style = pycodestyle.StyleGuide(quiet=False)
        base_model = "models/base_model.py"
        test_base_model = "test_base_model.py"
        result = style.check_files([base_model, test_base_model])
        self.assertEqual(result.total_errors, 0)
