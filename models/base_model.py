#!/usr/bin/python3
""" this is the base_model """


import uuid
from datetime import datetime


class BaseModel:
    """ The Base Model class """

    def __init__(self, *args, **kwargs):
        """
        __init__ constructor method
        This method recreates an instance if attributes provided
        otherwise create a new one

        Args:
            args: takes positional arguments
            kwargs: takes key-value arguments
        """

        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    to_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, to_dt)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        string representation to the object
        """

        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        save is a method that will update current date time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        to_dict = self.__dict__
        to_dict["__class__"] = self.__class__.__name__
        to_dict["created_at"] = to_dict["created_at"].isoformat()
        to_dict["updated_at"] = to_dict["updated_at"].isoformat()
        return to_dict
