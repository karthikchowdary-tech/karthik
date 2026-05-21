import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python API",
    "body": "Learning POST request",
    "userId": 1
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Created Data:")
print(response.json())