from model.base_model import Basemodel


class Review(Basemodel):
    def __init__(self, comment, rating):
        super().__init__()  # Call the __init__ method of the BaseModel class
        self.comment = comment
        self.rating = rating

    def __str__(self):
        return f"[Review] ({self.id}) {self.to_dict()}"
