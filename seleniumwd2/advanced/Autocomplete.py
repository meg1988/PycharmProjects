from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Autocomplete():
    def test(self):

        driver = webdriver.Firefox()
        baseurl = "https://www.southwest.com/"
        driver.maximize_window()
        driver.get(baseurl)

        driver.implicitly_wait(5)

        depart_city = driver.find_element(By.ID , 'air-city-departure')
        depart_city.send_keys("New York")

        sleep(3)

        window = driver.find_element(By.XPATH, "//ul[@id='air-city-departure-menu']//li[contains(text(),'NJ - EWR')]")
        window.click()

        sleep(3)

        height = driver.execute_script("return window.innerHeight")
        width = driver.execute_script("return window.innerWidth")

        print ("height is " + str(height))
        print ("width is " + str(width))



        driver.quit()

ff = Autocomplete()
ff.test()