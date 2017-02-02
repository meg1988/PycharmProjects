import unittest
from tests.home.login_tests import LoginTests
from tests.courses.course_tests_csv_file import CourseTestCSV

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CourseTestCSV)

smoketest = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smoketest)