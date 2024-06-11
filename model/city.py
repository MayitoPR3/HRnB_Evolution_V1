#!/usr/bin/python3
from model.base_model import Basemodel


class City(Basemodel):
    """this is a city class that represents a city"""
    def __init__(self, city_name, country_code, place_name):
        super().__init__()
        self.city_name = city_name
        self.country_code = country_code
        self.place_name = place_name
    
    def add_city(self, city_name):
        """"Add a new city"""
        self.city_name.append(city_name)
        self.place_name.append(city_name)
        
    def __str__(self):
        """returns a string representation of the city"""
        return f"[City] ({self.id}) {self.to_dict()}"