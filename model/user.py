
class User:
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

    
    

    
