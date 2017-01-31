import pytest

@pytest.yield_fixture()
def setUp():
    print("Running method level setup")
    yield
    print("Running method level teardown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, osType):
    print("Running one time setup")
    if browser == 'firefox':
        value = 10
        print("Running test on FF")
    else:
        value = 20
        print("Running test on chrome")

    if request.cls is not None:
        request.cls.value = value

    yield value
    print("Running one time teardown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help = "Type of operationg system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
