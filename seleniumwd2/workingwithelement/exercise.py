from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class Exercise():
    def info(self):

        baseurl = "https://www.airbnb.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)

        driver.implicitly_wait(10)

        destination =driver.find_element(By.ID, 'search-location')
        destination.send_keys("Las Vegas, NV, United States")

        sleep(3)

        startdate = driver.find_element(By.ID, 'startDate')
        startdate.send_keys("01/27/2017")

        sleep(3)

        enddate = driver.find_element(By.ID, 'endDate')
        enddate.send_keys("01/30/2017")

        sleep(3)

        guest = driver.find_element(By.XPATH,'//div[@class = "GuestPickerTrigger"]//button[@class = "GuestPickerTrigger__button"]')
        guest.click()

        sleep(3)

        inc = driver.find_element(By.XPATH,'//div[@class="increment-btn"]//button[@class="btn btn-increment"]')
        inc.click()

        sleep(3)

        search = driver.find_element(By.XPATH,'//div[@class="SearchForm__submit"]//button[@class="btn btn-primary btn-large btn-block"]')
        search.click()

        sleep(3)

        print("current url is " + str(driver.current_url))

        driver.quit()

ff = Exercise()
ff.info()