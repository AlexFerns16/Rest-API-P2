import requests

# headers
headers = {'Authorization': 'Bearer 8cff8bcf77689b631a895e0324f7abb4dbd37fd0'}

# django localhost:8000/api/
# endpoint = "http://127.0.0.1:8000/api/products/create/"

# token authentication is applied to this endpoint here
endpoint = "http://127.0.0.1:8000/api/products/list_create/"

# HTTP request
data = {
    "title": "This field is done test",
    "price": 49.97
}
get_response = requests.post(endpoint, json=data, headers=headers)

# gives the response in python dictionary format
print(get_response.json())

# gives the status code
print(get_response.status_code)
