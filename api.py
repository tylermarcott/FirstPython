import requests
import json

""" ex of post curl """

""" url = 'https://api.sitewatch.cloud/v1/customer'
payload =  json.dumps(
     {
    "Customer": {
        "Id": 2100100077,
        "FirstName": "Abe",
        "LastName": "Zeroh",
        "MI": "L",
        "Address1": "1234 Fake St.",
        "City": "Springfield",
        "State": "Oh",
        "Zip": 44322
        }
    }
)
headers = {
    'x-api-key: {{api-key}}'
    'Host: api.sitewatch.cloud'
    'Content-Type: application/json'
}

response = requests.request("GET") """











""" GET /items request, sitewatch  """


url ='https://api.sitewatch.cloud/v1/items'
headers = {
    'x-api-key: {{api-key}}'
    'Host: api.sitewatch.cloud'
    'Content-Type: application/json'
}

response = requests.request("GET", url, headers=headers)

print(response.text)