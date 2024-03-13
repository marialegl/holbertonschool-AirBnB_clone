#!/usr/bin/python3
import unitest
import pycodestyle
from models.base_model import BaseModel

class Test_base_model(unitest.TestCase):
    def unique_id(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1, instance2)
