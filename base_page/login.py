import pickle
import time
from time import sleep

from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()

class login:

    def __init__(self,driver):
        self.driver=driver

    def enter_phone_number(self,phone_number_location,phone_number_data):
        phone_location=WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,phone_number_location)))
        phone_location.click()
        phone_location.send_keys(phone_number_data)

    def submit_phone_number(self,submit_phone_number_location):
        button = self.driver.find_element(By.XPATH,submit_phone_number_location)
        button.click()

    def enter_otp(self,otp_location,otp_data):
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,"//span[@class='text-primary fw-bold ml-2 cursor-pointer']")))
        location = self.driver.find_element(By.XPATH,otp_location)
        location.send_keys(otp_data)

    def submit_otp(self,otp_submit_button_location):
        button = self.driver.find_element(By.XPATH,otp_submit_button_location)
        button.click()
        sleep(3)

    def get_cookie(self):
        with open("configs/cookie.pkl","wb") as file:
            pickle.dump(self.driver.get_cookies(), file)
