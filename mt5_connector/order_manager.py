import MetaTrader5 as mt5
import logging

class OrderManager:
    def __init__(self, symbol):
        self.symbol = symbol

    def close_position(self, ticket):
        position = mt5.positions_get(ticket=ticket)
        if not position:
            logging.warning(f"No position found for ticket: {ticket}")
            return

        pos = position[0]
        action_type = mt5.ORDER_TYPE_SELL if pos.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY

        close_request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.symbol,
            "volume": pos.volume,
            "type": action_type,
            "position": ticket,
            "price": mt5.symbol_info_tick(self.symbol).ask if action_type == mt5.ORDER_TYPE_BUY else mt5.symbol_info_tick(self.symbol).bid,
            "deviation": 20,
            "magic": 123456,
            "comment": "AI Bot Close",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        result = mt5.order_send(close_request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            logging.error(f"Close order failed: {result.retcode}")
        else:
            logging.info(f"Position closed successfully: {result}")
        return result
