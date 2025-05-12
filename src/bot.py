import time
import telebot
from services.crypto_api import fetch_crypto_prices
from config.settings import TOKEN, CHAT_ID, CHECK_INTERVAL, ALERT_THRESHOLD

bot = telebot.TeleBot(TOKEN)

def send_alerts():
    while True:
        crypto_prices = fetch_crypto_prices()
        for currency, price in crypto_prices.items():
            threshold = ALERT_THRESHOLD.get(currency)
            if threshold and price >= threshold:
                bot.send_message(
                    CHAT_ID,
                    f"🚨 Alert: {currency} price is now ${price:.2f}, exceeding the threshold of ${threshold:.2f}!"
                )
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    send_alerts()