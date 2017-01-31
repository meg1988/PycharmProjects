from traceback import print_stack
from utilities.HandyWrappers import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitTypes():

    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers(self.driver)


    def waitForElement(self, locator, locatorType = "id", timeout = 10 , pollFrequency = 0.5):
        element=None
        try:

            print("Waiting for maximum : : " + str(timeout) + ":: seconds for elements to be clickable")

            wait = WebDriverWait(self.driver, timeout=timeout , poll_frequency=pollFrequency, ignored_exceptions=[TimeoutException,NoSuchElementException,ElementNotSelectableException,ElementNotVisibleException])

            byType = self.hw.getByType(locatorType)
            element = wait.until(EC.element_to_be_clickable((byType,locator)))

            print("Elements appeared on the webpage")
        except:
            print("Elements did not appear on the page")
            print_stack()
        return element

