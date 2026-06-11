import pytest
from playwright.sync_api import sync_playwright
import allure
from conftest import *
from config import Config
from pages.login_page_1 import LoginPage
from pages.dashboard_page_2 import DashboardPage
from pages.cart_page_3 import CartPage
from pages.oder_page_4 import OrderPage
from pages.order_history_page_5 import OrdersHistoryPage
from playwright.sync_api import Page
@allure.title("Verify Complete End to End Order Workflow")
def test_complete_wf_end_2_end(page):
    #login page
    login_page = LoginPage(page)
    login_page.set_username(Config.email)
    login_page.set_password(Config.pass_word)
    login_page.click_login()

    #dashboard page
    dashboard = DashboardPage(page)
    dashboard.search_product_add_to_cart()
    dashboard.click_cart()

    #cart Page
    cart_page = CartPage(page)
    cart_page.open_cart()
    cart_page.click_checkout()

    #order page
    order_page = OrderPage(page)
    order_page.load()
    order_page.country_inpt()
    order_page.select_country()
    order_page.select_card_number(Config.credit_card)
    order_page.select_ccv_code(Config.ccv_code)
    order_page.select_name_on_card(Config.name_on_card)
    order_page.select_coupon_code(Config.coupon_code)
    order_page.place_order_ty()
    generated_order_id = order_page.get_order_id()
    allure.attach(
        generated_order_id,
        name="Generated Order ID",
        attachment_type=allure.attachment_type.TEXT
    )

    #orderhistory page
    history_page = OrdersHistoryPage(page)
    history_page.order_id_link()
    actual_order_id = history_page.get_order_id_from_history(generated_order_id)
    allure.attach(
        actual_order_id,
        name="Actual Order ID",
        attachment_type=allure.attachment_type.TEXT
    )

    assert actual_order_id == generated_order_id



