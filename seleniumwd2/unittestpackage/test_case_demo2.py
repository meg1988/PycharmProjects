import unittest
import unittestpackage.test_case_demo

class TestCaseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("#"*30)
        print("This is the setup method at class level. I will run only once before the test case")
        print("#"*30)

    def setUp(self):
        print("This is the setup method. I will run once before every test case")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print('This is tear down method. I will run once after every test case')

    @classmethod
    def tearDownClass(cls):
        print("#" * 30)
        print("This is the teardown method at class level. I will run only once after the test case")
        print("#" * 30)


if __name__ == "__main__":
        unittest.main(verbosity=2)
