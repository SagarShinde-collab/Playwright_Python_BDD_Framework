import allure
from playwright.sync_api import Page

class OrdersHistoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.oder_history_page = page.locator("button[routerlink*='myorders']")
        self.order_rows = page.locator("tbody tr")
    @allure.title("Order History Page")
    def order_id_link(self):
        self.oder_history_page.click()
        self.page.wait_for_url("**/dashboard/myorders")
        print("After click URL:", self.page.url)

    @allure.step("Order Id matched with Expected oder Id")
    def get_order_id_from_history(self, order_ids):
        print("Current URL:", self.page.url)
        self.page.wait_for_timeout(1000)

        count = self.order_rows.count()
        print("Row Count:", count)
        print("Expected oder Id:", order_ids)
        for i in range(count):
            row_order_id = self.order_rows.nth(i).locator("th").text_content().strip()
            print(f"Row {i}: {row_order_id}")

            if row_order_id and row_order_id.strip() == order_ids:
                return row_order_id.strip()

        # return None
        return None
