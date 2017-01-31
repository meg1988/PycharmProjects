from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class RadioCheckbox():
    def isEnabled(self):

        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)

        driver.implicitly_wait(5)

        bmwradio = driver.find_element(By.XPATH,'//input[@id="bmwradio"]')
        benzradio = driver.find_element(By.XPATH,'//input[@id="benzradio"]')
        bmwcheck = driver.find_element(By.XPATH, '//input[@id="bmwcheck"]')
        benzcheck = driver.find_element(By.XPATH, '//input[@id="benzcheck"]')
        hondacheck = driver.find_element(By.XPATH, '//input[@id="hondacheck"]')

        bmwradio.click()

        print("the id of the element is " + str(bmwradio.get_attribute("id")))

        sleep(3)

        benzradio.click()

        print("bmw radio button is selected "+ str(bmwradio.is_selected()))
        print("benz radio button is selected "+ str(benzradio.is_selected()))

        sleep(3)

        bmwcheck.click()
        sleep(3)

        benzcheck.click()
        sleep(3)

        hondacheck.click()
        sleep(3)

        driver.quit()


ff = RadioCheckbox()
ff.isEnabled()