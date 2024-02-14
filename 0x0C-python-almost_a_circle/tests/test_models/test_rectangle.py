import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_ids(self):
        """Test cases for ids of Rectangle instances"""
        r1 = Rectangle(2, 3)
        r2 = Rectangle(2, 4, 5)
        r3 = Rectangle(4, 5, 7, 8, 34)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r2.id, 6)
        self.assertEqual(r3.id, 34)

    def test_values(self):
        """Test cases for attribute values"""
        r1 = Rectangle(2, 3)
        r2 = Rectangle(2, 4, 5)
        r3 = Rectangle(4, 5, 7, 8, 34)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r3.height, 5)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.x, 7)

    def test_errors(self):
        """Test of errors raised"""
        r2 = Rectangle(2, 4, 5)
        r3 = Rectangle(4, 5, 7, 8, 34)
        with self.assertRaises(TypeError):
            er = Rectangle()
            er2 = Rectangle(10, "2")
            r2.x = {}
        with self.assertRaises(ValueError):
            r2.width = -10
            r3.y = -2


if __name__ == '__main__':
    unittest.main()
