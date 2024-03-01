import requests

url = "https://cdn2.thecatapi.com/images/ebv.jpg"

response = requests.get(url)

if response.status_code == 200:

    data = response.json
    print("Data retrieved successfully:", data)
else:
    print("failed retrieval of data. Status code:", response.status_code)