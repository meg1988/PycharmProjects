from pages.courses.register_course_page import RegisterCoursePage
import unittest
import pytest
from utilities.teststatus import TestStatus
from ddt import ddt,data,unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class CourseTestCSV(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.cp = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)

    @data(*getCSVData("../../../testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCvv):
        self.cp.searchCourse(courseName)

        result1 = self.cp.verifyCoursePageTitle(courseName)
        self.ts.mark('invalidCourseEnrollment',result1,"Title incorrect")

        self.cp.enrollCourse(ccNum,ccExp,ccCvv)

        result2 = self.cp.verifyPaymentFailed()
        self.ts.markFinal('invalidCourseEnrollment',result2,"Payment failed because of invalid CC number")

        self.cp.clickOnAllCourses()
