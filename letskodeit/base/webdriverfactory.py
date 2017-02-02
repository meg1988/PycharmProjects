from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser):

        self.browser = browser

    def getWebDriverInstance(self):
        baseUrl = 'https://letskodeit.teachable.com/'

        if self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driverLocation = "/Users/megharastogi/PycharmProjects/SeleniumProject/chromedriver"
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)
            driver.set_window_size(1280,800)
        elif self.browser == "safari":
            serverlocation = "/Users/megharastogi/PycharmProjects/SeleniumProject/selenium-server-standalone-3.0.1.jar"
            os.environ["SELENIUM_SERVER_JAR"] = serverlocation
            driver = webdriver.Safari()
        else:
            driver = webdriver.Firefox()


        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get(baseUrl)

        return driver


