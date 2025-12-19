# Quantitative Market Analysis Using Technical Indicators in Python

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Yahoo Finance](https://img.shields.io/badge/yfinance-Finance-green?style=for-the-badge)

## Project Overview
This project focuses on the quantitative analysis of equity price behavior using technical indicators and historical market data. By adopting a systematic and programmatic approach—similar to quantitative trading and research teams—this study analyzes price dynamics, momentum, volatility, and volume.

The analysis is performed on five years of historical daily data for **RELIANCE.NS**, with a focused visualization on the most recent **252 trading days** (one year) to ensure signal clarity.



## Objectives
- **Data Retrieval:** Programmatically fetch and preprocess financial time series data.
- **Indicator Computation:** Calculate quantitative technical indicators used in modern trading models.
- **Signal Analysis:** Analyze trends, momentum, and volatility from a mathematical perspective.
- **Visualization:** Create structured, multi-panel visualizations of market signals.
- **Strategy Foundation:** Build the groundwork for rule-based and algorithmic trading.

## Data Source
- **Source:** Yahoo Finance (`yfinance`)
- **Instrument:** RELIANCE.NS
- **Frequency:** Daily
- **Lookback Period:** 5 Years
- **Features:** Open, High, Low, Close, Volume

## Quantitative Indicators Implemented

### 1. Exponential Moving Averages (EMA)
Used for trend filtering and regime identification:
* **EMA 10:** Short-term signal sensitivity.
* **EMA 50:** Medium-term trend filtering.
* **EMA 200:** Long-term regime identification.



### 2. Bollinger Bands
* **Configuration:** 20-period moving average with ±2 standard deviations.
* **Purpose:** Measures volatility expansion/contraction and identifies potential mean-reversion or breakout points.

### 3. Relative Strength Index (RSI)
* **Configuration:** 14-period momentum oscillator.
* **Purpose:** Captures momentum shifts and identifies overbought (>70) or oversold (<30) conditions.

### 4. Volume-Based Confirmation
* Analyzes daily traded volume to validate the strength of price movements and confirm signals.

## Methodology
1.  **Extraction:** Download historical data using the `yfinance` API.
2.  **Preprocessing:** Clean and align time series, handling any missing values.
3.  **Calculation:** Compute rolling and exponentially weighted technical indicators using `pandas` and `numpy`.
4.  **Segmentation:** Isolate the most recent 252 trading days for detailed inspection.
5.  **Visualization:** Generate multi-panel quantitative charts using `mplfinance`.

## Tools and Technologies
- **Language:** Python
- **Data Manipulation:** `pandas`, `numpy`
- **Finance API:** `yfinance`
- **Visualization:** `matplotlib`, `mplfinance`
- **Time Management:** `datetime`

## Key Quantitative Observations
- **EMA Crossovers:** Provide a robust trend-following signal structure.
- **Bollinger Band Width:** Directly reflects changing volatility regimes (Squeeze vs. Expansion).
- **RSI Inflections:** Successfully captures points where price momentum begins to exhaust.
- **Volume Validation:** Essential for distinguishing between "noise" and high-conviction price moves.

## Future Extensions
- [ ] **Backtesting:** Implement historical simulation to test signal profitability.
- [ ] **Risk Metrics:** Integrate Maximum Drawdown (MDD) and Sharpe Ratio calculations.
- [ ] **Optimization:** Use parameter tuning to find the best lookback periods for indicators.
- [ ] **Execution Logic:** Develop rule-based logic for automated trade entry and exit.

## Disclaimer
*This project is for research and educational purposes only. The signals and analysis presented do not represent live trading or investment advice.*
