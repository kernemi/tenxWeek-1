import matplotlib.pyplot as plt
import pandas as pd


def plot_price_with_sma(df: pd.DataFrame, period: int = 20):
    plt.figure(figsize=(12, 5))
    plt.plot(df['date'], df['close'], label='Close')
    plt.plot(df['date'], df[f"SMA_{period}"], label=f"SMA {period}")
    plt.title("Close Price with SMA")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    return plt


def plot_rsi(df: pd.DataFrame, period: int = 14):
    plt.figure(figsize=(12, 4))
    plt.plot(df['date'], df[f"RSI_{period}"])
    plt.axhline(70, linestyle='--')
    plt.axhline(30, linestyle='--')
    plt.title("RSI Indicator")
    plt.tight_layout()
    return plt


def plot_macd(df: pd.DataFrame):
    plt.figure(figsize=(12, 4))
    plt.plot(df['date'], df["MACD"], label="MACD")
    plt.plot(df['date'], df["MACD_signal"], label="Signal")
    plt.bar(df['date'], df["MACD_hist"], label="Histogram")
    plt.legend()
    plt.title("MACD")
    plt.tight_layout()
    return plt
