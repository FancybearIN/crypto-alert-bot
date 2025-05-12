from time import sleep
import threading
from services.crypto_api import get_crypto_price
from telegram import Bot
from config.settings import TELEGRAM_BOT_TOKEN, CHAT_ID

class AlertManager:
    def __init__(self, currency, threshold):
        self.currency = currency
        self.threshold = threshold
        self.bot = Bot(token=TELEGRAM_BOT_TOKEN)
        self.alert_sent = False

    def check_price(self):
        while True:
            price = get_crypto_price(self.currency)
            if price is not None:
                if price >= self.threshold and not self.alert_sent:
                    self.send_alert(price)
                    self.alert_sent = True
                elif price < self.threshold:
                    self.alert_sent = False
            sleep(300)  # Check every 5 minutes

    def send_alert(self, price):
        message = f"Alert! The price of {self.currency} has reached {price}."
        self.bot.send_message(chat_id=CHAT_ID, text=message)

    def start(self):
        alert_thread = threading.Thread(target=self.check_price)
        alert_thread.start()