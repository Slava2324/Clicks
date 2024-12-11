import requests as req


with open("api.txt", "r") as api_key:
    API_KEY = api_key.read()

params = {"access_token": API_KEY,
          "v": "5.199"}

response = req.get(url="https://api.vk.ru/method/utils.getServerTime", params=params)
response.raise_for_status()
print(response.ok)
print(response.text)

