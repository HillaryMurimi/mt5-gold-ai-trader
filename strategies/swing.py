import numpy as np

class SwingTradingStrategy:
    def __init__(self, symbol):
        self.symbol = symbol

    def generate_signals(self, data):
        """
        Example: MACD cross strategy
        """
        data['EMA12'] = data['close'].ewm(span=12, adjust=False).mean()
        data['EMA26'] = data['close'].ewm(span=26, adjust=False).mean()
        data['MACD'] = data['EMA12'] - data['EMA26']
        data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()

        signals = []
        for i in range(1, len(data)):
            if data['MACD'][i] > data['Signal_Line'][i] and data['MACD'][i-1] <= data['Signal_Line'][i-1]:
                signals.append('buy')
            elif data['MACD'][i] < data['Signal_Line'][i] and data['MACD'][i-1] >= data['Signal_Line'][i-1]:
                signals.append('sell')
            else:
                signals.append('hold')

        signals.insert(0, 'hold')
        data['signal'] = signals
        return data[['close', 'MACD', 'Signal_Line', 'signal']]
