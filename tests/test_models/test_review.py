#!/usr/bin/python3
"""Unittest for Review"""

import unittest
from models.base_model import BaseModel
from models.review import Review
import pycodestyle


class TestBaseModelpep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pycodestyle.StyleGuide(quiet=True)
        review_pep8 = "models/review.py"
        test_review_pep8 = "tests/test_models/test_review.py"
        result = style.check_files([review_pep8, test_review_pep8])
        self.assertEqual(result.total_errors, 0)


class TestReview(unittest.TestCase):
    def test_review_instance(self):
        """Test if Review instance is created"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_inherits_base_model(self):
        """Test if Review inherits from BaseModel"""
        review = Review()
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_attributes(self):
        """Test if Review attributes are present"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))


if __name__ == "__main__":
    unittest.main()
