import pytest
import allure
from selenium import  webdriver
from selenium.webdriver.common.by import By
from utilities.log_generator import loggen
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
logs = loggen.create_log()

class inventory:
    def __init__(self,driver):
        self.driver=driver
    @allure.step("Clicking on 'Add material' button")
    def click_add_material(self,add_material_button_location):
        button = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,add_material_button_location)))
        button.click()
        logs.info("Clicked on 'Add material' button")

    @allure.step("Clicking on 'New material' button")
    def click_new_material_button(self,new_material_button_location):
        button = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,new_material_button_location)))
        button.click()
        logs.info("clicked on 'New material' button")

    @allure.step("Entering the material name")
    def enter_material_name(self,material_name_location):
        material_name_input = WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,material_name_location)))
        material_name_input.click()
        material_name_input.send_keys()