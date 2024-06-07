from Basemodel import Basemodel
from datetime import datetime
import uuid


class Basemodel:
    def __init__(self, uuid, updated_at=datetime, created_at=datetime):
        self.id = uuid.uuid4()
        self.updated_at = updated_at
        self.created_at = created_at

    