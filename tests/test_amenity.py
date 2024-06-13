import unittest
from flask import Flask
from flask_restx import Api
from api.api_amenities import ns as amenity_namespace
from datamanagment import DataManager
from datetime import datetime

class TestAmenityAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.api = Api(cls.app)
        cls.api.add_namespace(amenity_namespace)
        cls.client = cls.app.test_client()
        cls.data_manager = DataManager()

    def setUp(self):
        # Clear the data manager storage before each test
        self.data_manager.amenities = {}

    def test_get_all_amenities(self):
        response = self.client.get('/amenities/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_amenity(self):
        new_amenity = {
            "amenity_id": "amenity_1",
            "name": "Wi-Fi",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/amenities/', json=new_amenity)
        self.assertEqual(response.status_code, 201)
        self.assertIn('amenity_id', response.json)
        self.assertEqual(response.json['message'], 'Amenity created successfully')

    def test_create_duplicate_amenity(self):
        self.data_manager.amenities = {
            "amenity_1": {"amenity_id": "amenity_1", "name": "Wi-Fi"}
        }
        new_amenity = {
            "amenity_id": "amenity_2",
            "name": "Wi-Fi",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/amenities/', json=new_amenity)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json['message'], 'Amenity name already exists')

    def test_get_amenity_by_id(self):
        self.data_manager.amenities = {
            "amenity_1": {"amenity_id": "amenity_1", "name": "Wi-Fi"}
        }
        response = self.client.get('/amenities/amenity_1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['amenity_id'], 'amenity_1')

    def test_get_amenity_by_invalid_id(self):
        response = self.client.get('/amenities/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Amenity not found')

    def test_update_amenity(self):
        self.data_manager.amenities = {
            "amenity_1": {"amenity_id": "amenity_1", "name": "Wi-Fi"}
        }
        updated_amenity = {
            "name": "Updated Wi-Fi",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.put('/amenities/amenity_1', json=updated_amenity)
        self.assertEqual(response.status_code, 204)
        updated_amenity_data = self.data_manager.get_amenity("amenity_1")
        self.assertEqual(updated_amenity_data['name'], 'Updated Wi-Fi')

    def test_delete_amenity(self):
        self.data_manager.amenities = {
            "amenity_1": {"amenity_id": "amenity_1", "name": "Wi-Fi"}
        }
        response = self.client.delete('/amenities/amenity_1')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(self.data_manager.get_amenity("amenity_1"))

    def test_delete_invalid_amenity(self):
        response = self.client.delete('/amenities/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Amenity not found')


if __name__ == '__main__':
    unittest.main()
