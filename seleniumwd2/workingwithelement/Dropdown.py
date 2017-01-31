from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class Dropdown():
    def test(self):

        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)

        driver.implicitly_wait(5)

        element = driver.find_element(By.ID,'carselect')
        sel = Select(element)

        print("select benz by value")
        sel.select_by_value("benz")
        sleep(3)

        print("select honda by index")
        sel.select_by_index(2)

        sleep(3)

        print("select bmw by text value")
        sel.select_by_visible_text("BMW")

        sleep(3)

        print("select benz by index")
        sel.select_by_index("2")

        sleep(3)

        driver.quit()


ff = Dropdown()
ff.test()