import unittest
from flask import Flask
from flask_restx import Api
from api.api_city import ns as city_namespace
from datamanagment import DataManager
from datetime import datetime

class TestCityAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.api = Api(cls.app)
        cls.api.add_namespace(city_namespace)
        cls.client = cls.app.test_client()
        cls.data_manager = DataManager()

    def setUp(self):
        # Clear the data manager storage before each test
        self.data_manager.cities = {}
        self.data_manager.countries = {
            "country_1": {"country_code": "country_1", "name": "Country 1"}
        }

    def test_get_all_cities(self):
        response = self.client.get('/cities/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_city(self):
        new_city = {
            "city_id": "city_1",
            "name": "City 1",
            "country_id": "country_1",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/cities/', json=new_city)
        self.assertEqual(response.status_code, 201)
        self.assertIn('city_id', response.json)
        self.assertEqual(response.json['message'], 'City created successfully')

    def test_create_city_invalid_country(self):
        new_city = {
            "city_id": "city_1",
            "name": "City 1",
            "country_id": "invalid_country",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/cities/', json=new_city)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid country ID')

    def test_create_city_duplicate_name(self):
        self.data_manager.cities = {
            "city_1": {"city_id": "city_1", "name": "City 1", "country_id": "country_1"}
        }
        new_city = {
            "city_id": "city_2",
            "name": "City 1",
            "country_id": "country_1",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/cities/', json=new_city)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json['message'], 'City name already exists in the specified country')

    def test_get_city_by_id(self):
        self.data_manager.cities = {
            "city_1": {"city_id": "city_1", "name": "City 1", "country_id": "country_1"}
        }
        response = self.client.get('/cities/city_1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['city_id'], 'city_1')

    def test_get_city_by_invalid_id(self):
        response = self.client.get('/cities/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'City not found')

    def test_update_city(self):
        self.data_manager.cities = {
            "city_1": {"city_id": "city_1", "name": "City 1", "country_id": "country_1"}
        }
        updated_city = {
            "name": "Updated City 1",
            "country_id": "country_1",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.put('/cities/city_1', json=updated_city)
        self.assertEqual(response.status_code, 204)
        updated_city_data = self.data_manager.get_city("city_1")
        self.assertEqual(updated_city_data['name'], 'Updated City 1')

    def test_delete_city(self):
        self.data_manager.cities = {
            "city_1": {"city_id": "city_1", "name": "City 1", "country_id": "country_1"}
        }
        response = self.client.delete('/cities/city_1')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(self.data_manager.get_city("city_1"))

    def test_delete_invalid_city(self):
        response = self.client.delete('/cities/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'City not found')


if __name__ == '__main__':
    unittest.main()
