import yfinance as yf
import pandas as pd
from pathlib import Path


DATA_RAW_DIR = Path("data/raw")


def load_price_data(
    ticker: str,
    start: str = "2018-01-01",
    end: str | None = None,
    save: bool = True,
) -> pd.DataFrame:
    """
    Download daily price data for a single asset.

    Parameters
    ----------
    ticker : str
        Asset ticker (e.g. 'BTC-USD', 'SPY')
    start : str
        Start date (YYYY-MM-DD)
    end : str | None
        End date (YYYY-MM-DD), None = today
    save : bool
        Whether to save raw CSV to data/raw/

    Returns
    -------
    pd.DataFrame
        Cleaned OHLCV data with datetime index
    """

    DATA_RAW_DIR.mkdir(parents=True, exist_ok=True)

    df = yf.download(
        ticker,
        start=start,
        end=end,
        progress=False,
        auto_adjust=False,
    )

    if df.empty:
        raise ValueError(f"No data returned for ticker: {ticker}")

    # Flatten columns if yfinance returns MultiIndex
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Ensure numeric prices
    for col in ["Open", "High", "Low", "Close", "Adj Close", "Volume"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna()
    df.index.name = "Date"

    if save:
        file_path = DATA_RAW_DIR / f"{ticker}.csv"
        df.to_csv(file_path)

    return df
