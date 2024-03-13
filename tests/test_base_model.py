#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class Test_base_model(unittest.TestCase):
    def unique_id(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1, instance2)


if __name__ == "__main__":
    unittest.main()
