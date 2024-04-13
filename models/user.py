#!/usr/bin/python3
"""User Module"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class user that inherit form the base_model
    and creates new user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
