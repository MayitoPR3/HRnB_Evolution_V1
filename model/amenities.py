#!/usr/bin/python3
from model.base_model import Basemodel

class Amenities(Basemodel):
    """this class represents the Amenities"""
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
