import pandas as pd

class FNSPIDLoader:
    """
    Load and merge Financial News and Stock Price Integration Dataset (FNSPID).
    
    Attributes:
        news_path (str): CSV path for news headlines.
        stock_path (str): CSV path for stock prices.
    """
    def __init__(self, news_path: str, stock_path: str):
        self.news_path = news_path
        self.stock_path = stock_path

    def load_news(self) -> pd.DataFrame:
        """Load news CSV and normalize date to UTC."""
        df = pd.read_csv(self.news_path)
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        if df['date'].dt.tz is None:
            df['date'] = df['date'].dt.tz_localize('UTC')
        return df

    def load_stock(self) -> pd.DataFrame:
        """Load stock CSV and normalize date to UTC."""
        df = pd.read_csv(self.stock_path)
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        if df['date'].dt.tz is None:
            df['date'] = df['date'].dt.tz_localize('UTC')
        return df

    def merge_news_stock(self) -> pd.DataFrame:
        """Merge news and stock prices on date & ticker symbol."""
        news = self.load_news()
        stock = self.load_stock()
        df = pd.merge(news, stock, how='inner', left_on=['date','stock'], right_on=['date','stock'])
        return df
