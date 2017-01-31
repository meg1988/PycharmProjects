from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshot():
    def info(self):
        baseurl = 'https://letskodeit.teachable.com/'
        driver = webdriver.Firefox()
        driver.get(baseurl)

        driver.implicitly_wait(10)

        login_link = driver.find_element(By.XPATH, '//div[@id="navbar"]//a[@href = "/sign_in"]')
        login_link.click()

        time.sleep(5)

        email_field = driver.find_element(By.ID, 'user_email')
        password_field = driver.find_element(By.ID, 'user_password')

        email_field.send_keys("abc@gmail.com")
        password_field.send_keys("abc")
        driver.find_element_by_name("commit").click()

        time.sleep(3)

        self.takeScreenshot(driver)

        driver.quit()

    def takeScreenshot(self , driver):

        filename = str(round(time.time()) * 1000) + ".png"
        screenshotDirectory = "/Users/megharastogi/Desktop/"
        destinationFile = screenshotDirectory + filename

        try:
            driver.save_screenshot(destinationFile)
            print("screenshot saved to directory   --->> " + destinationFile)
        except NotADirectoryError:
            print("Not a directory")



ff = Screenshot()
ff.info()