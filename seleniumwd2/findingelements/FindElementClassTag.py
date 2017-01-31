from selenium import webdriver

class FindElementClassTag():
    def info(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseurl)

        elementbyclass = driver.find_element_by_class_name("displayed-class")
        elementbyclass.send_keys("Testing the element")

        if elementbyclass is not None:
            print("found element by class name")

        elementbytag = driver.find_element_by_tag_name("h1")
        text = elementbytag.text

        if elementbytag is not None:
            print("found element by tag name and the text is : " + text)

ff = FindElementClassTag()
ff.info()