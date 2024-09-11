from config.config import USERNAME, PASSWORD
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

def test_user_search(browser):
    page = browser.new_page()
    
    # Log in first
    login_page = LoginPage(page)
    login_page.navigate("https://opensource-demo.orangehrmlive.com")
    login_page.login(USERNAME, PASSWORD)

    # Now perform search
    dashboard = DashboardPage(page)
    dashboard.search_user("Bhuvaneshwar")
    assert dashboard.verify_search_result("Bhuvaneshwar")
    
    page.close()
