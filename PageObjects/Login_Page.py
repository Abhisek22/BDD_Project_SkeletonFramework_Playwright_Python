from .Dashboard_Page import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigateToLogin(self):
        self.page.goto("https://rahulshettyacademy.com/client")


    def login(self, userEmail, userPassword):
        self.page.locator("#userEmail").fill(userEmail)
        self.page.locator("#userPassword").fill(userPassword)
        self.page.get_by_role("button", name="Login").click()
        dashboard_page = DashboardPage(self.page)
        return dashboard_page