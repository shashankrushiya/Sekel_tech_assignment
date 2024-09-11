import requests

def get_users(limit=50, offset=0):
    url = f"https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit={limit}&offset={offset}&sortField=u.userName&sortOrder=ASC"
    response = requests.get(url)
    return response
