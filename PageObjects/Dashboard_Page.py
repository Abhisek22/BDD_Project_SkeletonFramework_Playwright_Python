from .OrderHistory_Page import OrderHistoryPage


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def goToOrderHistory(self):
        self.page.get_by_role("button", name="Orders").click()
        orderhistory_page = OrderHistoryPage(self.page)
        return orderhistory_page