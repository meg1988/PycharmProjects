from selenium.webdriver.common.by import By

class HandyWrappers():

    def __init__(self,driver):
        self.driver = driver

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
        elif locatorType == 'class_name':
            return By.CLASS_NAME
        elif locatorType == 'tag_name':
            return By.TAG_NAME
        elif locatorType == 'link_text':
            return By.LINK_TEXT
        elif locatorType == 'partial_link_text':
            return By.PARTIAL_LINK_TEXT
        else :
            print("Locator type is not supported")
        return False

    def getElement(self, locator, locatorType = "id"):
        element = None

        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element found")

        except:
            print("Element not found")
        return element

    def isElementPresent(self, locator, locatorType):

        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.getElement(locator, locatorType)

            if element is not None:
                return True
            else:
                return False

        except:
            print("Element not found")
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
            print("Element not found")
            return False







