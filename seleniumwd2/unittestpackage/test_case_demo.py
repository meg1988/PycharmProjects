import unittest

class TestCaseDemo(unittest.TestCase):

    def setUp(self):
        print("This is the setup method. I will run once before every test case")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print('This is tear down method. I will run once after every test case')

if __name__ == "__main__":
        unittest.main(verbosity=2)
