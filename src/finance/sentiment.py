from textblob import TextBlob
import pandas as pd

class SentimentAnalyzer:
    """
    Perform sentiment scoring on financial news headlines.
    """
    def __init__(self, df: pd.DataFrame, text_col: str = "headline"):
        self.df = df
        self.text_col = text_col

    def score_sentiment(self) -> pd.DataFrame:
        """Add a 'sentiment' column (-1 to 1) based on headline text."""
        self.df['sentiment'] = self.df[self.text_col].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
        return self.df
