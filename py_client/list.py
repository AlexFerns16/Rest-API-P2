import requests

# django localhost:8000/api/
endpoint = "http://127.0.0.1:8000/api/products/list/"

# endpoint for search
# search_endpoint = "http://localhost:8000/api/search/?q=hello&public=1&tag=movies"

# HTTP request
get_response = requests.get(endpoint)

# HTTP request for search
# get_response = requests.get(search_endpoint)

# gives the response in python dictionary format
print(get_response.json())

# gives the status code
print(get_response.status_code)
