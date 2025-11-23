import pandas as pd

try:
    import talib
    TA_AVAILABLE = True
except:
    TA_AVAILABLE = False


def sma(df: pd.DataFrame, period: int = 20):
    if TA_AVAILABLE:
        df[f"SMA_{period}"] = talib.SMA(df['close'], timeperiod=period)
    else:
        df[f"SMA_{period}"] = df['close'].rolling(period).mean()
    return df


def rsi(df: pd.DataFrame, period: int = 14):
    if TA_AVAILABLE:
        df[f"RSI_{period}"] = talib.RSI(df['close'], timeperiod=period)
    else:
        delta = df['close'].diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        avg_gain = gain.rolling(period).mean()
        avg_loss = loss.rolling(period).mean()
        rs = avg_gain / avg_loss
        df[f"RSI_{period}"] = 100 - (100 / (1 + rs))
    return df


def macd(df: pd.DataFrame):
    if TA_AVAILABLE:
        macd_line, signal, hist = talib.MACD(df['close'])
    else:
        fast = df['close'].ewm(span=12, adjust=False).mean()
        slow = df['close'].ewm(span=26, adjust=False).mean()
        macd_line = fast - slow
        signal = macd_line.ewm(span=9, adjust=False).mean()
        hist = macd_line - signal

    df["MACD"] = macd_line
    df["MACD_signal"] = signal
    df["MACD_hist"] = hist
    return df
