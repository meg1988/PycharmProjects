from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class WorkingWithJavaScript():
    def test(self):

        driver = webdriver.Firefox()
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        #driver.maximize_window()


        #driver.get(baseurl)

        driver.execute_script("window.location = 'https://letskodeit.teachable.com/pages/practice';")

        driver.implicitly_wait(3)
        sleep(10)

        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("test")

        sleep(3)

        driver.quit()

ff = WorkingWithJavaScript()
ff.test()