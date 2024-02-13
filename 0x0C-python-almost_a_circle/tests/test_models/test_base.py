import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""
    def setUp(self):
        """Set up of Base instances"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(11)

    def test_ids(self):
        """Tests if IDs are assigned correctly"""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 11)


if __name__ == '__main__':
    unittest.main()
