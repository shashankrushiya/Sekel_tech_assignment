import pytest
from api.api_utils import ApiUtils


@pytest.fixture(scope="function")
def api_utils():
    """
    Pytest fixture to provide an instance of the ApiUtils class.
    """
    return ApiUtils()


def test_api_token_auth(api_utils):
    """
    Test case to verify the API token-based authentication and user data retrieval.
    """
    # Step 1: Login and retrieve the token
    api_utils.login_and_get_token(username="Admin", password="admin123")

    # Step 2: Make the API request to get users
    users_data = api_utils.get_users()

    # Step 3: Assert that the data is as expected
    assert users_data, "No user data received"
    print(users_data)
