from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class SwitchToWindow():
    def test(self):

        driver = webdriver.Firefox()
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(5)

        parent_handle = driver.current_window_handle

        print("parent handle : " + parent_handle)

        driver.find_element(By.ID , "openwindow").click()

        sleep(5)

        handles = driver.window_handles
        print("handles :")
        for handle in handles:
            print(handle)
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                print("switched to new window with handle" + handle)
                searchbox = driver.find_element(By.ID, "search-courses")
                searchbox.send_keys("python")

                sleep(3)
                driver.close()
                break

        driver.switch_to.window(parent_handle)
        driver.find_element(By.ID, "name").send_keys("Test")

        sleep(3)

        driver.quit()

ff = SwitchToWindow()
ff.test()