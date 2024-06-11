#!/usr/bin/python3
from model.city import City

class Country(City):
    """this is a country class that represents a country"""
    def __init__(self, country_code):
        """initialize the country"""
        super().__init__()
        self.country_code = country_code

    def __str__(self):
        """returns a string representation of the review class"""
        return f"[Country] ({self.id}) {self.to_dict()}"
