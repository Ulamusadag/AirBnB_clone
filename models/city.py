#!/usr/bin/python3
"""City Module"""
form models.base_model import BaseModel


class City(BaseModel):
    """A class inheris from the BaseModel
    Attributes:
    state_id (str):empty string: it will be the State.id
    name (str): empty string"""

    state_id = ""
    name = ""
