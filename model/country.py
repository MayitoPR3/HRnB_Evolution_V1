from model.city import City

class Country(City):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
