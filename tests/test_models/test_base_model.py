#!/usr/bin/python3
"""Unittest for BaseModel"""

import unittest
import pycodestyle
from models.base_model import BaseModel
import time


class Test_Base_Model(unittest.TestCase):
    """Outputs tests for Base Model"""

    def test_unique_id(self):
        """
        method to test if id is unique
        """

        firstInstance = BaseModel()
        secondInstance = BaseModel()
        self.assertNotEqual(firstInstance, secondInstance)

    def test_save(self):
        """
        method to test if each time that the instance is
        saved the updated_at attribute is update
        """

        firstInstance = BaseModel()
        attrUpdatedSaveBefore = firstInstance.updated_at
        time.sleep(1)
        firstInstance.save()
        attrUpdatedSaveAfter = firstInstance.updated_at
        self.assertNotEqual(attrUpdatedSaveBefore, attrUpdatedSaveAfter)

    def test_to_dict(self):
        """
        method that test if a dictionary is returned a if updated_at and
        created_at attributes are in the correct format
        """

        firstInstance = BaseModel()

        updated_expected = firstInstance.updated_at.isoformat()
        created_expected = firstInstance.created_at.isoformat()

        update_current_format = firstInstance.to_dict()["updated_at"]
        created_current_format = firstInstance.to_dict()["created_at"]

        self.assertEqual(updated_expected, update_current_format)
        self.assertEqual(created_expected, created_current_format)


class Test_Base_Model_Pep8(unittest.TestCase):
    """Validate Pep8"""

    def test_pep8(self):
        """
        test for base_model file for validar pep8 style
        """

        style = pycodestyle.StyleGuide(quiet=False)
        base_model = "models/base_model.py"
        test_base_model = "tests/test_models/test_base_model.py"
        result = style.check_files([base_model, test_base_model])
        self.assertEqual(result.total_errors, 0)
