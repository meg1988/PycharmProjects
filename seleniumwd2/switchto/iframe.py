from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class SwitchToIFrame():
    def test(self):

        driver = webdriver.Firefox()
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(5)

        driver.execute_script("window.scrollBy(0,1500);")
        sleep(5)

        #driver.switch_to.frame("courses-iframe")
        driver.switch_to.frame(0)

        sleep(5)

        driver.find_element_by_id("search-courses").send_keys("python")
        sleep(5)

        driver.switch_to.default_content()
        sleep(5)

        driver.execute_script("window.scrollBy(0,-1500);")
        sleep(5)
        driver.find_element(By.ID,"name").send_keys("Test1")
        sleep(5)

        driver.switch_to.frame("iframe-name")
        sleep(5)

        driver.find_element_by_id("search-courses").send_keys("python")
        sleep(5)

        driver.switch_to.default_content()
        sleep(5)

        driver.execute_script("window.scrollBy(0,1500);")
        sleep(5)
        driver.find_element(By.ID, "name").send_keys("Test2")
        sleep(5)

        driver.quit()

ff = SwitchToIFrame()
ff.test()

