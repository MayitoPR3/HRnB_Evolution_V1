#!/usr/bin/python3
from base_model import BaseModel


class Review(BaseModel):
    """class for Reviews
    """
    def __init__(self, comment, rating):
        """defines the init method for the review class"""
        super().__init__()  # Call the __init__ method of the BaseModel class
        self.comment = comment
        self.rating = rating

    def __str__(self):
        """returns a string representation of the review class"""
        return f"[Review] ({self.id}) {self.to_dict()}"
