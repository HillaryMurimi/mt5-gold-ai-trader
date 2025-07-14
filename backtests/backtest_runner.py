import pandas as pd
from strategies.scalping import ScalpingStrategy
from strategies.day_trading import DayTradingStrategy
from strategies.swing import SwingTradingStrategy
import matplotlib.pyplot as plt

class BacktestRunner:
    def __init__(self, strategy_type: str, symbol: str, data: pd.DataFrame):
        self.symbol = symbol
        self.data = data
        self.strategy = self._select_strategy(strategy_type)

    def _select_strategy(self, strategy_type):
        if strategy_type == 'scalping':
            return ScalpingStrategy(self.symbol)
        elif strategy_type == 'day_trading':
            return DayTradingStrategy(self.symbol)
        elif strategy_type == 'swing':
            return SwingTradingStrategy(self.symbol)
        else:
            raise ValueError("Invalid strategy type")

    def run(self):
        result = self.strategy.generate_signals(self.data.copy())
        result['returns'] = result['close'].pct_change()
        result['strategy_returns'] = result['returns'] * result['signal'].map({'buy': 1, 'sell': -1, 'hold': 0}).fillna(0)
        result['cumulative'] = (1 + result['strategy_returns']).cumprod()

        self._plot_results(result)
        return result

    def _plot_results(self, result):
        plt.figure(figsize=(12, 6))
        plt.plot(result['cumulative'], label='Strategy Equity Curve')
        plt.title(f"Backtest Equity Curve for {self.symbol}")
        plt.xlabel("Time")
        plt.ylabel("Cumulative Return")
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == '__main__':
    # Example with CSV price data
    df = pd.read_csv("sample_gold_data.csv")  # CSV must have 'close' column and datetime index
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)

    runner = BacktestRunner(strategy_type='swing', symbol='XAUUSD', data=df)
    results = runner.run()
