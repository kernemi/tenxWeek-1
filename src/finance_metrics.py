# src/finance_metrics.py
import pandas as pd
import numpy as np
import talib
from pynance import Stock

# Compute daily returns
def compute_daily_returns(df, close_col='Close'):
    df['daily_return'] = df[close_col].pct_change()
    return df

# Compute SMA, RSI, MACD
def compute_technical_indicators(df, close_col='Close'):
    df['SMA_20'] = talib.SMA(df[close_col], timeperiod=20)
    df['RSI_14'] = talib.RSI(df[close_col], timeperiod=14)
    df['MACD'], df['MACD_signal'], _ = talib.MACD(df[close_col])
    return df

# Compute PyNance risk metrics
def compute_risk_metrics(ticker, start, end):
    stock = Stock(ticker, start=start, end=end)
    df = stock.history()
    df['daily_return'] = df['Close'].pct_change()
    df['volatility'] = df['daily_return'].rolling(20).std()
    df['cum_return'] = (1 + df['daily_return']).cumprod()
    df['drawdown'] = df['cum_return'] / df['cum_return'].cummax() - 1
    return df
def validate_ohlcv(df):
    required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required OHLCV column: {col}")
    if df.duplicated().any():
        print("Warning: duplicate rows found")
    if df.isnull().any().any():
        print("Warning: missing values detected")
