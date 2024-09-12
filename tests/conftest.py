import pytest
from playwright.sync_api import sync_playwright
import os


# Ensure the screenshots folder exists
def ensure_screenshots_dir():
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")


@pytest.fixture(scope="session")
def browser():
    ensure_screenshots_dir()  # Create screenshots folder if it doesn't exist
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch browser
        yield browser
        browser.close()  # Close browser after tests are done


# Capture a screenshot if a test fails
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_make_report(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:  # Only take a screenshot if the test failed
        page = item.funcargs.get('page')  # Get the Playwright page object
        if page:
            screenshot_name = f"screenshots/{item.name}.png"  # Define screenshot path
            page.screenshot(path=screenshot_name)  # Take screenshot
            print(f"Screenshot saved: {screenshot_name}")
