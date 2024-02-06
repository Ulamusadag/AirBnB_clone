#!/usr/bin/python3
""" this is the base_model """

import uuid
from datetime import datetime

class BaseModel:
	""" The Base Mode3l class """

	def __init__(self, *args, **kwargs):
		"""
		__init__ constructor method

		Args:
		args: takes positional arguments
		kwargs: takes key-value arguments
		"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now
		self.updated_at = self.created_at

	def __str__(self):
		"""
		string representasion to the object
		"""
	
		return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self__dict__))
		
	def save(self):
		"""
		save is a method that will update current date time
		"""
		
		self.update_at = datetime.now

	def to_dict(self):
		"""
		returns a dictionary containing all keys/values of __dict__
		"""
		dict = dict(self.__dict__)
		dict["__class__"] = self.__class__.__name
		dict["created_at"] = dict["created_at"].isoformat()
		dict["updated_at"] = dict["updated_at"].isoformat()
		return dict
