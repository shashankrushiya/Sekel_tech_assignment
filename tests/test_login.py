import pytest
from config.config import USERNAME, PASSWORD, BASE_URL
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def login_page(browser):
    page = browser.new_page()
    login = LoginPage(page)
    login.navigate(BASE_URL)
    yield login
    page.close()


# @pytest.mark.xfail
def test_user_login(login_page):
    login_page.login(USERNAME, PASSWORD)
    assert login_page.verify_login() == "Mary Briganza"
