from Basemodel import Basemodel


class User(Basemodel):
    def __init__(self, user_id, first_name, last_name, password):
        
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@gmail.com'
        self.password = password
        self.places = []
        self.reviews = []
        self.city = None
        self.country = None

    def add_place(self, place):
        self.places.append(place)
        
    def add_review(self, review):
        self.reviews.append(review)
        
    def set_city(self, city):
        self.city = city
        
    def set_country(self, country):
        self.country = country
        
    

    
