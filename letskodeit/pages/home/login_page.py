from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.elementClick(self._login_link,"link")

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

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(".//*[@id='navbar']//span[text()='User Settings']","xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(".//div[contains(text(),'Invalid email or password')]", "xpath")
        return result

    def verifyLoginTitle(self):
       return self.verifyPageTitle("Google")




