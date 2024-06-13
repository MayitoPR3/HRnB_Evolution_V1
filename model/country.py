#!/usr/bin/python3
from base_model import BaseModel


class Country(BaseModel):
    """this is a country class that represents a country"""
    def __init__(self, name, country_code):
        """initialize the country"""
        super().__init__()
        self.name = name
        self.country_code = country_code

    def __str__(self):
        """returns a string representation of the review class"""
        return f"[Country] ({self.id}) {self.to_dict()}"
