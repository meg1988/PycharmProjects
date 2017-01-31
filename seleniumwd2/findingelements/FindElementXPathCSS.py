from selenium import webdriver

class FindElementXPathCSS():
    def info(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseurl)

        elementbyxpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementbyxpath is not None:
            print("found element by Xpath")

        elementbycss = driver.find_element_by_css_selector("#displayed-text")

        if elementbycss is not None:
            print("found element by CSS selector")

ff = FindElementXPathCSS()
ff.info()