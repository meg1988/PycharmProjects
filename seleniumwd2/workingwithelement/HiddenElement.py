from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class HiddenElement():
    def practice(self):

        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(5)

        textboxelement = driver.find_element_by_id('displayed-text')

        textboxstate = textboxelement.is_displayed();

        print("is textbox visible " + str(textboxstate))

        sleep(4)

        driver.find_element_by_id("hide-textbox").click()

        textboxstate = textboxelement.is_displayed();

        print("is textbox visible " + str(textboxstate))

        sleep(4)

        driver.find_element_by_id("show-textbox").click()

        textboxstate = textboxelement.is_displayed();

        print("is textbox visible " + str(textboxstate))

        sleep(5)

        driver.quit()

    def expedia(self):
        baseurl = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(5)

        dropboxelement = driver.find_element_by_id('package-1-age-select-1')
        print("dropdown there " + str(dropboxelement.is_displayed()))
        sleep(5)

        driver.quit()



ff = HiddenElement()
ff.practice()
ff.expedia()