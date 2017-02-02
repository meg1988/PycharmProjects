from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage
import utilities.custom_logger as cl
from utilities.util import Util
import logging

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(self.driver)
        util = Util()
    #locators

    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"


    def clickLoginLink(self):
        login_link = self.waitForElement(locator=self._login_link,locatorType="link")
        self.elementClick(element=login_link)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, "id")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, "id")

    def clickLoginButton(self):
        self.elementClick(self._login_button,"name")


    def login(self, email = None , password = None):

        self.clickLoginLink()
        if email is not None:
            self.enterEmail(email)
        if password is not None:
            self.enterPassword(password)
        self.clickLoginButton()

    def logout(self):

        self.nav.navigateToUserSettings()
        logout_link = self.waitForElement(locator = ".//div[@id='navbar']//a[@href='/sign_out']",locatorType="xpath")
        self.elementClick(element=logout_link)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(".//div[@id='navbar']//li[@class='dropdown']","xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(".//div[contains(text(),'Invalid email or password')]", "xpath")
        return result

    def verifyLoginTitle(self):
       return self.verifyPageTitle("Let's Kode")




