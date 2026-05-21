import requests

url = "https://api.github.com/users/octocat"

response = requests.get(url)

print(response.json())
