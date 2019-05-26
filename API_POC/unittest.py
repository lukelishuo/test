import requests
import unittest
import time
from Tests import jball
class testclassone(unittest.TestCase):
    def setUp(self):
        print(111)
        pass
    def test_1(self):
        jball()
        pass
    def tearDown(self):
        print(333)
        pass


if __name__ == '__main__':
    unittest.main()