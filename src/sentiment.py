import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# For transformer-based models, e.g., HuggingFace
# from transformers import pipeline

# Baseline sentiment using VADER
def compute_vader_sentiment(df: pd.DataFrame, text_col: str = "headline") -> pd.DataFrame:
    sia = SentimentIntensityAnalyzer()
    df['vader_sentiment'] = df[text_col].apply(lambda x: sia.polarity_scores(str(x))['compound'])
    return df

# Placeholder for transformer-based sentiment
def compute_transformer_sentiment(df: pd.DataFrame, text_col: str = "headline") -> pd.DataFrame:
    """
    Add transformer-based sentiment scoring.
    Example: Use HuggingFace pipeline('sentiment-analysis') with finance-tuned model
    """
    # Uncomment when model is available
    # nlp = pipeline('sentiment-analysis', model='yiyanghkust/finbert-tone')
    # df['transformer_sentiment'] = df[text_col].apply(lambda x: nlp(str(x))[0]['score'])
    df['transformer_sentiment'] = 0.0  # placeholder
    return df

# Aggregation by day
def aggregate_daily_sentiment(df: pd.DataFrame, date_col: str = "date_utc_date") -> pd.DataFrame:
    daily = df.groupby(date_col).agg({
        'vader_sentiment': ['mean', 'median', 'count'],
        'transformer_sentiment': ['mean', 'median']
    })
    daily.columns = ['_'.join(col).strip() for col in daily.columns.values]
    daily.reset_index(inplace=True)
    return daily
