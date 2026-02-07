import matplotlib.pyplot as plt
import pandas as pd


def plot_price(
    prices: pd.Series,
    title: str = "Price",
    figsize: tuple = (14, 5),
):
    plt.figure(figsize=figsize)
    plt.plot(prices.index, prices.values)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()


def plot_returns(
    returns: pd.Series,
    title: str = "Daily Returns",
    figsize: tuple = (14, 5),
):
    plt.figure(figsize=figsize)
    plt.plot(returns.index, returns.values)
    plt.axhline(0, linestyle="--", alpha=0.5)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Return")
    plt.show()


def plot_return_histogram(
    returns: pd.Series,
    bins: int = 50,
    title: str = "Return Distribution",
    figsize: tuple = (8, 5),
):
    plt.figure(figsize=figsize)
    plt.hist(returns.values, bins=bins, alpha=0.7)
    plt.title(title)
    plt.xlabel("Return")
    plt.ylabel("Frequency")
    plt.show()


def plot_volatility(
    volatility: pd.Series,
    title: str = "Rolling Volatility",
    figsize: tuple = (14, 5),
):
    plt.figure(figsize=figsize)
    plt.plot(volatility.index, volatility.values)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.show()


def plot_price_with_volatility(
    prices: pd.Series,
    volatility: pd.Series,
    title: str = "Price with Volatility Overlay",
    figsize: tuple = (14, 5),
):
    fig, ax1 = plt.subplots(figsize=figsize)

    ax1.plot(prices.index, prices.values)
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Price")

    ax2 = ax1.twinx()
    ax2.plot(volatility.index, volatility.values, alpha=0.3)
    ax2.set_ylabel("Volatility")

    plt.title(title)
    plt.show()


def plot_cumulative_returns(
    cumulative_returns: pd.Series,
    title: str = "Cumulative Returns",
    figsize: tuple = (14, 5),
):
    plt.figure(figsize=figsize)
    plt.plot(cumulative_returns.index, cumulative_returns.values)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Growth of $1")
    plt.show()


def plot_multiple_cumulative_returns(
    cumulative_returns: dict,
    title: str = "Cumulative Returns Comparison",
    figsize: tuple = (14, 5),
):
    plt.figure(figsize=figsize)

    for label, series in cumulative_returns.items():
        plt.plot(series.index, series.values, label=label)

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Growth of $1")
    plt.legend()
    plt.show()
