import unittest
from datetime import datetime
from model.user import User


class TestUser(unittest.TestCase):
    def test_created_at_and_updated_at(self):
        # Create a new user
        user = User(email="test@example.com", first_name="John", last_name="Doe", password=1234)

        # Check if created_at and updated_at are set
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

        # Ensure created_at and updated_at are equal initially
        self.assertAlmostEqual(user.created_at.timestamp(), user.updated_at.timestamp(), delta=0.01)

        # Update user's information
        user.first_name = "Jane"

        # Check if updated_at has been updated
        self.assertNotEqual(user.created_at, user.updated_at)


if __name__ == '__main__':
    unittest.main()
