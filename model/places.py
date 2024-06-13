#!/usr/bin/python3
from base_model import Basemodel


class Place(Basemodel):
    """This class represents the Place object"""
    def __init__(self, place_name, place_description, place_address, number_rooms, 
                 number_of_bathrooms, price_per_night, max_guests, latitude, longitude):
        """initialize the Place object"""
        super().__init__()  # Call the __init__ method of the BaseModel class
        self.place_name = place_name
        self.description = place_description
        self.address = place_address
        self.number_rooms = number_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.latitude = latitude
        self.longitude = longitude
     
    def __str__(self):
        """returns a string representation of this object"""
        return f"[Place] ({self.id}) {self.to_dict()}"
