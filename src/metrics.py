import pandas as pd
import numpy as np


def sharpe_ratio(
    returns: pd.Series,
    risk_free_rate: float = 0.0,
    trading_days: int = 252,
) -> float:
    """
    Compute annualized Sharpe Ratio.

    Sharpe = (E[R] - Rf) / std(R)
    """
    excess_returns = returns - risk_free_rate / trading_days

    mean_return = excess_returns.mean()
    std_return = excess_returns.std()

    if std_return == 0:
        return np.nan

    sharpe = (mean_return / std_return) * np.sqrt(trading_days)
    return sharpe


def sortino_ratio(
    returns: pd.Series,
    risk_free_rate: float = 0.0,
    trading_days: int = 252,
) -> float:
    """
    Compute annualized Sortino Ratio.

    Sortino = (E[R] - Rf) / downside_std(R)
    """
    excess_returns = returns - risk_free_rate / trading_days

    downside_returns = excess_returns[excess_returns < 0]
    downside_std = downside_returns.std()

    if downside_std == 0:
        return np.nan

    mean_return = excess_returns.mean()
    sortino = (mean_return / downside_std) * np.sqrt(trading_days)
    return sortino


def max_drawdown(
    cumulative_returns: pd.Series,
) -> float:
    """
    Compute maximum drawdown from cumulative returns.
    """
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    return drawdown.min()
