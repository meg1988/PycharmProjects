import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not true")
        b = False
        self.assertFalse(b, "b is not false")

    def test_assertEqual(self):
        a = "test"
        b = "test"
        self.assertNotEqual(a,b,"a is equal to b")

if __name__== '__main_':
    unittest.main(verbosity=2)

