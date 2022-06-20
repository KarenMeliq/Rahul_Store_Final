import pytest
from selenium.webdriver.common.by import By
from get_elements.web_elements import WebElements
from browser import RahulShettyAcademy
from locators_and_exp_results.exp_results import Exp_results
from locators_and_exp_results.locators import Locators


@pytest.mark.usefixtures('open_browser')
class Test_rahul_shetty_academy(RahulShettyAcademy,Exp_results):

    def test_rahul_store(self):
        result = WebElements.get_title_url(self)
        assert self.expected_title_url == result


        test_product_quantity_price = WebElements.add_test_product(self)
        assert  test_product_quantity_price == Exp_results.expected_quantity_price

        result_test_product_in_cart = WebElements.is_mango_in_cart(self)
        assert self.expected_test_prod_on_overlay in result_test_product_in_cart

        result_proceed_checkout = WebElements.proceed_checkout(self)
        assert result_proceed_checkout.is_displayed()

        result_proceed_checkout_one_item = WebElements.proceed_checkout_one_item(self)
        assert self.one_test_product in result_proceed_checkout_one_item

        WebElements.place_order(self)
        assert self.driver.find_element(By.XPATH, Locators.terms_condition).is_selected()

        result = WebElements.proceed_to_success_page(self)
        assert self.success_text in result



