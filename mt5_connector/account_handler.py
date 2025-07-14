import MetaTrader5 as mt5
import logging

class AccountHandler:
    def __init__(self):
        pass

    def get_account_info(self):
        info = mt5.account_info()
        if info:
            return {
                "balance": info.balance,
                "equity": info.equity,
                "margin": info.margin,
                "free_margin": info.margin_free,
                "leverage": info.leverage,
                "login": info.login,
                "currency": info.currency,
            }
        else:
            logging.error("Failed to retrieve account info")
            return {}

    def is_market_open(self, symbol):
        symbol_info = mt5.symbol_info(symbol)
        if symbol_info is None:
            logging.warning(f"Symbol not found: {symbol}")
            return False
        return symbol_info.visible and mt5.market_book_add(symbol)
