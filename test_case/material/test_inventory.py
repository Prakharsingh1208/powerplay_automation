import time
from symbol import yield_expr

import pytest
import allure
from selenium import  webdriver
from selenium.webdriver.common.by import By
from base_page.material.inventory import inventory
from utilities.ReadConfig import inventory_config

url=inventory_config.get_url()
add_material_button_location=inventory_config.get_add_material_button_location()
new_material_button_location=inventory_config.get_new_material_button_location()
input_name_location=inventory_config.get_input_name_location()
uom_input_location=inventory_config.get_uom_input_location()
save_create_new_location=inventory_config.get_save_create_new_location()
add_new_material_cross_button=inventory_config.get_add_new_material_cross_button()
select_material_cross_button=inventory_config.get_select_material_cross_button()
Added_materials_location=inventory_config.get_Added_materials_location()

@pytest.fixture()
def setup_inventory(setup):
    setup.maximize_window()
    setup.get(url)
    yield setup
    return setup

@pytest.mark.unit
@allure.title("Verify should not able to create material with name and UOM blank")
@allure.feature("Material")
def test_creating_material_without_necessary_field(setup_inventory):
    browser=inventory(setup_inventory)
    browser.click_add_material(add_material_button_location)
    browser.click_new_material_button(new_material_button_location)
    browser.enter_material_name(input_name_location)
    browser.select_uom(uom_input_location)
    browser.click_save_create_new(save_create_new_location)
    browser.click_on_cross_button(add_new_material_cross_button)
    browser.click_on_cross_button(select_material_cross_button)
    browser.verify_the_save_create_function('1',Added_materials_location)
