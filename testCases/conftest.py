from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome("/Users/daominyang/Documents/chromedriver 3")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        # This is default browser
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):
    """
    This function will et the value from CLI /hooks
    :param parser:
    :return:
    """
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    """
    This will return the Browser value to setup method
    :param request:
    :return:
    """
    return request.config.getoption("--browser")

##### PyTest HTML Report ###########

def pytest_configure(config):
    """
    It is a hook for Adding Environment info to HTML Report
    In order to gen HTML report, one need to add --htmp=Reports/report.html
    in the pytest command line.
    pytest -s -v -n=2 --html=Reports/report.html testCases/test_login.py --browser chrome
    :param config:
    :return:
    """
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Tester'


@pytest.mark.optionslhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)