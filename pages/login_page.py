from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = 'input[name="username"]'
        self.password_input = 'input[name="password"]'
        self.login_button = 'button[type="submit"]'

    def navigate(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def verify_login(self):
        return self.page.locator('span.oxd-userdropdown-name').text_content()
