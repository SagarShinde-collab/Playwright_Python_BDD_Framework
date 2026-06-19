import allure

from config import Config

from pages.login_page_1 import LoginPage
from pages.dashboard_page_2 import DashboardPage
from pages.cart_page_3 import CartPage
from pages.oder_page_4 import OrderPage
from pages.order_history_page_5 import OrdersHistoryPage


def user_on_login_page(page):
    with allure.step("Given User is on login page"):
        pass


def login(page):
    with allure.step("When User logs into application"):
        login_page = LoginPage(page)
        login_page.set_username(Config.email)
        login_page.set_password(Config.pass_word)
        login_page.click_login()


def add_product(page):
    with allure.step("And User adds product to cart"):
        dashboard = DashboardPage(page)
        dashboard.search_product_add_to_cart()
        dashboard.click_cart()


def checkout(page):
    with allure.step("And User proceeds to checkout"):
        cart_page = CartPage(page)
        cart_page.open_cart()
        cart_page.click_checkout()


def place_order(page, order_context):
    with allure.step("And User places the order"):
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
        order_context["generated_order_id"] = generated_order_id

        allure.attach(
            generated_order_id,
            "Generated Order ID",
            allure.attachment_type.TEXT
        )


def verify_order(page, order_context):
    generated_order_id = order_context["generated_order_id"]
    with allure.step("Verify Order ID exists in order history"):
        history_page = OrdersHistoryPage(page)
        history_page.order_id_link()

        actual_order_id = history_page.get_order_id_from_history(generated_order_id)

        allure.attach(
            generated_order_id,
            name="Expected Order ID",
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            actual_order_id,
            "Actual Order ID",
            allure.attachment_type.TEXT
        )

        assert actual_order_id == generated_order_id


@allure.epic("E-Commerce")
@allure.feature("Order Management")
@allure.story("End to End Workflow")
@allure.title("Verify Complete End To End Workflow")
def test_complete_order_workflow(page, order_context):
    """
    Plain pytest test that executes the end-to-end flow by calling the
    same helper functions that were in `step_definations/test_oder_workflow_steps.py`.
    This file intentionally does NOT use pytest-bdd decorators or scenario.
    """
    user_on_login_page(page)
    login(page)
    add_product(page)
    checkout(page)
    place_order(page, order_context)
    verify_order(page, order_context)