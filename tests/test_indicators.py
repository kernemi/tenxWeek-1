import pandas as pd
from src.finance.indicators import sma, rsi, macd


def sample_df():
    return pd.DataFrame({
        "close": [100, 101, 102, 103, 104, 105]
    })


def test_sma():
    df = sma(sample_df(), 3)
    assert "SMA_3" in df.columns


def test_rsi():
    df = rsi(sample_df(), 3)
    assert df.filter(like="RSI").shape[1] == 1


def test_macd():
    df = macd(sample_df())
    assert "MACD" in df.columns
    assert "MACD_signal" in df.columns
