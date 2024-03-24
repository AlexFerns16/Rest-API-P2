import requests

# prints raw text response > source code
# HTTP request > HTML
endpoint1 = "https://httpbin.org/"

# prints object data
# RestAPI HTTP request > json
endpoint2 = "https://httpbin.org/anything"

# django localhost:8000/
endpoint3 = "http://127.0.0.1:8000/"

# django localhost:8000/api/
endpoint4 = "http://127.0.0.1:8000/api/"

# HTTP request
get_response = requests.get(
    endpoint4, 
    # params={'abc':123},
    json={"product_id": 123}
)

# gives the headers
# print(get_response.headers)

# gives the response in javascript object format
# print(get_response.text)

# gives the response in python dictionary format
print(get_response.json())

# accessing the 'key' of the python 'dictionary'
# print(get_response.json()['message'])

# gives the status code
print(get_response.status_code)
