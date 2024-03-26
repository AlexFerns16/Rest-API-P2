import requests

# django localhost:8000/api/
endpoint = "http://127.0.0.1:8000/api/products/update/1/"

# HTTP request
data = {
    "title": "Hello World, My Old Friend!",
    "price": 129.99
}
get_response = requests.put(endpoint, json=data)

# gives the response in python dictionary format
print(get_response.json())

# gives the status code
print(get_response.status_code)
