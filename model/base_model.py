#!/usr/bin/python3
from datetime import datetime
import uuid


class Basemodel:
    """class Basemodel where every class will be connected
    """
    def __init__(self, id=None, created_at=None, updated_at=None):
        """initialization of the class

            id or uuid : creates a UUID4 for every process
            updated_at : created the updated time of the request
            created_at : creates the creation time of the request
        """
        self.id = id or str(uuid.uuid4())
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
      
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return self.__dict__