import unittest
from src.user import User


class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("Favour")
        self.assertEqual(user.name, "Favour")
        self.assertEqual(len(user.cart.items), 0)


if __name__ == "__main__":
    unittest.main()