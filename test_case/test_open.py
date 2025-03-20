import time

import pytest
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_page.login import login
from utilities.ReadConfig import login_config
from utilities.log_generator import loggen

base_url=login_config.get_base_url()
phone_number_location=login_config.get_phone_number_location()
phone_number_data=login_config.get_phone_number_data()
otp_location=login_config.get_otp_location()
otp_data=login_config.get_otp_data()
submit_phone_number_location=login_config.get_submit_phone_number_location()
otp_submit_button_location=login_config.get_otp_submit_button_location()

@pytest.fixture
def setup_login2(setup):
    setup.get("https://portal.getpowerplay.in/projects")
    with open("configs/cookie.pkl","rb") as file:
        cookies = pickle.load(file)
    for cookie in cookies:
        setup.add_cookie(cookie)
    yield setup
    return setup

def test_login_to_get_cookie(setup_login2):
    browser = login(setup_login2)
    time.sleep(100)