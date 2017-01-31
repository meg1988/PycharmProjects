from selenium import webdriver

class FindPrice():
    def findprice(self):

        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseurl)

        # price = driver.find_element_by_xpath("//table[@id='product']//tr//td[text()='Python Programming Language']//following-sibling::td")
        price = driver.find_element_by_xpath("//table[@id='product']//td[text()='Python Programming Language']//following-sibling::td")

        print("price of value is " + str(price.text))

ff = FindPrice()
ff.findprice()