from selenium import webdriver

class FindAuthor():
    def findauthor(self):

        baseurl = "https://dhtmlx.com/docs/products/dhtmlxGrid/"
        driver = webdriver.Firefox()
        driver.get(baseurl)

        #author = driver.find_element_by_xpath("//td[text()='Mayra Heidenreich']//following-sibling::td[2]")
        #price = driver.find_element_by_xpath("//td[text()='Python Programming Language']//following-sibling::td")

        #author = driver.find_element_by_xpath('//*[@id="cgrid2_1483744415510"]/div[2]/table/tbody/tr[6]/td[3]')
        author = driver.find_element_by_css_selector('#cgrid2_1483744415510 > div.objbox > table > tbody > tr.ev_material.rowselected > td:nth-child(3)')

        print("author of Green mile is " + str(author.text))

ff = FindAuthor()
ff.findauthor()