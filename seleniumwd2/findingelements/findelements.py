from selenium import webdriver
import os

class FindElement(object):

    def findelementbyname(self):
        driverlocation = "/Users/megharastogi/PycharmProjects/SeleniumProject/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.get("https://letskodeit.teachable.com/pages/practice")

ff = FindElement()
ff.findelementbyname()

