import requests
from config.settings import CRYPTO_API_KEY, ALERT_CURRENCY

API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

def fetch_crypto_prices():
    """
    Fetches the latest prices for the currencies specified in ALERT_CURRENCY.
    """
    headers = {
        "X-CMC_PRO_API_KEY": CRYPTO_API_KEY
    }
    symbols = ",".join(ALERT_CURRENCY)  # Combine currencies into a single string
    try:
        response = requests.get(API_URL, headers=headers, params={"symbol": symbols})
        response.raise_for_status()
        data = response.json()
        return parse_crypto_data(data)
    except Exception as e:
        print(f"Error fetching crypto data: {e}")
        return {}

def parse_crypto_data(data):
    """
    Extracts and returns the prices of the specified currencies.
    """
    crypto_prices = {}
    for symbol in ALERT_CURRENCY:
        try:
            price = data["data"][symbol]["quote"]["USD"]["price"]
            crypto_prices[symbol] = price
        except KeyError:
            print(f"Data for {symbol} not found in API response.")
    return crypto_prices