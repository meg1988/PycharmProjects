from selenium import webdriver
import time

class BrowserInteractions():
    def info(self):

        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()

        driver.maximize_window();
        print("opening the browser")

        driver.get(baseurl)
        print("opening the url")

        title = driver.title
        print("The title of the page is " + str(title))

        current_url = driver.current_url;
        print("the current url is " + str(current_url))

        driver.refresh()
        print("window refereshed first time")

        driver.get(driver.current_url)
        print("window refereshed using current url")

        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        print("new url open")

        time.sleep(5)

        current_url = driver.current_url;
        print("the current url is " + str(current_url))

        title = driver.title
        print("The title of the page is " + str(title))

        driver.back()
        print("getting back to previous page")

        time.sleep(5)

        current_url = driver.current_url;
        print("the current url is " + str(current_url))

        title = driver.title
        print("The title of the page is " + str(title))

        driver.forward()
        print("getting forward to next page")

        time.sleep(5)

        current_url = driver.current_url;
        print("the current url is " + str(current_url))

        title = driver.title
        print("The title of the page is " + str(title))


        #pagesource = driver.page_source
        #print("page source is " + str(pagesource))

        driver.quit()

ff = BrowserInteractions()
ff.info()





