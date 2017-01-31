from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from waittypes.explicitwaittypes import ExplicitWaitTypes

class ExplicitWaitDemo():
    def info(self):

        baseurl = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(1)

        sleep(2)

        driver.find_element(By.ID,'tab-flight-tab').click()
        sleep(2)
        driver.find_element(By.ID, 'flight-origin').click()
        driver.find_element(By.ID, 'flight-origin').send_keys("San Francisco, CA (SFO-San Francisco Intl.)")
        sleep(2)
        driver.find_element(By.ID, 'flight-destination').click()
        driver.find_element(By.ID, 'flight-destination').send_keys("New York, NY (NYC-All Airports)")
        sleep(2)
        driver.find_element(By.ID, 'flight-departing').click()
        driver.find_element(By.ID, 'flight-departing').send_keys("01/27/2017")
        sleep(2)
        flightreturn = driver.find_element(By.ID, 'flight-returning')
        flightreturn.click()
        flightreturn.clear()
        flightreturn.send_keys("01/30/2017")
        sleep(2)
        driver.find_element(By.ID, "search-button").click()

        sleep(2)

        driver.find_element(By.ID, 'tab-flight-tab').click()
        sleep(2)
        driver.find_element(By.ID, 'flight-origin').click()
        driver.find_element(By.ID, 'flight-origin').send_keys("San Francisco, CA (SFO-San Francisco Intl.)")
        sleep(2)
        driver.find_element(By.ID, 'flight-destination').click()
        driver.find_element(By.ID, 'flight-destination').send_keys("New York, NY (NYC-All Airports)")
        sleep(2)
        driver.find_element(By.ID, 'flight-departing').click()
        driver.find_element(By.ID, 'flight-departing').send_keys("01/27/2017")
        sleep(2)
        flightreturn = driver.find_element(By.ID, 'flight-returning')
        flightreturn.click()
        flightreturn.clear()
        flightreturn.send_keys("01/30/2017")
        sleep(2)
        driver.find_element(By.ID, "search-button").click()

        ew = ExplicitWaitTypes(driver)
        element = ew.waitForElement("stopFilter_stops-0",'id',15,1)
        element.click()

        sleep(2)
        driver.quit()

ff = ExplicitWaitDemo()
ff.info()





