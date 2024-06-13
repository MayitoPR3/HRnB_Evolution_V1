import unittest
from flask import Flask
from flask_restx import Api
from api.api_review import ns as review_namespace
from datamanagment import DataManager
from datetime import datetime


class TestReviewAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.api = Api(cls.app)
        cls.api.add_namespace(review_namespace)
        cls.client = cls.app.test_client()
        cls.data_manager = DataManager()

    def setUp(self):
        # Clear the data manager storage before each test
        self.data_manager.reviews = {}
        self.data_manager.places = {
            "place_1": {"id": "place_1", "name": "Place 1", "host_id": "host_1"}
        }
        self.data_manager.users = {
            "user_1": {"id": "user_1", "name": "User 1"},
            "host_1": {"id": "host_1", "name": "Host 1"}
        }

    def test_get_all_reviews(self):
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_review(self):
        new_review = {
            "user_id": "user_1",
            "place_id": "place_1",
            "rating": 5,
            "comment": "Great place!",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/reviews/', json=new_review)
        self.assertEqual(response.status_code, 201)
        self.assertIn('review_id', response.json)
        self.assertEqual(response.json['message'], 'Review created successfully')

    def test_create_review_invalid_user(self):
        new_review = {
            "user_id": "invalid_user",
            "place_id": "place_1",
            "rating": 5,
            "comment": "Great place!",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/reviews/', json=new_review)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid user ID')

    def test_create_review_invalid_place(self):
        new_review = {
            "user_id": "user_1",
            "place_id": "invalid_place",
            "rating": 5,
            "comment": "Great place!",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/reviews/', json=new_review)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Invalid place ID')

    def test_create_review_invalid_rating(self):
        new_review = {
            "user_id": "user_1",
            "place_id": "place_1",
            "rating": 6,  # Invalid rating
            "comment": "Great place!",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/reviews/', json=new_review)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Rating must be between 1 and 5')

    def test_create_review_host_reviewing_own_place(self):
        new_review = {
            "user_id": "host_1",
            "place_id": "place_1",
            "rating": 5,
            "comment": "Great place!",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.post('/reviews/', json=new_review)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Users cannot review their own place')

    def test_get_review_by_id(self):
        self.data_manager.reviews = {
            "review_1": {"id": "review_1", "user_id": "user_1", "place_id": "place_1", "rating": 5, "comment": "Great place!"}
        }
        response = self.client.get('/reviews/review_1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 'review_1')

    def test_get_review_by_invalid_id(self):
        response = self.client.get('/reviews/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Review not found')

    def test_update_review(self):
        self.data_manager.reviews = {
            "review_1": {"id": "review_1", "user_id": "user_1", "place_id": "place_1", "rating": 5, "comment": "Great place!"}
        }
        updated_review = {
            "user_id": "user_1",
            "place_id": "place_1",
            "rating": 4,
            "comment": "Updated review",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        response = self.client.put('/reviews/review_1', json=updated_review)
        self.assertEqual(response.status_code, 204)
        updated_review_data = self.data_manager.get_review("review_1")
        self.assertEqual(updated_review_data['rating'], 4)
        self.assertEqual(updated_review_data['comment'], 'Updated review')

    def test_delete_review(self):
        self.data_manager.reviews = {
            "review_1": {"id": "review_1", "user_id": "user_1", "place_id": "place_1", "rating": 5, "comment": "Great place!"}
        }
        response = self.client.delete('/reviews/review_1')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(self.data_manager.get_review("review_1"))

    def test_delete_invalid_review(self):
        response = self.client.delete('/reviews/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Review not found')


if __name__ == '__main__':
    unittest.main()
