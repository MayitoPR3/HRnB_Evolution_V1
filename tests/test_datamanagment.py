#!/bin/usr/python3
from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        pass

class DataManager(IPersistenceManager):
    def __init__(self, storage):
        self.storage = storage

    def save(self, entity):
        self.storage.save(entity)

    def get(self, entity_id, entity_type):
        return self.storage.get(entity_id, entity_type)

    def update(self, entity):
        self.storage.update(entity)

    def delete(self, entity_id, entity_type):
        self.storage.delete(entity_id, entity_type)

class FileStorage:
    def save(self, entity):
        with open(f"{entity['id']}_{entity['type']}.txt", 'w') as f:
            f.write(str(entity))

    def get(self, entity_id, entity_type):
        try:
            with open(f"{entity_id}_{entity_type}.txt", 'r') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def update(self, entity):
        with open(f"{entity['id']}_{entity['type']}.txt", 'w') as f:
            f.write(str(entity))

    def delete(self, entity_id, entity_type):
        try:
            os.remove(f"{entity_id}_{entity_type}.txt")
        except FileNotFoundError:
            pass

# tests
file_storage = FileStorage()
data_manager = DataManager(file_storage)

entity = {"id": 1, "type": "test_entity", "name": "Example Entity"}
data_manager.save(entity)
retrieved_entity = data_manager.get(1, "example_entity")
print(retrieved_entity)
