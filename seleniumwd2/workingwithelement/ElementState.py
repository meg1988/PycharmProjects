from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class ElementState():
    def isEnabled(self):

        baseurl = "https://www.google.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(5)

        search_bar2 = driver.find_element(By.ID,"gs_taif0")
        search_bar1 = driver.find_element(By.ID,"lst-ib")

        print(str(search_bar2.is_enabled()))
        print(str(search_bar1.is_enabled()))

        search_bar1.send_keys("hello world")

        sleep(5)

        driver.quit()



ff = ElementState()
ff.isEnabled()