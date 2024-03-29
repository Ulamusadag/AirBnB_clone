#!/usr/bin/python3
"""The review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A review of a place/house

    Attributes:
        text
        user_id
        place_id
    """
    text = ""
    user_id = ""
    place_id = ""
