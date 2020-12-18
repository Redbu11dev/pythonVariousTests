import json

from pip._vendor import requests

API_ENDPOINT = "https://jsonplaceholder.typicode.com/"


def get_posts(post_id=None, only_comments=None):
    if post_id:
        print("GET REQUEST BY ID:")
        r = requests.get(url=f"{API_ENDPOINT}posts/{post_id}")
        if only_comments:
            print("GET REQUEST ONLY COMMENTS:")
            r = requests.get(url=f"{API_ENDPOINT}posts/{post_id}/comments")
    else:
        print("GET REQUEST ALL POSTS:")
        r = requests.get(url=f"{API_ENDPOINT}posts")
    print(r)
    print(r.content.decode("utf-8"))


def make_post(json_data=None):
    r = requests.post(url=f"{API_ENDPOINT}posts", json=json_data)
    print("POST REQUEST:")
    print(r)
    print(r.content.decode("utf-8"))
    response = json.loads(r.content.decode("utf-8"))
    new_post_id = response['id']
    print(f"NEW POST ID:\n{new_post_id}")


def update_post(post_id, json_data=None):
    r = requests.put(url=f"{API_ENDPOINT}posts/{post_id}", json=json_data)
    print("PUT REQUEST:")
    print(r)
    print(r.content.decode("utf-8"))


def update_post_partially(post_id, json_data=None):
    r = requests.patch(url=f"{API_ENDPOINT}posts/{post_id}", json=json_data)
    print("PATCH REQUEST:")
    print(r)
    print(r.content.decode("utf-8"))


def delete_post(post_id):
    r = requests.put(url=f"{API_ENDPOINT}posts/{post_id}")
    print("DELETE REQUEST:")
    print(r)
    print(r.content.decode("utf-8"))


get_posts()
get_posts(post_id=1)
get_posts(post_id=1, only_comments=True)

json_str1 = '''{
  "title": "foo",
  "body": "bar",
  "userId": 1
}'''
print(json_str1)
make_post(json.loads(json_str1))

json_str2 = '''{
  "id": 1,
  "title": "foo332",
  "body": "bar4sadsad",
  "userId": 1
}'''
print(json_str2)
update_post(25, json.loads(json_str2))

json_str3 = '''{
  "body": "ayy lmao"
}'''
print(json_str3)
update_post_partially(22, json.loads(json_str3))

delete_post(1)
