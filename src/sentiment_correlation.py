# src/sentiment_correlation.py
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from src.sentiment import aggregate_daily_sentiment
from src.finance_metrics import compute_daily_returns

def sentiment_return_pipeline(news_df, stock_df, date_col='date_utc_date', ticker_col='stock'):
    # Aggregate sentiment by date and ticker
    daily_sent = aggregate_daily_sentiment(news_df)
    
    # Compute stock daily returns
    stock_df = compute_daily_returns(stock_df)
    
    # Merge datasets
    merged = pd.merge(daily_sent, stock_df, left_on=[date_col, ticker_col], right_on=[date_col, ticker_col], how='inner')
    
    # Compute correlations per sentiment column
    sentiment_cols = [col for col in merged.columns if 'sentiment' in col]
    results = {}
    for col in sentiment_cols:
        pearson_corr, pearson_p = pearsonr(merged[col], merged['daily_return'])
        spearman_corr, spearman_p = spearmanr(merged[col], merged['daily_return'])
        results[col] = {'pearson_corr': pearson_corr, 'pearson_p': pearson_p,
                        'spearman_corr': spearman_corr, 'spearman_p': spearman_p}
    return merged, results
