from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus
from selenium.webdriver import ActionChains
from time import sleep

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def objectSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order = 2)
    def test_validLogin(self):

        self.lp.login('test@email.com','abcabc')

        result1 = self.lp.verifyLoginTitle()
        if result1:
            resultMessage1 = 'Title is Correct'
        else:
            resultMessage1 = 'Title is Incorrect'
        self.ts.mark("test_validLogin",result1, resultMessage1)
        result2 = self.lp.verifyLoginSuccessful()
        if result2:
            resultMessage2 = 'Login Successful'
        else:
            resultMessage2 = 'Login Failed'
        self.ts.markFinal("test_validLogin", result2, resultMessage2)


    @pytest.mark.run(order = 1)
    def test_invalidLogin(self):

        self.lp.logout()

        """
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(self.driver.find_element_by_xpath(".//*[@id='navbar']//span[text()='User Settings']")).click().perform()
            sleep(3)

            print("Mouse over on element")
        except:
            print("Mouse over failed on element")

        #sleep(3)
        #self.driver.find_element_by_xpath(".//*[@id='navbar']//span[text()='User Settings']").click()
        #sleep(3)
        self.driver.find_element_by_xpath(".//div[@id='navbar']//a[@href='/sign_out']").click()
        sleep(3)
        """

        self.lp.login(password='abcabcabc')

        result = self.lp.verifyLoginFailed()
        assert result == True

