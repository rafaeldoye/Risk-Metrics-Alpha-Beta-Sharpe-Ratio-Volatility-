import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch data and calculate returns
def fetch_data(tickers, start_date, end_date):
    # Fetch data from Yahoo Finance
    data = yf.download(tickers, start=start_date, end=end_date)
    
    # Display the first few rows of data to check structure
    print("Data preview:\n", data.head())  # Display the first few rows to see the columns
    
    # Using 'Close' directly
    close_data = data['Close']  # Using 'Close' column for simplicity
    
    # Calculate daily returns (percentage change)
    returns = close_data.pct_change().dropna()  # Percentage change to calculate returns
    return close_data, returns

# Function to calculate beta and alpha against the index
def calculate_alpha_beta(stock_returns, index_returns):
    covariance = np.cov(stock_returns, index_returns)[0, 1]
    variance = np.var(index_returns)
    beta = covariance / variance
    alpha = np.mean(stock_returns) - beta * np.mean(index_returns)
    return alpha, beta

# Function to calculate the Sharpe ratio and volatility
def calculate_sharpe_volatility(returns, risk_free_rate=0.01):
    volatility = np.std(returns) * np.sqrt(252)  # Annualize volatility
    excess_returns = returns - risk_free_rate / 252
    sharpe_ratio = np.mean(excess_returns) / np.std(excess_returns) * np.sqrt(252)  # Annualized Sharpe ratio
    return sharpe_ratio, volatility

# Main function to run the analysis
def analyze_stocks(stocks, index, start_date, end_date, user_weights):
    # Fetch the data for stocks and index
    stock_data, stock_returns = fetch_data(stocks, start_date, end_date)
    index_data, index_returns = fetch_data([index], start_date, end_date)
    
    # Create a dictionary to store the results
    results = {}
    
    # Add index metrics first
    index_alpha, index_beta = calculate_alpha_beta(index_returns[index], index_returns[index])  # Index beta is always 1, alpha is 0
    index_sharpe, index_volatility = calculate_sharpe_volatility(index_returns[index])
    
    results['Index'] = {
        'Alpha': index_alpha,
        'Beta': index_beta,
        'Sharpe Ratio': index_sharpe,
        'Volatility': index_volatility
    }

    # Calculate metrics for each stock
    for stock in stocks:
        stock_return = stock_returns[stock]
        alpha, beta = calculate_alpha_beta(stock_return, index_returns[index])
        sharpe_ratio, volatility = calculate_sharpe_volatility(stock_return)
        
        results[stock] = {
            'Alpha': alpha,
            'Beta': beta,
            'Sharpe Ratio': sharpe_ratio,
            'Volatility': volatility
        }
    
    # Convert the results dictionary to a pandas DataFrame for easy visualization
    results_df = pd.DataFrame(results).T
    
    # Portfolio metrics (weighted average)
    # Make sure user_weights sums to 1, otherwise normalize
    if np.sum(user_weights) != 1:
        print("Warning: The sum of the weights doesn't equal 1. Normalizing weights.")
        user_weights = user_weights / np.sum(user_weights)
    
    # Fixing the shape issue here by using stock_returns[stocks].mean(axis=0).values
    portfolio_return = np.dot(user_weights, stock_returns[stocks].mean(axis=0).values)  # Portfolio return is the weighted average return
    
    # Portfolio volatility: calculate based on covariance matrix
    covariance_matrix = stock_returns[stocks].cov()
    portfolio_volatility = np.sqrt(np.dot(user_weights.T, np.dot(covariance_matrix, user_weights))) * np.sqrt(252)  # Annualized volatility
    portfolio_sharpe = portfolio_return / portfolio_volatility  # Portfolio Sharpe ratio
    
    # Output results
    print("Stock and Index Performance Metrics:")
    print(results_df)
    print("\nPortfolio Performance Metrics:")
    print(f"Portfolio Sharpe Ratio: {portfolio_sharpe:.4f}")
    print(f"Portfolio Volatility: {portfolio_volatility:.4f}")
    
    # Visualize the data
    results_df['Volatility'] = results_df['Volatility'] * np.sqrt(252)
    results_df['Sharpe Ratio'] = results_df['Sharpe Ratio'] * np.sqrt(252)
    
    results_df[['Volatility', 'Sharpe Ratio']].plot(kind='bar', figsize=(10, 6))
    plt.title("Volatility & Sharpe Ratio: Stocks and Index")
    plt.ylabel("Value")
    plt.show()

    return results_df

# User inputs
stocks_input = input("Enter stock tickers separated by commas (e.g., AAPL, MSFT, TSLA): ")
stocks = stocks_input.split(',')
index_input = input("Enter the index ticker (e.g., ^GSPC for S&P 500): ")
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

# Ask the user for portfolio weights
weights_input = input(f"Enter the weights for the stocks separated by commas (e.g., 0.4, 0.3, 0.3 for {', '.join(stocks)}): ")
user_weights = np.array([float(weight) for weight in weights_input.split(',')])

# Analyze the stocks with user-defined weights
results = analyze_stocks(stocks, index_input, start_date, end_date, user_weights)
