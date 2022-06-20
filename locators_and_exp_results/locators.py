
class Locators:

    add_test_product = '//div[18]//div[3]//button[1]'
    card_btn = '//*[@id="root"]/div/header/div/div[3]/a[4]/img'
    test_product_one_kg = '//tbody/tr[1]/td[3]/strong'

    test_product_price ='//tbody/tr[2]/td[3]/strong'
    test_product_img = 'img[class = "product-image"][src="./images/mango.jpg"]'
    proceed_checkout = "div.action-block > button"

    prod_table = ".products-wrapper"
    one_item = "(//p[@class='quantity'])[1]"
    place_order = "div:nth-child(4) > button:nth-child(14)"

    terms_condition = "(//input[@type='checkbox'])[1]"
    proceed = "//button[normalize-space()='Proceed']"
    success_message = "//*[contains(text(), 'Thank you, your order has been placed successfully')]"
