from requests import *


with open("api.txt", "r") as api_key:
    API_KEY = api_key.read()

print(API_KEY)

