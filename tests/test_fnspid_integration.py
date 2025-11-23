"""
finance.loader
---------------
Functions and classes to load stock and financial news datasets.
"""
import pandas as pd
from src.finance.fnspid_loader import FNSPIDLoader
from src.finance.sentiment import SentimentAnalyzer

def test_fnspid_workflow():
    loader = FNSPIDLoader("tests/data/news_sample.csv", "tests/data/stock_sample.csv")
    df = loader.merge_news_stock()
    assert not df.empty
    analyzer = SentimentAnalyzer(df)
    df_scored = analyzer.score_sentiment()
    assert 'sentiment' in df_scored.columns
