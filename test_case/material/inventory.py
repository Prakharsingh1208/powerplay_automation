from symbol import yield_expr

import pytest
import allure
from selenium import  webdriver
from selenium.webdriver.common.by import By
from base_page.material.inventory import inventory
from utilities.ReadConfig import inventory_config


@pytest.fixture()
def setup_inventory(setup):
    setup.maximize_window()
    setup.get(inventory_config.get_url())
    yield setup
    return setup

@allure.title("Verify should not able to create material with name and UOM blank")
@allure.feature("Material")
def test_creating_material_without_necessary_field(setup_inventory):
    browser=inventory(setup_inventory)
    browser.click_add_material()