from playwright.sync_api import Page


class AdminPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_admin_page(self):
        # Click on the "Admin" tab in the menu
        self.page.click('a[href="/web/index.php/admin/viewAdminModule"]')

    def search_user(self, username: str):
        # Enter the username in the search bar and search
        self.page.fill('input[class="oxd-input oxd-input--active"]', username)
        self.page.click('button[type="submit"]')  # Click the search button

    def verify_user_in_results(self, username: str) -> bool:
        # Check if the searched user appears in the result list
        return self.page.is_visible(f'text="{username}"')

    def click_add_button(self):
        # Click on the "Add" button to add a new user
        self.page.click('button[class="oxd-button oxd-button--medium oxd-button--secondary"]')

    def add_user(self, role, emp_name, user_name, status, password):
        # Add user details in the form and save
        self.page.click('i[class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]')  # Select dropdown
        self.page.select_option('select[name="userType"]', value=role)  # Select role from dropdown
        self.page.fill('input[placeholder="Employee Name"]', emp_name)  # Enter employee name
        self.page.fill('input[placeholder="Username"]', user_name)  # Enter username
        self.page.select_option('select[name="status"]', status)  # Select status
        self.page.fill('input[name="password"]', password)  # Enter password
        self.page.fill('input[name="confirmPassword"]', password)  # Confirm password
        self.page.click('button[type="submit"]')  # Click save button

        # Check if the user was added successfully
        return self.page.is_visible(f'text="{user_name}" added successfully')
