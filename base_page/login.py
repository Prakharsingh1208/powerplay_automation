import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.find_element(By.XPATH,"")

class login:

    def __init__(self,driver):
        self.driver=driver

    def enter_phone_number(self,phone_number_location,phone_number_data):
        phone_location = self.driver.find_element(By.XPATH,phone_number_location)
        phone_location.click()
        phone_location.send_keys(phone_number_data)

    def submit_phone_number(self,submit_phone_number_location):
        button = self.driver.find_element(By.XPATH,submit_phone_number_location)
        button.click()

    def enter_otp(self,otp_location,otp_data):
        location = self.driver.find_element(By.XPATH,otp_location)
        location.send_keys(otp_data)
        time.sleep(3)

    def submit_otp(self,otp_submit_button_location):
        button = self.driver.find_element(By.XPATH,otp_submit_button_location)
        button.click()
        time.sleep(10)