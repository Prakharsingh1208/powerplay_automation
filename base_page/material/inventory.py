import time
from time import sleep
from tkinter.tix import Select

import pytest
import allure
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from utilities.log_generator import loggen
from selenium.webdriver.support.ui import Select
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
        self.driver.execute_script("arguments[0].click();", button)
        logs.info("clicked on 'New material' button")

    @allure.step("Entering the material name")
    def enter_material_name(self,material_name_location):
        material_name_input = WebDriverWait(self.driver,5,0.5).until(EC.element_to_be_clickable((By.XPATH,material_name_location)))
        self.driver.execute_script("arguments[0].click();",material_name_input)
        material_name_input.send_keys("Test")
        logs.info("Entered the material name")

    @allure.step("selecting the material UOM")
    def select_uom(self,uom_input_location):
        menu=WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(uom_input_location))
        self.driver.execute_script("arguments[0].click();", menu)
        options=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"(//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters fes-m css-ddvog1'])[2]")))
        sleep(10)
        logs.info("Selected UOM")


    @allure.step("Clicking 'save & create new'")
    def click_save_create_new(self,save_create_new_location):
        button=WebDriverWait(self.driver,3,0.5).until(EC.presence_of_element_located(save_create_new_location))
        button.click()
        logs.info("Clicked on 'save & create'")

    @allure.step("Clicking on cross button")
    def click_on_cross_button(self,cross_button_location):
        button = WebDriverWait(self.driver,3,0.5).until(EC.presence_of_element_located((By.XPATH,cross_button_location)))
        button.click()

    @allure.step("Validation the test case")
    def verify_the_save_create_function(self,test_case_id,Added_materials_location):
        WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(Added_materials_location))
        items=self.driver.find_elements(By.XPATH,Added_materials_location)
        t=0
        for item in items:
            if item.text == 'Test':
                t=1
                assert True
        if t == 0:
            assert False


