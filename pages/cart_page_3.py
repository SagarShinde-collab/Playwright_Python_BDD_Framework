import allure
from playwright.sync_api import expect,Page

from config import Config


class CartPage:
    def __init__(self, page:Page):
        self.page = page
        #self.add_to_cart_btn_locator=page.locator("//button[contains(text(),' Add To Cart')]").nth(2)
        self.cart_page_link=page.locator("//button[@routerlink='/dashboard/cart']")
        self.order_id_locator=page.locator(".itemNumber")
        self.checkout_btn=page.locator("//button[normalize-space()='Checkout']")


    #def add_to_cart_btn(self):
        #self.add_to_cart_btn_locator.click()

    @allure.title("cart page open")
    def open_cart(self):
        self.cart_page_link.click()
        self.page.wait_for_url("**/dashboard/cart")
    @allure.step("Order id Generated")
    def order_id(self):
        order_id=self.order_id_locator.text_content().strip()
        print(f"ORDER ID: {order_id}")
        return order_id

    @allure.step("Checkout cart page")
    def click_checkout(self):
        self.checkout_btn.click()
