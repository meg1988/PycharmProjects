from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    def screenShot(self,testcaseName, resultMessage):

        fileName = testcaseName + "_" + resultMessage + "." + str(round(time.time()) * 1000) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory,relativeFileName)
        destinationDirectory = os.path.join(currentDirectory,screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory : " + destinationFile)
        except:
            self.log.error("### Exception Occurred !!!")
            print_stack()



    def getTitle(self):
        return self.driver.title

    def getByType(self,locatorType):
        locatorType = locatorType.lower()

        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css_selector':
            return By.CSS_SELECTOR
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'tag':
            return By.TAG_NAME
        elif locatorType == 'link':
            return By.LINK_TEXT
        elif locatorType == 'partial':
            return By.PARTIAL_LINK_TEXT
        else :
            self.log.info("Locator type " + locatorType + " is not supported")
        return False

    def getElement(self, locator, locatorType = "id"):
        element = None

        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator : " + locator + " with locator type : " + locatorType)

        except:
            self.log.info("Element not found with locator : " + locator + " with locator type : " + locatorType)
        return element

    def getElementList(self, locator, locatorType = "id"):
        element = None

        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator : " + locator + " with locator type : " + locatorType)

        except:
            self.log.info("Element list not found with locator : " + locator + " with locator type : " + locatorType)
        return element

    def elementClick(self, locator='' , locatorType="id", element = None):
        try:
            if locator:
                element = self.getElement(locator,locatorType)
            element.click()
            self.log.info("Clicked on element with locator : " + locator + " with locator type : " + locatorType)
        except:
            self.log.error("Cannot click on the element with locator : " + locator + " with locator type : " + locatorType)
            print_stack()

    def sendKeys(self, data, locator='' , locatorType="id", element = None):
        try:
            if locator:
                element = self.getElement(locator,locatorType)
            element.clear()
            element.send_keys(data)
            self.log.info("Sent data '"+ data +"' on element with locator : " + locator + " with locator type : " + locatorType)
        except:
            self.log.info("Cannot send data '"+ data +"' on the element with locator : " + locator + " with locator type : " + locatorType)
            print_stack()

    def getText(self, data, locator='' , locatorType="id", element = None, info=''):

        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator,locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("the text is :: '" + text +"'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator='', locatorType='id', element = None):

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element found with locator : " + locator + " with locator type : " + locatorType)
                return True
            else:
                self.log.info("Element not found with locator : " + locator + " with locator type : " + locatorType)
                return False

        except:
            self.log.info("Element not found with locator : " + locator + " with locator type : " + locatorType)
            return False

    def isElementDisplayed(self, locator='', locatorType='id', element = None):

        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator : " + locator + " with locator type : " + locatorType)
            else:
                self.log.info("Element is not displayed with locator : " + locator + " with locator type : " + locatorType)

            return isDisplayed

        except:
            self.log.info("Element is not displayed with locator : " + locator + " with locator type : " + locatorType)
            return False

    def elementPresenceCheck(self,locator,locatorType):

        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elementList = self.driver.find_elements(byType, locator)

            if len(elementList) > 0:
                return True
            else:
                return False

        except:
            self.log.info("Element not found with locator : " + locator + " with locator type : " + locatorType)
            return False



    def waitForElement(self, locator, locatorType = "id", timeout = 10 , pollFrequency = 0.5):
        element=None
        try:

            self.log.info("Waiting for maximum : : " + str(timeout) + ":: seconds for elements to be clickable")

            wait = WebDriverWait(self.driver, timeout=timeout , poll_frequency=pollFrequency, ignored_exceptions=[TimeoutException,NoSuchElementException,ElementNotSelectableException,ElementNotVisibleException])

            byType = self.getByType(locatorType)
            element = wait.until(EC.element_to_be_clickable((byType,locator)))

            self.log.info("Elements appeared on the webpage")
        except:
            self.log.info("Elements did not appear on the page")
            print_stack()
        return element

    def webScroll(self, direction="up"):

        if direction =='up':
            self.driver.execute_script('window.scrollBy(0,-1000)')
        if direction =='down':
            self.driver.execute_script('window.scrollBy(0,1000)')


    def selectDropdown(self, data, locator='', locatorType='id', element = None):
        sel = Select(self.getElement(locator,locatorType))
        sel.select_by_visible_text(data)
