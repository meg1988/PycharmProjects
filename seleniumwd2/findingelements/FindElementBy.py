from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElementBy():

    def info(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseurl)
        elementbyID = driver.find_element(By.ID,"name")

        if elementbyID is not None:
            print("Found element by ID : " + str(elementbyID.send_keys("testing by ID")))

        elementbyxpath = driver.find_element(By.XPATH,'//*[@id="block-1069048"]/div/div/div/h1')

        if elementbyxpath is not None:
            print("Found element by XPath : " + elementbyxpath.text)

        elementbyname = driver.find_element(By.NAME, "enter-name")

        if elementbyname is not None:
            print("Found element by name : " + str(elementbyname.send_keys("testing by name")))

        elementbycss = driver.find_element(By.CSS_SELECTOR, "#opentab")

        if elementbycss is not None:
            print("Found element by cc selector : " + elementbycss.text)

        elementbyclass = driver.find_element(By.CLASS_NAME, "displayed-class")

        if elementbyclass is not None:
            print("Found element by class : " + str(elementbyclass.send_keys("testing with class")))

        elementbytag = driver.find_element(By.TAG_NAME, "h1")

        if elementbytag is not None:
            print("Found element by tag : " + elementbytag.text)

        elementbylink = driver.find_element(By.LINK_TEXT, "Login")

        if elementbylink is not None:
            print("Found element by link : " + elementbylink.text)

        elementbypartiallink = driver.find_element(By.PARTIAL_LINK_TEXT, "Pract")

        if elementbypartiallink is not None:
            print("Found element by partial link : " + elementbypartiallink.text)

ff = FindElementBy()
ff.info()








