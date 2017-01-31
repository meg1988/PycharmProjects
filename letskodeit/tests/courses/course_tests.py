from pages.courses.register_course_page import RegisterCoursePage
import unittest
import pytest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class CourseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.cp = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order = 1)
    def test_searchValidCourse(self):
        self.cp.searchCourse("JavaScript")

        result = self.cp.verifyCoursePageTitle()
        self.ts.markFinal('searchValidCourse',result,"Title incorrect")

    @pytest.mark.run(order = 2)
    def test_invalidCourseEnrollment(self):
        self.cp.enrollCourse('41111111','01/2020','222')

        result = self.cp.verifyPaymentFailed()
        self.ts.markFinal('invalidCourseEnrollment',result,"Payment failed because of invalid CC number")

