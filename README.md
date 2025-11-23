# Predicting Price Moves with News Sentiment - Week 1 
## Task 1
**Author** Kernemi Kidane
**Branches:**  
- `task-1`: Environment setup, GitHub workflow, project structure  
- `task-2`: Quantitative analysis of stock prices  

## Overview

This repository implements the first two tasks of the financial news sentiment project:

1. **Task-1:** Set up Python environment, GitHub repo, and basic CI skeleton.  
2. **Task-2:** Load stock price data, compute technical indicators (SMA, RSI, MACD), visualize results, and prepare the dataset for correlation analysis (Task-3).  

Indicators are computed with TA-Lib if installed; otherwise, a pandas fallback is used.  

## Project Structure
```
src/
├── init.py
├── finance/
│ ├── init.py
│ ├── loader.py # Load and clean stock CSV data
│ ├── indicators.py # SMA, RSI, MACD calculations
│ └── visualize.py # Plotting utilities

scripts/
├── sample_task2_analysis.py # Example workflow: load → indicators → plot

tests/
├── test_sample.py
├── test_indicators.py # Unit tests for SMA, RSI, MACD

notebooks/
└── task2_stock_EDA.ipynb # EDA and exploratory notebook

.github/workflows/
└── unittests.yml # CI pipeline skeleton

.vscode/settings.json
requirements.txt
README.md
.gitignore
```
## Quickstart

### 1. Setup environment

**Unix/macOS**
```bash
python -m venv .venv
source .venv/bin/activate
```
```windows
python -m venv .venv
.venv\Scripts\activate
```
### 2. install dependencies
```
pip install -r requirements.txt
```
### 3. run sample analysis and unit tests
```
python scripts/sample_task2_analysis.py
pytest -q
```

## Task2-Public Functions (with docstrings)
-src/finance/loader.py
```def load_stock_data(path: str) -> pd.DataFrame:
    """
    Load stock price data CSV and clean/normalize dates.

    Args:
        path (str): Path to CSV file containing OHLCV data.

    Returns:
        pd.DataFrame: Cleaned DataFrame with datetime index in UTC and columns: date, open, high, low, close, volume.
    """
```
-src/finance/indicators.py
```
def sma(df: pd.DataFrame, period: int = 20) -> pd.DataFrame:
    """Compute Simple Moving Average (SMA) on closing prices."""
    
def rsi(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    """Compute Relative Strength Index (RSI) on closing prices."""
    
def macd(df: pd.DataFrame) -> pd.DataFrame:
    """Compute MACD line, signal line, and histogram for closing prices."""
```
-src/finance/visualize.py
```
def plot_price_with_sma(df: pd.DataFrame, period: int = 20):
    """Plot closing prices with SMA overlay."""

def plot_rsi(df: pd.DataFrame, period: int = 14):
    """Plot RSI indicator over time with overbought/oversold lines."""

def plot_macd(df: pd.DataFrame):
    """Plot MACD, signal line, and histogram."""
```
## Current Progress
Task-1: Completed
- Repository structure, venv setup, GitHub workflow
- Basic pytest skeleton, README

Task-2: Partial
- Stock CSV loading & cleaning implemented
- SMA, RSI, MACD calculations implemented (pandas fallback works)
- Visualization utilities ready
- Unit tests for indicators completed
- Sample notebook and analysis script implemented
Next Steps
- Run indicators across full universe of tickers
- Generate plots for multiple tickers
- Prepare dataset for sentiment correlation analysis (Task-3)
  
## Example usage
```
from finance.loader import load_stock_data
from finance.indicators import sma, rsi, macd
from finance.visualize import plot_price_with_sma

df = load_stock_data("your path")
df = sma(df, 20)
df = rsi(df, 14)
df = macd(df)

plot_price_with_sma(df, 20).show()
```
