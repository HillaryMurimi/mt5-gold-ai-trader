import os
from dotenv import load_dotenv

load_dotenv()

# News API
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_QUERY = os.getenv("NEWS_QUERY", "Gold")
NEWS_LANGUAGE = os.getenv("NEWS_LANGUAGE", "en")

# MT5 Credentials
MT5_LOGIN = os.getenv("MT5_LOGIN")
MT5_PASSWORD = os.getenv("MT5_PASSWORD")
MT5_SERVER = os.getenv("MT5_SERVER")

# Risk Settings
MAX_RISK_PERCENT = float(os.getenv("MAX_RISK_PERCENT", 2))  # default: 2%

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
