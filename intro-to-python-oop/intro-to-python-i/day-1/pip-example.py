# import doesn't work without pip
# import requests
from requests import get

url = "https://icanhazdadjoke.com/"

res = get(url, headers={"Accept": "application/json"})

res = res.json()

print(res['joke'])
