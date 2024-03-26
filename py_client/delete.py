import requests

# enter product id
prod_id = input("Enter Product ID: ")
try:
    prod_id = int(prod_id)
except:
    prod_id = None
    print("{}, is not an integer".format(prod_id))

if prod_id:
    # django localhost:8000/api/
    endpoint = "http://127.0.0.1:8000/api/products/delete/{}/".format(prod_id)

    # HTTP request
    get_response = requests.delete(endpoint)

    # gives the response in python dictionary format
    # print(get_response.json())

    # gives the status code
    print(get_response.status_code, get_response.status_code==204)
