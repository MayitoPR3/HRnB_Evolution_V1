#!/usr/bin/python3
from model.city import City

class Country(City):
    def __init__(self, country_code):
        super().__init__()
        self.country_code = country_code
