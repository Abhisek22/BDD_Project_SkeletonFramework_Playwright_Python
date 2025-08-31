import pytest
from pygments.lexer import default


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="To invoke specific browser as per requirement"
                     )


@pytest.fixture(scope="session")
def credentials(request):
    return request.param

@pytest.fixture()
def browserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()