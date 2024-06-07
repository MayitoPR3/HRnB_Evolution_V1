from model.base_model import Basemodel


class User(Basemodel):
    """class for the User
    """
    def __init__(self, email, password, first_name="", last_name="", **kwargs):
        """initializes the function of user information"""
        super().__init__(**kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.places = []
        self.reviews = []
        
    def update_name(self, first_name="", last_name=""):
        """ defines the process to update the name"""
        self.first_name = first_name
        self.last_name = last_name
        
    def __str__(self):
        return f"[User] ({self.id}) {self.to_dict()}"
    
    

    
