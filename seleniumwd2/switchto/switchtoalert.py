from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class SwitchToAlert():
    def test(self):

        driver = webdriver.Firefox()
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(5)

        driver.find_element(By.ID , "name").send_keys("Megha")
        sleep(3)
        driver.find_element(By.ID , "alertbtn").click()
        sleep(3)
        driver.switch_to.alert.accept()

        sleep(3)

        driver.find_element(By.ID , "name").send_keys("Megha")
        sleep(3)

        driver.find_element(By.ID , "confirmbtn").click()
        sleep(3)

        driver.switch_to.alert.dismiss()
        sleep(3)

        driver.quit()

ff = SwitchToAlert()
ff.test()
