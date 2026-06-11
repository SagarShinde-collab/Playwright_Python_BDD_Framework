from pages.login_page_1 import LoginPage
from pages.dashboard_page_2 import DashboardPage
from pages.cart_page_3 import CartPage
from config import Config
from playwright.sync_api import Page
from playwright.sync_api import expect

def test_cart_page(logged_in_user):
    # Cart Page
    cart_page = CartPage(logged_in_user)
    cart_page.open_cart()
    cart_page.order_id()
    cart_page.click_checkout()

