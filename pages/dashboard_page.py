from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = 'input[placeholder="Search"]'
        self.search_button = 'button[type="submit"]'
        self.add_button = 'button:has-text("Add")'

    def search_user(self, username):
        self.page.fill(self.search_input, username)
        self.page.click(self.search_button)

    def verify_search_result(self, username):
        return username in self.page.locator('.oxd-table').text_content()

    def add_user(self, role, emp_name, user_name, status, password):
        self.page.click(self.add_button)
        self.page.select_option('select[name="systemUser[userType]"]', role)
        self.page.fill('input[name="systemUser[employeeName][empName]"]', emp_name)
        self.page.fill('input[name="systemUser[userName]"]', user_name)
        self.page.select_option('select[name="systemUser[status]"]', status)
        self.page.fill('input[name="systemUser[password]"]', password)
        self.page.fill('input[name="systemUser[confirmPassword]"]', password)
        self.page.click('button[type="submit"]')
        return self.page.locator('.oxd-text--success').is_visible()
