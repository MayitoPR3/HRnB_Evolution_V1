#!/usr/bin/python3
from base_model import Basemodel

class Amenities(Basemodel):
    """this class represents the Amenities"""
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description

    def __str__(self):
        """returns a string representation of the review class"""
        return f"[Amenities] ({self.id}) {self.to_dict()}"
