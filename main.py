import requests as req
from urllib.parse import urljoin


with open("api.txt", "r") as api_key:
    API_KEY = api_key.read()

params = {"access_token": API_KEY,
          "v": 5.199
        }
param = {"url": "https://api.vk.ru/method/utils.getServerTime",
         "access_token": API_KEY,
         "v": 5.199}

shorter_url = req.get("https://api.vk.ru/method/utils.getShortLink", params=param).text
response = req.get(shorter_url, params=params)

print(response.text)#.get("response").get("short_url"))

