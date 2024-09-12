import requests


class ApiUtils:
    def __init__(self):
        self.base_url = "https://opensource-demo.orangehrmlive.com"
        self.login_endpoint = "/web/index.php/auth/login"
        self.api_endpoint = "/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC"
        self.token = None

    def login_and_get_token(self, username: str, password: str):
        """
        Logs in and retrieves the authentication token from the API.
        """
        login_url = f"{self.base_url}{self.login_endpoint}"
        login_data = {
            "username": username,
            "password": password
        }
        response = requests.post(login_url, json=login_data)

        if response.status_code == 200:
            self.token = response.json().get("token")  # Extract token from the response
            if self.token:
                print("Login successful, token obtained.")
            else:
                raise Exception("Token not found in the response.")
        else:
            raise Exception(f"Login failed with status code: {response.status_code}")

    def get_users(self):
        """
        Fetches the list of users from the API using the authentication token.
        """
        if self.token is None:
            raise Exception("No token found. Please login first.")

        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        api_url = f"{self.base_url}{self.api_endpoint}"

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            print("API request successful")
            return response.json()  # Return the response data
        else:
            raise Exception(f"API request failed with status code: {response.status_code}")
