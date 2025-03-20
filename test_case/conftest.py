from email.policy import default

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Choose one from chrome, firefox and edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser=='chrome':
        driver = webdriver.Chrome()
    elif browser=='firefox':
        driver = webdriver.Firefox()
    elif browser=='edge':
        driver = webdriver.Edge()
    else:
        raise AssertionError("Please provide the correct browser flag")

    yield driver
    driver.quit()
    return driver
