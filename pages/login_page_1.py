import allure
import playwright.sync_api
from playwright.sync_api import expect,Page

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.user_name=page.locator('#userEmail')
        self.pass_word=page.locator('#userPassword')
        self.login_button = page.locator('#login')
        self.error_msg = page.locator("div[aria-label='Incorrect email or password.']")
    @allure.step("Enter the email)")
    def set_username(self,email):
        self.user_name.fill(email)
    @allure.step("Enter the password")
    def set_password(self,pass_word):
        self.pass_word.fill(pass_word)
    @allure.step("Login to your account")
    def click_login(self):
        self.login_button.click()


    def verify_home_page_title(self):
        expect(self.page).to_have_title("Let's Shop")

    def verify_login_error_message(self):
        expect(self.error_msg).to_contain_text("Incorrect email or password.")