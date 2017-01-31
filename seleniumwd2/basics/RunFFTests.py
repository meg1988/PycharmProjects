from selenium import webdriver

class RunFFTests(object):

    def info(self):
        driver = webdriver.Firefox()
        print("opening given url")
        driver.get("http://www.gmail.com")

runtest = RunFFTests()
runtest.info()