# Crypto Alert Bot

This project is a Telegram bot that provides real-time alerts for cryptocurrency prices, specifically for currencies like XRP and PI. The bot checks the prices every 5 minutes and sends updates to users based on predefined conditions.

## Project Structure

```
crypto-alert-bot
├── src
│   ├── bot.py                # Main entry point for the Telegram bot
│   ├── services
│   │   ├── crypto_api.py     # Functions to interact with cryptocurrency APIs
│   │   └── alert_manager.py   # Manages alert logic and price checking
│   └── config
│       └── settings.py       # Configuration settings for the bot
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/crypto-alert-bot.git
   cd crypto-alert-bot
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure the bot:**
   Edit the `src/config/settings.py` file to include your Telegram bot token and any necessary API keys.

4. **Run the bot:**
   Execute the following command to start the bot:
   ```
   python src/bot.py
   ```

## Usage

- Once the bot is running, you can interact with it through Telegram.
- The bot will send alerts every 5 minutes based on the price conditions set in the `src/services/alert_manager.py` file.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the bot.

## License

This project is licensed under the MIT License. See the LICENSE file for details.