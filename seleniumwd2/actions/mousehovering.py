from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains

class MouseHover():
    def test(self):

        driver = webdriver.Firefox()
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver.maximize_window()
        driver.get(baseurl)

        driver.implicitly_wait(5)
        driver.execute_script("window.scrollBy(0,600);")
        sleep(3)

        element = driver.find_element(By.ID, "mousehover")
        itemToClickLocator = './/div[@class="mouse-hover-content"]//a[text()="Top"]'


        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            sleep(2)
            topLink = driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(topLink).click().perform()
            sleep(3)

            print("Mouse over on element")
        except:
            print("Mouse over failed on element")

        driver.quit()

ff = MouseHover()
ff.test()