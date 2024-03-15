#!/usr/bin/python3
""" Unittest for file_storage """

import pycodestyle
import unittest
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import os


class TestBaseModelpep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pycodestyle.StyleGuide(quiet=True)
        filestorage_pep8 = "models/engine/file_storage.py"
        fs_pep8 = "tests/test_models/test_engine/test_file_storage.py"
        result = style.check_files([filestorage_pep8, fs_pep8])
        self.assertEqual(result.total_errors, 0)


class TestFileStorage(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        if file_storage.__doc__ is not None:
            self.assertTrue(len(file_storage.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        if FileStorage.__doc__ is not None:
            self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(FileStorage):
            if func.__doc__ is not None:
                self.assertTrue(len(func.__doc__) > 0)

    def test_permissions(self):
        """test read-write-execute permissions"""
        read = os.access("models/engine/file_storage.py", os.R_OK)
        self.assertTrue(read)
        write = os.access("models/engine/file_storage.py", os.W_OK)
        self.assertTrue(write)
        exe = os.access("models/engine/file_storage.py", os.X_OK)
        self.assertTrue(exe)

    def test_instance(self):
        """check if obj is an instance of BaseModel"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)


if __name__ == "__main__":
    unittest.main()
