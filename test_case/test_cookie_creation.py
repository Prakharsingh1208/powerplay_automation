import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.ReadConfig import login
from utilities.log_generator import loggen

base_url=login.get_base_url()
@pytest.fixture
def setup_login(setup):
    setup.get()
    yield setup
    return setup

def test_login_to_get_cookie(setup_login):
    browser =
