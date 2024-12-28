# Risk-Metrics-Alpha-Beta-Sharpe-Ratio-Volatility-

This Python script allows users to analyze the performance of a stock portfolio relative to a market index. The analysis includes calculating key financial metrics such as **Alpha**, **Beta**, **Sharpe Ratio**, **Volatility**, and portfolio-specific metrics like **weighted returns** and **portfolio volatility**. 

The data is fetched from Yahoo Finance using the `yfinance` library, and the script offers a comprehensive comparison of the stocks' and portfolio's performance relative to an index over a user-defined date range.

## Features

- Fetches stock data and calculates daily returns.
- Calculates **Alpha** and **Beta** of individual stocks against a chosen index.
- Computes **Sharpe Ratio** and **Volatility** for both individual stocks and portfolio.
- Supports portfolio analysis, including weighted average returns and portfolio volatility.
- Generates visualizations comparing the **Volatility** and **Sharpe Ratio** of each stock and index.
- Interactive inputs for stock tickers, index tickers, date range, and portfolio weights.

## Requirements

To run this script, you will need the following Python libraries:
- `yfinance`: For fetching financial data from Yahoo Finance.
- `numpy`: For numerical calculations.
- `pandas`: For data manipulation and analysis.
- `matplotlib`: For generating visualizations.

You can install these libraries using pip:

```bash
pip install yfinance numpy pandas matplotlib
```

## Script Description

### 1. `fetch_data(tickers, start_date, end_date)`
This function fetches historical data for the given stock tickers from Yahoo Finance. It also calculates daily percentage returns for the stocks by using the adjusted closing price.

**Parameters:**
- `tickers`: A list of stock tickers (e.g., `['AAPL', 'MSFT']`).
- `start_date`: The start date for data fetching (e.g., `'2020-01-01'`).
- `end_date`: The end date for data fetching (e.g., `'2020-12-31'`).

**Returns:**
- `close_data`: A DataFrame containing the 'Close' prices for the stocks.
- `returns`: A DataFrame containing the daily returns for the stocks.

### 2. `calculate_alpha_beta(stock_returns, index_returns)`
This function calculates the **Alpha** and **Beta** of a stock relative to a market index.

**Parameters:**
- `stock_returns`: The daily returns of the stock.
- `index_returns`: The daily returns of the market index.

**Returns:**
- `alpha`: The excess return of the stock compared to the index.
- `beta`: The stock's sensitivity to market movements (volatility relative to the index).

### 3. `calculate_sharpe_volatility(returns, risk_free_rate=0.01)`
This function calculates the **Sharpe Ratio** and **Volatility** for a stock or portfolio.

**Parameters:**
- `returns`: A DataFrame containing the daily returns of a stock or portfolio.
- `risk_free_rate`: The risk-free rate (default is 0.01, which represents 1%).

**Returns:**
- `sharpe_ratio`: A measure of the risk-adjusted return of the stock or portfolio.
- `volatility`: The standard deviation of the returns, annualized by multiplying by the square root of 252 (number of trading days in a year).

### 4. `analyze_stocks(stocks, index, start_date, end_date, user_weights)`
This is the main function that performs the stock and portfolio analysis. It fetches data, calculates financial metrics for each stock, and computes portfolio performance metrics based on user-defined weights.

**Parameters:**
- `stocks`: A list of stock tickers to analyze (e.g., `['AAPL', 'MSFT']`).
- `index`: The market index ticker (e.g., `'^GSPC'` for the S&P 500).
- `start_date`: The start date for data fetching (e.g., `'2020-01-01'`).
- `end_date`: The end date for data fetching (e.g., `'2020-12-31'`).
- `user_weights`: A list or array of portfolio weights corresponding to each stock.

**Returns:**
- `results_df`: A DataFrame containing the Alpha, Beta, Sharpe Ratio, and Volatility for each stock and the index, along with the portfolio performance metrics.

### 5. User Interaction
The script will prompt users for the following inputs:
- **Stock Tickers**: Comma-separated list of stock symbols (e.g., `AAPL, MSFT, TSLA`).
- **Index Ticker**: The ticker symbol of the market index (e.g., `^GSPC` for the S&P 500).
- **Start Date**: The start date in `YYYY-MM-DD` format (e.g., `'2020-01-01'`).
- **End Date**: The end date in `YYYY-MM-DD` format (e.g., `'2020-12-31'`).
- **Portfolio Weights**: A comma-separated list of portfolio weights corresponding to each stock (e.g., `0.4, 0.3, 0.3`).

### Example Input

```
Enter stock tickers separated by commas (e.g., AAPL, MSFT, TSLA): AAPL, MSFT, TSLA
Enter the index ticker (e.g., ^GSPC for S&P 500): ^GSPC
Enter start date (YYYY-MM-DD): 2020-01-01
Enter end date (YYYY-MM-DD): 2020-12-31
Enter the weights for the stocks separated by commas (e.g., 0.4, 0.3, 0.3 for AAPL, MSFT, TSLA): 0.4, 0.3, 0.3
```

### Visualizations
- A **bar chart** comparing the **Volatility** and **Sharpe Ratio** for each stock and the index will be displayed.

## How to Use

1. Clone or download this repository to your local machine.
2. Install the required dependencies:
    ```bash
    pip install yfinance numpy pandas matplotlib
    ```
3. Run the script:
    ```bash
    python stock_analysis.py
    ```
4. Follow the on-screen prompts to input stock tickers, index ticker, date range, and portfolio weights.
5. View the performance metrics in the terminal and the visualizations.

## Example Output

### Terminal Output
```text
Stock and Index Performance Metrics:
           Alpha     Beta  Sharpe Ratio  Volatility
Index     0.0000    1.0000       0.8251      0.1875
AAPL      0.0105    1.2456       1.0512      0.2993
MSFT      0.0148    1.0802       1.1754      0.2654
TSLA      0.0123    2.2345       1.9023      0.6487

Portfolio Performance Metrics:
Portfolio Sharpe Ratio: 1.2113
Portfolio Volatility: 0.3225
```

### Visualization
A bar chart will be displayed, comparing **Volatility** and **Sharpe Ratio** for each stock and the index.


## Contributing

Feel free to fork the repository, make changes, and submit pull requests. Contributions are welcome!

## Acknowledgements

- Data provided by [Yahoo Finance](https://www.yahoo.com/finance).
- `yfinance` library used for downloading stock data.

---
