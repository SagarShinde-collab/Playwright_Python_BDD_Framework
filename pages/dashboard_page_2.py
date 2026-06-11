from playwright.sync_api import expect,Page
from time import sleep
import allure

from config import Config

product_needed= Config.product_needed
class DashboardPage:
    def __init__(self, page:Page):
        self.page = page
        self.products=page.locator('.card-body')
        self.cart=page.locator("[routerlink*='cart']")


    @allure.title("Dashboard Page Select the product and add to cart")
    def search_product_add_to_cart(self):
        self.products.first.wait_for()
        count = self.products.count()
        print(f"Total products: {count}")

        for i in range(count):
            product_name = self.products.nth(i).locator("b").text_content()


            if product_name.strip() == product_needed:
                self.products.nth(i).locator("text='Add To Cart'").click()
                break
    @allure.step("Add To Cart")
    def click_cart(self):
        self.cart.click()






