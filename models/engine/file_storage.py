#!/usr/bin/python3
"""A module to store data"""


import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """A class to store instances data"""
    __file_path = "database.json"
    __objects = {}

    def all(self):
        """A method the returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__class__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            tmp_dict = {}
            for key, value in FileStorage.__objects.items():
                tmp_dict[key] = value.to_dict()
            json.dump(tmp_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        classes = {'BaseModel': BaseModel, 'User': User,
                   'Amenity': Amenity, 'City': City, 'State': State,
                   'Place': Place, 'Review': Review}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                ds_file = json.load(f)
                if ds_file:
                    for key, value in ds_file.items():
                        class_name = key.split('.')[0]
                        class_type = classes[class_name]
                        obj = class_type(**value)
                        FileStorage.__objects[key] = obj
                else:
                    return
        else:
            return
