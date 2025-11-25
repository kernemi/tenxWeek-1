import pandas as pd
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

# Headline length stats
def headline_length_stats(df, text_col='headline'):
    df['headline_len'] = df[text_col].str.len()
    return df['headline_len'].describe()

# Publisher counts
def publisher_article_counts(df, publisher_col='publisher'):
    return df[publisher_col].value_counts()

# Daily trends
def daily_trends(df, date_col='date_utc_date'):
    return df.groupby(date_col).size()

# Keyword / topic extraction
def top_keywords(df, text_col='headline', top_n=20):
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df[text_col])
    word_counts = X.toarray().sum(axis=0)
    keywords = dict(zip(vectorizer.get_feature_names_out(), word_counts))
    return Counter(keywords).most_common(top_n)

# Plot publisher distribution
def plot_publisher_counts(counts):
    counts.plot(kind='bar', figsize=(10,5), title='Articles per Publisher')
    plt.show()
