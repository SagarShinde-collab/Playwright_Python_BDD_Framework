from config import Config
#from pages.loginpage import LoginPage
#from pages.dashboardpage import DashboardPage
#from pages.cartpage import CartPage
from pages.order_history_page_5 import OrdersHistoryPage
from pages.oder_page_4 import OrderPage
import time




def test_order_page(logged_in_user):
    #oder Page
    order_page = OrderPage(logged_in_user)
    order_page.load()
    order_page.country_inpt()
    order_page.select_country()
    order_page.select_card_number(Config.credit_card)
    order_page.select_ccv_code(Config.ccv_code)
    order_page.select_name_on_card(Config.name_on_card)
    order_page.select_coupon_code(Config.coupon_code)
    order_page.place_order_ty()
    order_page.get_order_id()
    time.sleep(5)



