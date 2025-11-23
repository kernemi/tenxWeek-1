from src.finance.loader import load_stock_data
from src.finance.indicators import sma, rsi, macd
from src.finance.visualize import plot_price_with_sma, plot_rsi, plot_macd
from pathlib import Path
import sys

sys.path.append(str(Path().resolve().parent))

df = load_stock_data("../../data/NVDA.csv")

df = sma(df, 20)
df = rsi(df, 14)
df = macd(df)

# Save results
df.to_csv("data/NVDA_with_indicators.csv", index=False)

plot_price_with_sma(df, 20).show()
plot_rsi(df, 14).show()
plot_macd(df).show()
