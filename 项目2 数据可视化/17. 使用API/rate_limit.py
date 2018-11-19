import requests

url = "https://api.github.com/rate_limit"
rep = requests.get(url)
print("Request code", rep.status_code)

response_dicts = rep.json()

print('response_dicts: ', response_dicts)