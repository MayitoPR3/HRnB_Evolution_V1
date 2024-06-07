from datetime import datetime
from Basemodel import Basemodel


class Reviews(Basemodel):
    def __init__(self, user_feedback, place_rating):
        
        self.user_feedback = user_feedback
        self.place_rating = place_rating

    