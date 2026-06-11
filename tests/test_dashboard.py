from pages.dashboard_page_2 import DashboardPage

def test_add_product_to_cart(logged_in_user):

    #Dashboard Page
    product_page = DashboardPage(logged_in_user)
    product_page.search_product_add_to_cart()
    product_page.click_cart()





