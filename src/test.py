import requests

API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
API_KEY = "59de5d93-a373-4c55-8269-adecef07ea68"
headers = {"X-CMC_PRO_API_KEY": API_KEY}
params = {"symbol": "XRP,PI"}

response = requests.get(API_URL, headers=headers, params=params)
print(response.status_code, response.json())