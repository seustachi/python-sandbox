import requests
import json

response = requests.get("https://api.github.com/users/octocat")

print(response.status_code) # print the status code
print(response.json()) # print the response in json format

# print(response.headers) # print the headers
# print(response.url) # print the url
# print(response.encoding) # print the encoding
# print(response.cookies) # print the cookies


try:
    response = requests.get("https://api.github.com/users/octocataaaaaaa")
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")

print(response.json())






