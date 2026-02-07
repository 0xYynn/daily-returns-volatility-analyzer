import pandas as pd
import numpy as np


def compute_arithmetic_returns(
    prices: pd.Series,
) -> pd.Series:
    """
    Compute arithmetic (simple) returns.

    r_t = (P_t / P_{t-1}) - 1
    """
    returns = prices.pct_change()
    return returns.dropna()


def compute_log_returns(
    prices: pd.Series,
) -> pd.Series:
    """
    Compute log returns.

    r_t = log(P_t / P_{t-1})
    """
    log_returns = np.log(prices / prices.shift(1))
    return log_returns.dropna()


def compute_cumulative_returns(
    returns: pd.Series,
) -> pd.Series:
    """
    Compute cumulative returns from arithmetic returns.

    CR_t = (1 + r_1) * ... * (1 + r_t)
    """
    cumulative = (1 + returns).cumprod()
    return cumulative
