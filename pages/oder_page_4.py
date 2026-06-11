import allure
from playwright.sync_api import expect,Page
from config import Config




class OrderPage:
    def __init__(self, page:Page):
        self.page = page
        self.card_number=page.locator("(//input[@type='text'])[1]")
        self.country_input = page.locator("input[placeholder='Select Country']")
        self.country_options=page.locator(".ta-results button")
        self.ccv_option=page.locator("(//input[@class='input txt'])[1]")
        self.name_card=page.locator("(//input[@class='input txt'])['text'][2]")
        self.cou_code=page.locator("(//input[@name='coupon'])")
        self.apply_coupn=page.locator("//button[normalize-space()='Apply Coupon']")
        self.place_order_btn=page.locator("//a[@class='btnn action__submit ng-star-inserted']")
        self.order_id_create=page.locator("label[class='ng-star-inserted']")


    @allure.title("Order page Open")
    def load(self):
        self.page.wait_for_url("**/dashboard/order?*")
    @allure.step("Select Country")
    def country_inpt(self):
        self.country_input.press_sequentially("Ind")

    def select_country(self):
        self.page.wait_for_selector(".ta-results")
        count = self.country_options.count()
        for i in range(count):
            option = self.country_options.nth(i)
            text = option.text_content().strip()
            print(text)
            if text.endswith("India"):
                option.click()
                break
    @allure.step("select credit card")
    def select_card_number(self,credit_card):
        self.card_number.fill(credit_card)
    @allure.step("select ccv code")
    def select_ccv_code(self,ccv_code):
        self.ccv_option.fill(ccv_code)

    @allure.step("Select the name on Card")
    def select_name_on_card(self,name_on_card):
        self.name_card.fill(name_on_card)
    @allure.step("Select coupon code")
    def select_coupon_code(self,coupon_code):
        self.cou_code.fill(coupon_code)
        self.page.locator("body").click()
        self.apply_coupn.click()

    def place_order_ty(self):
        self.place_order_btn.click()

    def get_order_id(self):
        order_ids = self.order_id_create.text_content()
        order_ids = order_ids.replace("|", "").strip()
        print("Generated Order ID:", order_ids)
        return order_ids



