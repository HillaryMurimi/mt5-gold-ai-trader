import pandas as pd

def moving_average(data: pd.Series, window: int) -> pd.Series:
    return data.rolling(window=window).mean()

def exponential_moving_average(data: pd.Series, span: int) -> pd.Series:
    return data.ewm(span=span, adjust=False).mean()

def rsi(data: pd.Series, window: int = 14) -> pd.Series:
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def macd(data: pd.Series, span_short: int = 12, span_long: int = 26, signal_span: int = 9):
    ema_short = exponential_moving_average(data, span_short)
    ema_long = exponential_moving_average(data, span_long)
    macd_line = ema_short - ema_long
    signal_line = exponential_moving_average(macd_line, signal_span)
    return macd_line, signal_line
