from config.config import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_add_user(browser):
    page = browser.new_page()
    
    # Log in first
    login_page = LoginPage(page)
    login_page.navigate("https://opensource-demo.orangehrmlive.com")
    login_page.login(USERNAME, PASSWORD)
    
    # Now add user
    dashboard = DashboardPage(page)
    assert dashboard.add_user(role='1', emp_name='John Smith', user_name='john.smith', status='1', password='Qwerty@123')
    
    page.close()
