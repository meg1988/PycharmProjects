from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ClickType():
    def info(self):
        baseurl='https://letskodeit.teachable.com/'
        driver = webdriver.Firefox()
        driver.get(baseurl)

        driver.implicitly_wait(10)

        login_link = driver.find_element(By.XPATH, '//div[@id="navbar"]//a[@href = "/sign_in"]')

        login_link.send_keys("hello")
        login_link.click()

        time.sleep(5)

        email_field = driver.find_element(By.ID, 'user_email')
        password_field = driver.find_element(By.ID, 'user_password')

        email_field.send_keys("test@gmail.com")
        password_field.send_keys("test")


        time.sleep(3)

        email_field.clear()
        password_field.clear()

        time.sleep(3)

        email_field.send_keys("test1@gmail.com")
        password_field.send_keys("test1")

        time.sleep(3)

        driver.quit()

ff = ClickType()
ff.info()





