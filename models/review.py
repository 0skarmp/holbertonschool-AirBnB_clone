#!/usr/bin/python3
""" This module has a class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ this class define the Review  """

    place_id = ""
    user_id = ""
    text = ""
