from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class RadioCheckboxList():
    def test(self):

        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)

        driver.implicitly_wait(5)

        radio_elements = driver.find_elements(By.XPATH, '//div[@id="radio-btn-example"]//input[@type="radio"]')
        radio_elements[0].click()

        sleep(3)

        radio_elements[1].click()

        sleep(3)

        radio_elements[2].click()

        cb_elements = driver.find_elements(By.XPATH,'//input[contains(@type,"checkbox") and contains(@name,"cars")]')
        cb_elements[0].click()

        sleep(3)

        cb_elements[1].click()

        sleep(3)

        cb_elements[2].click()

        driver.quit()


ff = RadioCheckboxList()
ff.test()