import unittest
import datetime
import time  # Import the time module
from model.user import User


class TestUser(unittest.TestCase):
    def test_user_created_at(self):
        # Test that created_at is automatically set on user creation
        user = User(first_name="John", last_name="Doe", email="john@example.com", password=None)
        self.assertIsInstance(user.created_at, datetime.datetime)

    def test_user_updated_at(self):
        # Test that updated_at is automatically set on user update
        user = User(first_name="John", last_name="Doe", email="john@example.com", password=None)
        original_updated_at = user.updated_at

        # Introduce a slight delay before performing the update operation
        time.sleep(1)  # Delay for 1 second

        # Perform an update
        user.update_name("John Smith")

        self.assertNotEqual(user.updated_at, user.created_at)
        self.assertIsInstance(user.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
