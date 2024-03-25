import requests

# django localhost:8000/api/
endpoint = "http://127.0.0.1:8000/api/products/list_create/"

# HTTP request
get_response = requests.get(endpoint)

# gives the response in python dictionary format
print(get_response.json())

# gives the status code
print(get_response.status_code)
