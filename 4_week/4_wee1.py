import unittest

class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_1(self):
        self.assertEqual(1,0,None)

if __name__ == "__main__":
    unittest.main(verbosity=4)