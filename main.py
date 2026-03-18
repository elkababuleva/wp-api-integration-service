import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response.status_code)