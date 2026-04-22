import unittest
from main import add

class testmain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),52)


if __name__ == "__main__":
    unittest.main()