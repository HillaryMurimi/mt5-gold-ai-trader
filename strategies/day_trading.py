import numpy as np

class DayTradingStrategy:
    def __init__(self, symbol):
        self.symbol = symbol

    def generate_signals(self, data):
        """
        Example: RSI-based mean reversion strategy
        """
        delta = data['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        data['RSI'] = 100 - (100 / (1 + rs))

        signals = []
        for rsi in data['RSI']:
            if rsi < 30:
                signals.append('buy')
            elif rsi > 70:
                signals.append('sell')
            else:
                signals.append('hold')

        data['signal'] = signals
        return data[['close', 'RSI', 'signal']]
