from pages.order_history_page_5 import OrdersHistoryPage
from pages.oder_page_4 import OrderPage
from config import Config
from tests import test_order

def test_order_page_history(order_ids):

    page = order_ids["page"]
    expected_order_id = order_ids["order_id"]

    history_page = OrdersHistoryPage(page)
    history_page.order_id_link()
    actual_order_id = history_page.get_order_id_from_history(expected_order_id)

    assert actual_order_id == expected_order_id