from selenium import webdriver
import os

class FindElement(object):

    def findelementbyname(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseurl)
        elementbyid = driver.find_element_by_id("name")

        if elementbyid is not None :
            print("found the element by id hurray")

        elementbyname = driver.find_element_by_name("show-hide")

        if elementbyname is not None :
            print("found the element by name hurray")
 

ff = FindElement()
ff.findelementbyname()

