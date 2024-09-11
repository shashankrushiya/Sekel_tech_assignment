from api.api_utils import get_users

def test_api():
    response = get_users()
    
    # Validate status code
    assert response.status_code == 200
    
    # Validate JSON structure
    data = response.json()
    for user in data['data']:
        assert 'userName' in user
        assert 'status' in user
        assert 'role' in user
