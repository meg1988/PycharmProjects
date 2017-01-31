import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage
import os

@pytest.yield_fixture()
def setUp():
    print("Running method level setup")
    yield
    print("Running method level teardown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, osType):
    print("Running one time setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("test@email.com", "abcabc")
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time teardown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help = "Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
