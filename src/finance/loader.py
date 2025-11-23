import pandas as pd

def load_stock_data(path: str) -> pd.DataFrame:
    """
    Load stock data CSV with columns: Date, Open, High, Low, Close, Volume.
    Converts Date to timezone-aware UTC.
    """
    df = pd.read_csv(path)

    # Normalize column names
    df.columns = [c.lower() for c in df.columns]

    # Parse timestamp
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # If timezone-naive, set UTC
    if df['date'].dt.tz is None:
        df['date'] = df['date'].dt.tz_localize('UTC')

    df = df.sort_values('date').reset_index(drop=True)
    return df
