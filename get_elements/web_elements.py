import re

import pytest
from selenium.webdriver.common.by import By

from browser import RahulShettyAcademy
from locators_and_exp_results.locators import Locators

@pytest.mark.usefixtures('open_browser')
class WebElements(RahulShettyAcademy):

    def __init__(self, driver):
        self.driver = driver

    def get_title_url(self):
        driver = self.driver
        rahull_title = driver.title
        rahull_url = driver.current_url
        return rahull_title, rahull_url


    def add_test_product(self):
        self.driver.find_element(By.XPATH, Locators.add_test_product).click()
        test_product_quantity = self.driver.find_element(By.XPATH, Locators.test_product_one_kg).text
        test_product_str = self.driver.find_element(By.XPATH, Locators.test_product_price).text
        return test_product_quantity, test_product_str


    def is_mango_in_cart(self):
        self.driver.find_element(By.XPATH, Locators.card_btn).click()
        test_product_shown = self.driver.find_element(By.CSS_SELECTOR, Locators.test_product_img).get_attribute("src")
        return test_product_shown


    def proceed_checkout(self):
        driver = self.driver
        self.driver.find_element(By.CSS_SELECTOR, Locators.proceed_checkout).click()
        cart_page = driver.find_element(By.CSS_SELECTOR, Locators.prod_table)
        return cart_page

    def proceed_checkout_one_item(self):
        driver = self.driver
        item_test_product= driver.find_element(By.XPATH, Locators.one_item).text
        return item_test_product

    def place_order(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.place_order).click()
        self.driver.find_element(By.XPATH, Locators.terms_condition).click()

    def proceed_to_success_page(self):
        self.driver.find_element(By.XPATH, Locators.proceed).click()
        succ_message = self.driver.find_element(By.XPATH, Locators.success_message).text
        return succ_message

