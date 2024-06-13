import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())  # Generates a unique identifier
        self.created_at = datetime.now().isoformat()  # ISO formatted creation timestamp
        self.updated_at = self.created_at  # Initially, creation and update times are the same

    def to_dict(self):
        """Method to convert the model attributes to a dictionary."""
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def update(self, data):
        """Updates the model with provided data."""
        for key, value in data.items():
            if hasattr(self, key) and key != 'id':  # Prevents changing the ID
                setattr(self, key, value)
        self.updated_at = datetime.now().isoformat()  # Update the updated_at timestamp whenever any change is made