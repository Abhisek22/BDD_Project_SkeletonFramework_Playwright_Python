import parse
import pytest
from pytest_bdd import given, when, then, parsers, scenarios
from PageObjects.Login_Page import LoginPage
from Utils.API_Utils.apiBase import APIUtils

scenarios('Features/orderTransactionDetails.feature')

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('Through API place the item order with {username} and {password}'))
def placeOrderWithAPI(playwright, username, password, shared_data):
    credentials = {}
    credentials['userEmail'] = username
    credentials['userPassword'] = password
    api_utils = APIUtils()
    orderId = api_utils.create_order(playwright, credentials)
    shared_data['orderId'] = orderId


@when(parsers.parse('I login to portal with {username} and {password}'))
def loginToPortal(playwright, username, password, browserInstance, shared_data):
    loginPage = LoginPage(browserInstance)
    loginPage.navigateToLogin()
    shared_data['login_Page'] = loginPage
    dashboardPage = loginPage.login(username, password)
    shared_data['dashboard_Page'] = dashboardPage

@when('Navigate to orders page')
def navigateToOrderHistoryPage(playwright, shared_data):
    dashboard_page = shared_data['dashboard_Page']
    orderhistory_page = dashboard_page.goToOrderHistory()
    shared_data['orderhistory_Page'] = orderhistory_page

@when('Select the orderId')
def selectOrderID(playwright, shared_data):
    orderhistory_page = shared_data['orderhistory_Page']
    orderId = shared_data['orderId']
    orderdetails_page = orderhistory_page.getOrderDetails(orderId)
    shared_data['orderdetails_Page'] = orderdetails_page

@then('Order message is successfully displayed')
def orderMessageVerification(playwright, shared_data):
    orderdetails_page = shared_data['orderdetails_Page']
    orderdetails_page.verifySuccessOrderMessage()