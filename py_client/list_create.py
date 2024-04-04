import requests
from getpass import getpass
from django.http import HttpResponse

# ----------------------------------------------------------------------------------
# django localhost:8000/api/
auth_endpoint = "http://127.0.0.1:8000/api/auth/"

# username and password
username = input('What is your username? ')
password = getpass('What is your password? ')

# HTTP request
auth_response = requests.post(auth_endpoint, json={'username':username, 'password':password})

# gives the response in python dictionary format
print(auth_response.json())

# gives the status code
print(auth_response.status_code)


# ----------------------------------------------------------------------------------
if auth_response.status_code == 200:
    
    token = auth_response.json()['token']
    headers = {
        # 'Authorization': 'Token {}'.format(token)
        'Authorization': 'Bearer {}'.format(token)
    }

    # django localhost:8000/api/
    endpoint = "http://127.0.0.1:8000/api/products/list_create/"

    # HTTP request
    get_response = requests.get(endpoint, headers=headers)

    # gives the response in python dictionary format
    print(get_response.json())

    # gives the status code
    print(get_response.status_code)
