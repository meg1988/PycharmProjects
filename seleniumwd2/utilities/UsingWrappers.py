from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.HandyWrappers import HandyWrappers
from time import sleep

class UsingWrappers():

    def info(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)

        hw1 = HandyWrappers(driver)

        if hw1.isElementPresent('name','id'):
            text1 = hw1.getElement('name')
            text1.send_keys("Hello")

        sleep(3)

        if hw1.elementPresenceCheck("//input[@id='abc']","xpath"):
            text2 = hw1.getElement("//input[@id='abc']","xpath")
            text2.clear()
            sleep(3)
            text2.send_keys("How are you")
            sleep(3)

        driver.quit()


ff = UsingWrappers()
ff.info()
