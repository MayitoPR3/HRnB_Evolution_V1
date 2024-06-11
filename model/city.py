from model.base_model import Basemodel


class City(Basemodel):
    def __init__(self, name, country_code, place):
        super().__init__()
        self.name = name
        self.country_code = country_code
        self.places = place
    
    def add_city(self, name):
        self.name.append(name)
        self.places.append(name)
        
