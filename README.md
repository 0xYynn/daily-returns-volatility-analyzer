# 📊 Daily Returns & Volatility Analyzer

## Overview

This project analyzes **daily returns, volatility, and risk-adjusted performance** of financial assets using historical price data.
It focuses on understanding **market behavior**, **volatility clustering**, and **risk vs return trade-offs** rather than building trading strategies.

The analysis is implemented as a **clean, modular Python research pipeline**, following best practices used in quantitative finance research.

---

## Objectives

* Compute and analyze **daily arithmetic and logarithmic returns**
* Visualize **return distributions** and **volatility clustering**
* Estimate **rolling volatility** to identify regime changes
* Compare **cumulative performance** across assets
* Evaluate **risk-adjusted performance** using Sharpe, Sortino, and Max Drawdown
* Build intuition for how different assets behave over time

---

## Assets Analyzed

* **BTC-USD** (Bitcoin)
* **SPY** (S&P 500 ETF)

All assets are analyzed on the **daily timeframe** over multi-year histories.

---

## Project Structure

```
daily-returns-volatility-analyzer/
│
├── data/
│   ├── raw/              # Raw downloaded price data (CSV)
│
├── src/
│   ├── data_loader.py    # Data ingestion and cleaning
│   ├── returns.py        # Arithmetic & log returns
│   ├── volatility.py     # Rolling volatility measures
│   ├── metrics.py        # Sharpe, Sortino, Max Drawdown
│   └── plots.py          # Visualization utilities
│
├── main.py               # End-to-end analysis pipeline
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## Methodology

### 1. Data Ingestion

* Historical daily OHLCV data is sourced using **Yahoo Finance**
* Data is cleaned to ensure:
  * Numeric price fields
  * Consistent datetime index
  * No missing values
* Raw data is stored separately to preserve reproducibility

### 2. Returns

* **Arithmetic returns** are used for:
  * Volatility estimation
  * Cumulative return calculation
* **Log returns** are computed for completeness and comparison
* Return distributions are visualized using histograms to highlight:
  * Fat tails
  * Asymmetry
  * Non-normal behavior

### 3. Volatility

* Rolling volatility is estimated using:
  * 20-day rolling standard deviation of returns
* This reveals:
  * Volatility clustering
  * Regime shifts
  * Differences in risk dynamics across assets

### 4. Performance Metrics

For each asset, the following metrics are computed:
* **Sharpe Ratio** – penalizes total volatility
* **Sortino Ratio** – penalizes downside volatility only
* **Maximum Drawdown** – measures worst peak-to-trough loss

These metrics are interpreted jointly to avoid misleading conclusions.

### 5. Visualization

Each asset is displayed using a **single dashboard-style figure**:

1. Price
2. Daily returns
3. Rolling volatility
4. Cumulative returns

This layout mirrors how quantitative researchers reason about markets:
**price → returns → risk → performance**

---

## Key Observations

* **Volatility clusters across all assets**, but clustering is significantly stronger and more persistent in BTC.
* **BTC exhibits much higher baseline volatility** than equities, even during “calm” periods.
* **Sharpe ratios tend to understate BTC’s performance** due to symmetric volatility penalization.
* **Sortino ratios provide a more informative view** for asymmetric return profiles like crypto.
* High cumulative returns often coincide with **large and prolonged drawdowns**, highlighting the importance of risk management.

---

## Tools & Libraries

* Python 3
* pandas
* NumPy
* matplotlib
* yfinance
* scipy

---

## How to Run

1. Create and activate a virtual environment
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the analysis:

   ```bash
   python main.py
   ```

Each asset will generate a consolidated dashboard and print summary risk metrics.

---

## Why This Project Matters

This project demonstrates:

* Clean financial time-series preprocessing
* Proper separation of data, computation, and visualization
* Practical understanding of volatility and risk
* Quantitative reasoning beyond indicator-based analysis

It serves as a **foundation for more advanced work**, including:

* regime detection
* strategy research
* risk-based portfolio construction

---

## Possible Extensions

* Add intraday data
* Compare additional asset classes
* Introduce regime classification
* Export dashboards automatically
* Extend metrics to rolling Sharpe/Sortino

---

## Author

Built as a self-directed qf project to develop intuition around **returns, volatility, and risk**.
