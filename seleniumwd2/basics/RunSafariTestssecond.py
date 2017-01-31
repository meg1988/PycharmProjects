from selenium import webdriver
import os

class RunSafariTestsSecond(object):

    def info(self):

        serverlocation = "/Users/megharastogi/PycharmProjects/SeleniumProject/selenium-server-standalone-3.0.1.jar"
        os.environ["SELENIUM_SERVER_JAR"] = serverlocation
        driver = webdriver.Safari(quiet=False)
        print("opening given url")
        driver.get("http://www.gmail.com")

runtest = RunSafariTestsSecond()
runtest.info()