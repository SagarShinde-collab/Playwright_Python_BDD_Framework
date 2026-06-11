import pytest
from pages.login_page_1 import LoginPage
from config import Config
from playwright.sync_api import Page
from playwright.sync_api import expect


def test_valid_user_login(page:Page):
    login_page = LoginPage(page)
    login_page.set_username(Config.email)
    login_page.set_password(Config.pass_word)
    login_page.click_login()

    login_page.verify_home_page_title()

def test_invalid_user_login(page:Page):
    login_page = LoginPage(page)
    login_page.set_username(Config.invalid_email)
    login_page.set_password(Config.invalid_password)
    login_page.click_login()

    login_page.verify_login_error_message()