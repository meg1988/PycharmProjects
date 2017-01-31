from selenium import webdriver
from selenium.webdriver.common.by import By

class FindAllElement():
    def info(self):

        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseurl)

        print("opened the url")

        elementListByClassName = driver.find_elements_by_class_name("inputs")

        if elementListByClassName is not None:
            print("the size of list is len " + str(len(elementListByClassName)))


        elementListByTagName = driver.find_elements(By.TAG_NAME,"h1")

        if elementListByTagName is not None:
            print("the size of list is len " + str(len(elementListByTagName)))

ff = FindAllElement()
ff.info()