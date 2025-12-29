"""
PORTFOLIO ANALYZER MODULE
Handles portfolio calculations and analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime

class PortfolioAnalyzer:
    """
    Analyzes portfolio performance and characteristics
    """
    
    def __init__(self, stocks, weights, price_data):
        """
        Initialize portfolio analyzer
        
        Args:
            stocks (list): List of stock symbols
            weights (dict): Dictionary of {stock: weight_percentage}
            price_data (pd.DataFrame): Historical price data
        """
        self.stocks = stocks
        self.weights = weights
        self.price_data = price_data
        
        # Normalize weights (ensure they sum to 100%)
        total_weight = sum(weights.values())
        self.weights_normalized = {k: v/total_weight for k, v in weights.items()}
        
        # Convert to array for calculations
        self.weight_array = np.array([self.weights_normalized[stock] for stock in stocks])
        
        # Calculate returns
        self.daily_returns = price_data.pct_change().dropna()
        self.portfolio_returns = (self.daily_returns * self.weight_array).sum(axis=1)
    
    def get_portfolio_value(self, initial_investment=100000):
        """
        Calculate portfolio value over time
        
        Args:
            initial_investment (float): Starting investment amount
        
        Returns:
            pd.DataFrame: Portfolio value time series
        """
        cumulative_returns = (1 + self.portfolio_returns).cumprod() - 1
        portfolio_value = initial_investment * (1 + cumulative_returns)
        
        return pd.DataFrame({
            'Portfolio Value': portfolio_value,
            'Cumulative Return': cumulative_returns
        })
    
    def get_composition(self):
        """
        Get portfolio composition
        
        Returns:
            pd.DataFrame: Stocks and their weights
        """
        composition = pd.DataFrame({
            'Stock': self.stocks,
            'Weight (%)': [self.weights_normalized[stock] * 100 for stock in self.stocks]
        }).sort_values('Weight (%)', ascending=False)
        
        return composition
    
    def get_daily_returns(self):
        """
        Get portfolio daily returns
        
        Returns:
            pd.Series: Daily portfolio returns
        """
        return self.portfolio_returns
    
    def get_cumulative_returns(self):
        """
        Get cumulative returns
        
        Returns:
            pd.Series: Cumulative portfolio returns
        """
        return (1 + self.portfolio_returns).cumprod() - 1
    
    def get_drawdown(self):
        """
        Calculate drawdown from peak
        
        Returns:
            pd.Series: Drawdown values
        """
        cumulative = self.get_cumulative_returns()
        running_max = cumulative.expanding().max()
        drawdown = (cumulative - running_max) / (1 + running_max)
        
        return drawdown
    
    def get_correlation_matrix(self):
        """
        Get correlation matrix of stocks in portfolio
        
        Returns:
            pd.DataFrame: Correlation matrix
        """
        return self.daily_returns.corr()
    
    def get_individual_stocks_performance(self):
        """
        Get individual stock performance metrics
        
        Returns:
            pd.DataFrame: Performance metrics for each stock
        """
        performances = []
        
        for stock in self.stocks:
            returns = self.price_data[stock].pct_change().dropna()
            
            # CAGR
            total_return = (self.price_data[stock].iloc[-1] / self.price_data[stock].iloc[0]) - 1
            num_years = len(self.price_data) / 252  # Trading days in a year
            cagr = (1 + total_return) ** (1 / num_years) - 1
            
            # Volatility
            volatility = returns.std() * np.sqrt(252)
            
            performances.append({
                'Stock': stock,
                'CAGR': cagr,
                'Volatility': volatility,
                'Total Return': total_return,
                'Sharpe Ratio': (cagr - 0.065) / volatility if volatility > 0 else 0
            })
        
        return pd.DataFrame(performances).sort_values('CAGR', ascending=False)
    
    def get_portfolio_concentration(self):
        """
        Get Herfindahl-Hirschman Index (HHI) for concentration
        
        Returns:
            float: Concentration index (0-1, higher = more concentrated)
        """
        weights_squared = np.sum(self.weight_array ** 2)
        # Normalize to 0-1 scale where 1/n is minimum concentration
        n = len(self.stocks)
        hhi = (weights_squared - 1/n) / (1 - 1/n)
        
        return max(0, min(1, hhi))  # Ensure 0-1 range
    
    def get_portfolio_beta(self, benchmark_returns):
        """
        Calculate portfolio beta relative to benchmark
        
        Args:
            benchmark_returns (pd.Series): Benchmark returns
        
        Returns:
            float: Portfolio beta
        """
        # Ensure same length
        common_index = self.portfolio_returns.index.intersection(benchmark_returns.index)
        
        portfolio_ret = self.portfolio_returns.loc[common_index]
        bench_ret = benchmark_returns.loc[common_index]
        
        # Calculate covariance
        covariance = np.cov(portfolio_ret, bench_ret)[0, 1]
        benchmark_variance = np.var(bench_ret)
        
        beta = covariance / benchmark_variance if benchmark_variance != 0 else 0
        
        return beta
    
    def get_portfolio_alpha(self, benchmark_returns, risk_free_rate=0.065):
        """
        Calculate Jensen's Alpha
        
        Args:
            benchmark_returns (pd.Series): Benchmark returns
            risk_free_rate (float): Risk-free rate for CAPM
        
        Returns:
            float: Annual alpha
        """
        # Calculate returns
        portfolio_return = self.portfolio_returns.mean() * 252  # Annualized
        benchmark_return = benchmark_returns.mean() * 252
        
        # Calculate beta
        beta = self.get_portfolio_beta(benchmark_returns)
        
        # Alpha = Portfolio Return - Risk-Free Rate - Beta * (Benchmark Return - Risk-Free Rate)
        alpha = portfolio_return - (risk_free_rate + beta * (benchmark_return - risk_free_rate))
        
        return alpha
