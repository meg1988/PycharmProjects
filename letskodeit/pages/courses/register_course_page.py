from base.basepage import BasePage
import utilities.custom_logger as cl
from utilities.util import Util
import logging

class RegisterCoursePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _search_field = "search-courses"
    _course = ".//div[@class='course-listing']//div[contains(text(),'JavaScript for beginners')]"
    _enroll_button = "enroll-button-top"
    _card_field="cc_field"
    _expiration_field="cc-exp"
    _cvv_field="cc_cvc"
    _country_select_field="country-select-inside"
    _pay_cc_button = "verify_cc_btn"
    _error_message =".//div[@id='checkout_form_errors']/div[@class='payment-errors invalid_number']"

    def enterCourseName(self, courseName):
        self.sendKeys(courseName, self._search_field ,"id")

    def selectCourse(self):
        self.elementClick(self._course,"xpath")

    def clickEnroll(self):
        self.elementClick(self._enroll_button,"id")

    def enterCCNum(self, ccNum):
        self.sendKeys(ccNum, self._card_field ,"id")

    def enterExpirationDate(self,expDate):
        self.sendKeys(expDate, self._expiration_field ,"id")

    def enterCVV(self,cvv):
        self.sendKeys(cvv,self._cvv_field,"id")

    def selectCountry(self, country):
        self.selectDropdown(country,self._country_select_field,'id')

    def clickOnPay(self):
        self.elementClick(self._pay_cc_button,"id")

    def searchCourse(self, courseName):
        self.enterCourseName(courseName)
        self.selectCourse()
        util = Util()
        util.sleep(3,"Waiting for page")

    def enrollCourse(self, card, expDate, cvv, country = "United States"):
        self.clickEnroll()
        self.enterCCNum(card)
        self.enterExpirationDate(expDate)
        self.enterCVV(cvv)
        self.selectCountry(country)
        self.clickOnPay()

    def verifyCoursePageTitle(self):
        return self.verifyPageTitle("Javascript")

    def verifyPaymentFailed(self):
        return  self.isElementPresent(self._error_message,"xpath")

