import pytest
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_add_user(browser):
    page = browser.new_page()

    # Step 1: Log in
    login_page = LoginPage(page)
    login_page.navigate("https://opensource-demo.orangehrmlive.com")
    login_page.login("Admin", "admin123")

    # Step 2: Navigate to Admin Page
    admin_page = AdminPage(page)
    admin_page.navigate_to_admin_page()

    # Step 3: Search for the user 'Admin'
    admin_page.search_user('Admin')

    # Step 4: Verify if user 'queen1234' exists
    user_exists = admin_page.verify_user_in_results('Admin')
    assert user_exists, "User 'Admin' should exist in search results"

    # Step 5: Click on the 'Add' button
    admin_page.click_add_button()

    # Step 6: Add a new user with details
    admin_page.add_user(
        role='Admin',  # Admin Role
        emp_name='Shashank Rushiya',  # Employee Name
        user_name='shashank.rushiya',  # Username
        status='Enable',  # Enable status
        password='Qwerty@123'  # Password
    )

    # Step 7: Verify the new user was added successfully
    assert admin_page.verify_user_in_results('shashank.rushiya'), "New user was not added successfully"

    page.close()
