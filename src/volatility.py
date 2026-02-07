import pandas as pd


def compute_rolling_volatility(
    returns: pd.Series,
    window: int = 20,
    annualize: bool = False,
    trading_days: int = 252,
) -> pd.Series:
    """
    Compute rolling volatility using standard deviation.

    Parameters
    ----------
    returns : pd.Series
        Daily arithmetic returns
    window : int
        Rolling window size (e.g. 20 days)
    annualize : bool
        Whether to annualize volatility
    trading_days : int
        Number of trading days per year (used if annualize=True)

    Returns
    -------
    pd.Series
        Rolling volatility
    """
    vol = returns.rolling(window).std()

    if annualize:
        vol = vol * (trading_days ** 0.5)

    return vol.dropna()


def compute_abs_return_volatility(
    returns: pd.Series,
    window: int = 20,
) -> pd.Series:
    """
    Compute rolling average of absolute returns.
    Useful as a simple volatility proxy.
    """
    abs_vol = returns.abs().rolling(window).mean()
    return abs_vol.dropna()
