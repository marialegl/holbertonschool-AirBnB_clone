#!usr/bin/python3
""" Class User that inherits from BaseModel """

from models.base_model import BaseModel


class City(BaseModel):
    """Public class attribute"""

    state_id = ""
    name = ""
