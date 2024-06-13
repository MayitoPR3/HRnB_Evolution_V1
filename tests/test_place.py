import unittest
from flask import Flask
from flask_restx import Api
from api.api_places import ns as place_namespace
from datamanagment import DataManager
from datetime import datetime

class TestPlaceAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.api = Api(cls.app)
        cls.api.add_namespace(place_namespace)
        cls.client = cls.app.test_client()
        cls.data_manager = DataManager()

    def setUp(self):
        # Clear the data manager storage before each test
        self.data_manager.places = {}
        self.data_manager.cities = {
            "city_1": {"city_id": "city_1", "name": "City 1", "country_id": "country_1"}
        }
        self.data_manager.amenities = {
            "amenity_1": {"amenity_id": "amenity_1", "name": "Wi-Fi"}
        }

    def test_get_all_places(self):
        response = self.client.get('/places/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_place(self):
        new_place = {
            "name": "Place 1",
            "description": "A nice place",
            "address": "123 Main St",
            "city_id": "city_1",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": "host_1",
            "number_of_rooms": 3,
            "number_of_bathrooms": 2,
            "price_per_night": 150.0,
            "max_guests": 5,
            "amenity_ids": ["amenity_1"],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/places/', json=new_place)
        self.assertEqual(response.status_code, 201)
        self.assertIn('place_id', response.json)
        self.assertEqual(response.json['message'], 'Place created successfully')

    def test_create_place_invalid_city(self):
        new_place = {
            "name": "Place 1",
            "description": "A nice place",
            "address": "123 Main St",
            "city_id": "invalid_city",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": "host_1",
            "number_of_rooms": 3,
            "number_of_bathrooms": 2,
            "price_per_night": 150.0,
            "max_guests": 5,
            "amenity_ids": ["amenity_1"],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/places/', json=new_place)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid city ID')

    def test_create_place_invalid_amenity(self):
        new_place = {
            "name": "Place 1",
            "description": "A nice place",
            "address": "123 Main St",
            "city_id": "city_1",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": "host_1",
            "number_of_rooms": 3,
            "number_of_bathrooms": 2,
            "price_per_night": 150.0,
            "max_guests": 5,
            "amenity_ids": ["invalid_amenity"],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/places/', json=new_place)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'One or more invalid amenity IDs')

    def test_create_place_invalid_latitude(self):
        new_place = {
            "name": "Place 1",
            "description": "A nice place",
            "address": "123 Main St",
            "city_id": "city_1",
            "latitude": 100.0,  # Invalid latitude
            "longitude": -74.0060,
            "host_id": "host_1",
            "number_of_rooms": 3,
            "number_of_bathrooms": 2,
            "price_per_night": 150.0,
            "max_guests": 5,
            "amenity_ids": ["amenity_1"],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/places/', json=new_place)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid latitude')

    def test_create_place_invalid_longitude(self):
        new_place = {
            "name": "Place 1",
            "description": "A nice place",
            "address": "123 Main St",
            "city_id": "city_1",
            "latitude": 40.7128,
            "longitude": 200.0,  # Invalid longitude
            "host_id": "host_1",
            "number_of_rooms": 3,
            "number_of_bathrooms": 2,
            "price_per_night": 150.0,
            "max_guests": 5,
            "amenity_ids": ["amenity_1"],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/places/', json=new_place)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid longitude')

    def test_create_place_negative_values(self):
        new_place = {
            "name": "Place 1",
            "description": "A nice place",
            "address": "123 Main St",
            "city_id": "city_1",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": "host_1",
            "number_of_rooms": -1,  # Invalid value
            "number_of_bathrooms": -1,  # Invalid value
            "price_per_night": -1.0,  # Invalid value
            "max_guests": -1,  # Invalid value
            "amenity_ids": ["amenity_1"],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/places/', json=new_place)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid room, bathroom, or guest count')

    def test_get_place_by_id(self):
        self.data_manager.places = {
            "place_1": {"id": "place_1", "name": "Place 1", "description": "A nice place"}
        }
        response = self.client.get('/places/place_1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 'place_1')

    def test_get_place_by_invalid_id(self):
        response = self.client.get('/places/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Place not found')

    def test_update_place(self):
        self.data_manager.places = {
            "place_1": {"id": "place_1", "name": "Place 1", "description": "A nice place"}
        }
        updated_place = {
            "name": "Updated Place 1",
            "description": "An updated nice place",
            "city_id": "city_1",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": "host_1",
            "number_of_rooms": 4,
            "number_of_bathrooms": 3,
            "price_per_night": 200.0,
            "max_guests": 6,
            "amenity_ids": ["amenity_1"],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.put('/places/place_1', json=updated_place)
        self.assertEqual(response.status_code, 204)
        updated_place_data = self.data_manager.get_place("place_1")
        self.assertEqual(updated_place_data['name'], 'Updated Place 1')

    def test_delete_place(self):
        self.data_manager.places = {
            "place_1": {"id": "place_1", "name": "Place 1", "description": "A nice place"}
        }
        response = self.client.delete('/places/place_1')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(self.data_manager.get_place("place_1"))

    def test_delete_invalid_place(self):
        response = self.client.delete('/places/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Place not found')


if __name__ == '__main__':
    unittest.main()
