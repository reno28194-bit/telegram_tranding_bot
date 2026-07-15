import os
from dotenv import load_dotenv

load_dotenv()

# Bot Configuration
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# API Configuration
COINGECKO_API = "https://api.coingecko.com/api/v3"
TIMEOUT = 10

# Trading Configuration
CRYPTO_UPDATE_INTERVAL = 3600  # 1 hour in seconds
MAX_TRACKED_COINS = 10

# Price thresholds for alerts
PRICE_ALERT_THRESHOLD = 5  # Notify if price changes 5%

# Supported coins (you can add more)
POPULAR_COINS = [
    "bitcoin",
    "ethereum",
    "binancecoin",
    "solana",
    "cardano",
    "ripple",
    "dogecoin",
    "polkadot",
    "avalanche-2",
    "chainlink"
]
