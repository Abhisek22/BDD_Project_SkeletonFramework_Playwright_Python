from .OrderDetails_Page import OrderDetailsPage


class OrderHistoryPage:

    def __init__(self, page):
        self.page = page

    def  getOrderDetails(self, orderId):
        self.page.locator("tr").filter(has_text=orderId).get_by_role("button", name="View").click()
        orderdetails_page = OrderDetailsPage(self.page)
        return orderdetails_page



