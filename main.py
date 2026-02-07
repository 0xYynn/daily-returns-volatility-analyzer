# =========================
# MAIN PIPELINE (DASHBOARD)
# =========================

import matplotlib.pyplot as plt

from src.data_loader import load_price_data
from src.returns import (
    compute_arithmetic_returns,
    compute_log_returns,
    compute_cumulative_returns,
)
from src.volatility import (
    compute_rolling_volatility,
    compute_abs_return_volatility,
)
from src.metrics import (
    sharpe_ratio,
    sortino_ratio,
    max_drawdown,
)


def plot_asset_dashboard(
    prices,
    returns,
    rolling_vol,
    cumulative_returns,
    ticker,
):
    fig, axs = plt.subplots(4, 1, figsize=(14, 12), sharex=True)

    # 1. Price
    axs[0].plot(prices.index, prices.values)
    axs[0].set_title(f"{ticker} Price")

    # 2. Returns
    axs[1].plot(returns.index, returns.values)
    axs[1].axhline(0, linestyle="--", alpha=0.5)
    axs[1].set_title("Daily Returns")

    # 3. Volatility
    axs[2].plot(rolling_vol.index, rolling_vol.values)
    axs[2].set_title("20-Day Rolling Volatility")

    # 4. Cumulative Returns
    axs[3].plot(cumulative_returns.index, cumulative_returns.values)
    axs[3].set_title("Cumulative Returns (Growth of $1)")

    plt.tight_layout()
    plt.show()


def analyze_asset(ticker: str):
    print(f"\n===== {ticker} =====")

    # -------------------------
    # Load data
    # -------------------------
    df = load_price_data(ticker)
    prices = df["Close"]

    # -------------------------
    # Returns
    # -------------------------
    arith_returns = compute_arithmetic_returns(prices)
    log_returns = compute_log_returns(prices)
    cumulative_returns = compute_cumulative_returns(arith_returns)

    # -------------------------
    # Volatility
    # -------------------------
    rolling_vol = compute_rolling_volatility(arith_returns, window=20)

    # -------------------------
    # Metrics
    # -------------------------
    sharpe = sharpe_ratio(arith_returns)
    sortino = sortino_ratio(arith_returns)
    mdd = max_drawdown(cumulative_returns)

    print(f"Sharpe Ratio  : {sharpe:.2f}")
    print(f"Sortino Ratio : {sortino:.2f}")
    print(f"Max Drawdown  : {mdd:.2%}")

    # -------------------------
    # Dashboard plot
    # -------------------------
    plot_asset_dashboard(
        prices=prices,
        returns=arith_returns,
        rolling_vol=rolling_vol,
        cumulative_returns=cumulative_returns,
        ticker=ticker,
    )

    return cumulative_returns


def main():
    tickers = ["BTC-USD", "SPY"]

    for ticker in tickers:
        analyze_asset(ticker)


if __name__ == "__main__":
    main()
