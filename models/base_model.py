#!/usr/bin/python3
"""This is the base_model"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """The Base Model class"""

    def __init__(self, *args, **kwargs):
        """
        __init__ constructor method
        This method recreates an instance if attributes provided
        otherwise create a new one

        Args:
            args: takes positional arguments
            kwargs: takes key-value arguments
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation to the object
        """
        return ("[{}] ({}) {}"
                .format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """
        save is a method that will update current date time
        when any attribute get updated
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        """
        dict_var = {**self.__dict__}
        dict_var["__class__"] = type(self).__name__
        dict_var["created_at"] = dict_var["created_at"].isoformat()
        dict_var["updated_at"] = dict_var["updated_at"].isoformat()

        return dict_var
