from pip._vendor import requests

API_ENDPOINT = "https://jsonplaceholder.typicode.com/"

r = requests.get(API_ENDPOINT+"posts")
print(r)
print(r.content.decode("utf-8"))
