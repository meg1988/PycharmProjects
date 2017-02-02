from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    _my_courses = "My Courses"
    _all_courses = "All Courses"
    _practice = "Practice"
    _user_setting_icon = ".//div[@id='navbar']//li[@class='dropdown']"


    def navigateToAllCourses(self):
        self.webScroll("up")
        self.elementClick(self._all_courses, "link")
        self.util.sleep(3, "Waiting for page")

    def navigateToMyCourses(self):
        self.webScroll("up")
        self.elementClick(self._my_courses, "link")
        self.util.sleep(3, "Waiting for page")

    def navigateToPractice(self):
        self.webScroll("up")
        self.elementClick(self._practice, "link")
        self.util.sleep(3, "Waiting for page")

    def navigateToUserSettings(self):
        element = self.waitForElement(locator = self._user_setting_icon, locatorType="xpath")
        self.elementClick(element = element)
