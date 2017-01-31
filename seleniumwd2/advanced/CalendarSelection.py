from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class CalendarSelection():
    def test1(self):

        baseurl = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        driver.find_element(By.ID, 'tab-flight-tab').click()
        sleep(2)

        driver.find_element(By.ID, 'flight-departing').click()
        date_to_select = driver.find_element(By.XPATH, '//div[@class="datepicker-cal-month"][position()=1]//button[text()="31"]')

        date_to_select.click()

        sleep(2)
        flightreturn = driver.find_element(By.ID, 'flight-returning')
        flightreturn.click()
        flightreturn.clear()
        driver.find_element(By.XPATH, '//div[@class="datepicker-cal-month"][position()=2]//button[text()="1"]').click()

        sleep(3)
        driver.quit()

    def test2(self):

        baseurl = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        driver.find_element(By.ID, 'tab-flight-tab').click()
        sleep(2)

        driver.find_element(By.ID, 'flight-departing').click()
        callMonth = driver.find_element(By.XPATH, '//div[@class="datepicker-cal-month"][position()=1]')
        dates = callMonth.find_elements(By.TAG_NAME,'button')

        for date in dates:
            if date.is_enabled() and date.text == '31':
                date.click()
                break

        sleep(2)
        driver.quit()



ff = CalendarSelection()
ff.test2()