from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.HandyWrappers import HandyWrappers
from time import sleep

class DynamicXpath():

    def info(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(15)

        hw1 = HandyWrappers(driver)

        if hw1.isElementPresent('//div[@id="navbar"]//a[@href = "/sign_in"]','xpath'):
            login = hw1.getElement('//div[@id="navbar"]//a[@href = "/sign_in"]','xpath')
            login.click()

        sleep(3)

        if hw1.elementPresenceCheck("user_email","id"):
            text1 = hw1.getElement("user_email","id")
            text1.send_keys("test@gmail.com")

        sleep(3)

        if hw1.isElementPresent('user_password','id'):
            text2 = hw1.getElement("user_password","id")
            text2.send_keys("abcabc")

        sleep(3)

        if hw1.isElementPresent('commit','name'):
            button = hw1.getElement('commit','name')
            button.click()
        sleep(3)

        if hw1.isElementPresent('search-courses','id'):
            searchbox = hw1 .getElement('search-courses','id')
            searchbox.send_keys('Javascript')
        sleep(3)

        _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        if hw1.isElementPresent(_courseLocator,'xpath'):
            courseElement = hw1 .getElement(_courseLocator,'xpath')
            courseElement.click()

        sleep(3)

        print(str(driver.current_url))
        driver.quit()


ff = DynamicXpath()
ff.info()
