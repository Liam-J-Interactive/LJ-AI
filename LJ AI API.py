 import requests

url = "https://api.pickaxe.co/v1/studio/product/list"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_TOKEN"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    print(data)
except requests.exceptions.RequestException as error:
    print("Error:", error)