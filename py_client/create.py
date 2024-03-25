import requests

# django localhost:8000/api/
endpoint = "http://127.0.0.1:8000/api/products/"

# HTTP request
data = {
    "title": "This field is done again again",
    "price": 37.99
}
get_response = requests.post(endpoint, json=data)

# gives the response in python dictionary format
print(get_response.json())

# gives the status code
print(get_response.status_code)
