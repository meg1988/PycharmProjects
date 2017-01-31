from selenium import webdriver
import os

class RunChromeTests(object):

    def info(self):
        driverLocation = "/Users/megharastogi/PycharmProjects/SeleniumProject/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        print("opening given url")
        driver.get("http://www.gmail.com")

runtest = RunChromeTests()
runtest.info()