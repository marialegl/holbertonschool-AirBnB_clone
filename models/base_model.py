#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "id":
                    self.id == value
                elif key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dictCopy = self.__dict__.copy()
        dictCopy["__class__"] = self.__class__.__name__
        dictCopy["created_at"] = self.created_at.isoformat()
        dictCopy["updated_at"] = self.updated_at.isoformat()
        return dictCopy
