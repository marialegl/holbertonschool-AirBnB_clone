#!/usr/bin/python3

import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(cls):
        return FileStorage.__objects

    @classmethod
    def new(cls, obj):
        if obj:
            className = obj.__class__.__name__
            key = f"{className}.{obj.id}"
            FileStorage._objects[key] = obj

    def save(self):
        """Serializes __object to the json file"""
        newDict = {}
        for key, obj in FileStorage.__objects.items():
            newDict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(newDict, file, default=str)

    def reload(self):
        """Deserialize json file"""
        try:
            with open(self.__file_path, "r") as file:
                tempDict = json.load(file)
                for key, value in tempDict.items():
                    keyObj = key.split(".")
                    tmpName = eval(keyObj[0])(**value)
                    FileStorage.__objects[key] = tmpName
        except Exception:
            pass
