from selenium import webdriver

class FindElementLinkText():
    def info(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseurl)

        elementbylinktest = driver.find_element_by_link_text("Login")


        if elementbylinktest is not None:
            print("found element by Linked test")

        elementbypartial = driver.find_element_by_partial_link_text("Pract")

        if elementbypartial is not None:
            print("found element by partial Linked test")

ff = FindElementLinkText()
ff.info()