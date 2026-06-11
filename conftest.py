import pytest
from playwright.sync_api import sync_playwright
from config import Config

def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chromium"
    )

    parser.addoption(
        "--env",
        action="store",
        default="qa"
    )

@pytest.fixture
def order_context():
    return {}

@pytest.fixture(scope="function")
def page(request):
    browser_name = request.config.getoption("--browser")
    env = request.config.getoption("--env")

    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=False)

        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=False)

        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=False)

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        page = browser.new_page()

        page.goto(Config.ENVIRONMENTS[env])

        page.wait_for_load_state("networkidle")

        yield page

        browser.close()

