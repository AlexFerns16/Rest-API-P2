import requests

# prints raw text response > source code
# HTTP request > HTML
endpoint1 = "https://httpbin.org/"

# prints object data
# RestAPI HTTP request > json
endpoint2 = "https://httpbin.org/anything"

# django localhost 8000
endpoint3 = "http://127.0.0.1:8000/"

# HTTP request
get_response = requests.get(endpoint3, json={"query":"Hello World"})   
print(get_response.text)    
# print(get_response.json())
print(get_response.status_code)
