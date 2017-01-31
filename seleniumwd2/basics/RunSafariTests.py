from selenium import webdriver

class RunSafariTests(object):

    def info(self):
        driver = webdriver.Safari()
        print("opening given url")
        driver.get("http://www.gmail.com")

runtest = RunSafariTests()
runtest.info()