from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class ScrollingElement():
    def test(self):

        driver = webdriver.Firefox()
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        driver.execute_script("window.scrollBy(0,1000);")
        sleep(3)

        driver.execute_script("window.scrollBy(0,-1000);")
        sleep(3)

        element = driver.find_element_by_id("mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);" , element)
        sleep(3)
        driver.execute_script("window.scrollBy(0,-150);")
        sleep(3)

        driver.execute_script("window.scrollBy(0,-1000);")
        location = element.location_once_scrolled_into_view
        print( "Location : "+ str(location))

        sleep(3)
        driver.quit()

ff = ScrollingElement()
ff.test()