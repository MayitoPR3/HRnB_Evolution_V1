from base_model import BaseModel

class Country(BaseModel):
    def __init__(self, name, country_code):
        super().__init__()
        self.name = name
        self.country_code = country_code

    def __str__(self):
        return f"Country({self.id}): {self.name}, Code: {self.country_code}"
