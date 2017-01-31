import unittest
from unittestpackage.test_case_demo import TestCaseDemo
from unittestpackage.test_case_demo2 import TestCaseDemo2

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)

smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
    