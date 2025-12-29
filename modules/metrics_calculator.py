"""
METRICS CALCULATOR MODULE
Calculates all performance and risk metrics for portfolios
"""

import pandas as pd
import numpy as np
from scipy import stats

class MetricsCalculator:
    """
    Calculates comprehensive performance and risk metrics
    """
    
    def __init__(self, price_data, portfolio_analyzer, risk_free_rate=0.065):
        """
        Initialize metrics calculator
        
        Args:
            price_data (pd.DataFrame): Historical price data
            portfolio_analyzer (PortfolioAnalyzer): Portfolio analyzer instance
            risk_free_rate (float): Annual risk-free rate (default: 6.5%)
        """
        self.price_data = price_data
        self.analyzer = portfolio_analyzer
        self.risk_free_rate = risk_free_rate
        
        self.daily_returns = portfolio_analyzer.portfolio_returns
        self.cumulative_returns = portfolio_analyzer.get_cumulative_returns()
        self.drawdown = portfolio_analyzer.get_drawdown()
    
    def calculate_all_metrics(self):
        """
        Calculate all metrics at once
        
        Returns:
            dict: All calculated metrics
        """
        return {
            'CAGR': self.calculate_cagr(),
            'Total Return': self.calculate_total_return(),
            'Annual Return': self.calculate_annual_return(),
            'Monthly Return': self.calculate_monthly_return(),
            'Annual Volatility': self.calculate_annual_volatility(),
            'Monthly Volatility': self.calculate_monthly_volatility(),
            'Daily Volatility': self.calculate_daily_volatility(),
            'Sharpe Ratio': self.calculate_sharpe_ratio(),
            'Information Ratio': self.calculate_information_ratio(),
            'Sortino Ratio': self.calculate_sortino_ratio(),
            'Calmar Ratio': self.calculate_calmar_ratio(),
            'Max Drawdown': self.calculate_max_drawdown(),
            'Average Drawdown': self.calculate_average_drawdown(),
            'Drawdown Duration': self.calculate_drawdown_duration(),
            'Ulcer Index': self.calculate_ulcer_index(),
            'Conditional Value at Risk': self.calculate_cvar(),
            'Value at Risk': self.calculate_var(),
            'Skewness': self.calculate_skewness(),
            'Kurtosis': self.calculate_kurtosis(),
            'Tracking Error': self.calculate_tracking_error(),
            'Beta': self.calculate_beta(),
            'Recovery Factor': self.calculate_recovery_factor(),
            'Profit Factor': self.calculate_profit_factor(),
            'Win Rate': self.calculate_win_rate(),
        }
    
    def calculate_cagr(self):
        """Calculate Compound Annual Growth Rate"""
        if len(self.price_data) < 2:
            return 0
        total_return = self.calculate_total_return()
        num_years = len(self.price_data) / 252
        if num_years <= 0:
            return 0
        cagr = (1 + total_return) ** (1 / num_years) - 1
        return cagr
    
    def calculate_total_return(self):
        """Calculate total return from start to end"""
        return (1 + self.daily_returns).prod() - 1
    
    def calculate_annual_return(self):
        """Calculate annualized return"""
        return self.daily_returns.mean() * 252
    
    def calculate_monthly_return(self):
        """Calculate average monthly return"""
        return self.daily_returns.mean() * 21
    
    def calculate_annual_volatility(self):
        """Calculate annualized volatility"""
        return self.daily_returns.std() * np.sqrt(252)
    
    def calculate_monthly_volatility(self):
        """Calculate monthly volatility"""
        return self.daily_returns.std() * np.sqrt(21)
    
    def calculate_daily_volatility(self):
        """Calculate daily volatility"""
        return self.daily_returns.std()
    
    def calculate_sharpe_ratio(self):
        """Calculate Sharpe Ratio"""
        excess_return = self.calculate_annual_return() - self.risk_free_rate
        volatility = self.calculate_annual_volatility()
        if volatility == 0:
            return 0
        return excess_return / volatility
    
    def calculate_information_ratio(self):
        """Calculate Information Ratio"""
        benchmark_return = self.daily_returns.mean()
        active_return = self.daily_returns.mean() - benchmark_return
        tracking_error = self.calculate_tracking_error()
        if tracking_error == 0:
            return 0
        ir = (active_return * 252) / tracking_error
        return ir
    
    def calculate_sortino_ratio(self):
        """Calculate Sortino Ratio"""
        excess_return = self.calculate_annual_return() - self.risk_free_rate
        downside_returns = self.daily_returns[self.daily_returns < 0]
        if len(downside_returns) == 0:
            return 0
        downside_volatility = downside_returns.std() * np.sqrt(252)
        if downside_volatility == 0:
            return 0
        return excess_return / downside_volatility
    
    def calculate_calmar_ratio(self):
        """Calculate Calmar Ratio"""
        cagr = self.calculate_cagr()
        max_dd = self.calculate_max_drawdown()
        if max_dd == 0:
            return 0
        return cagr / abs(max_dd)
    
    def calculate_max_drawdown(self):
        """Calculate Maximum Drawdown"""
        if len(self.drawdown) == 0:
            return 0
        return self.drawdown.min()
    
    def calculate_average_drawdown(self):
        """Calculate Average Drawdown"""
        drawdowns = self.drawdown[self.drawdown < 0]
        if len(drawdowns) == 0:
            return 0
        return drawdowns.mean()
    
    def calculate_drawdown_duration(self):
        """Calculate average drawdown duration in days"""
        in_drawdown = (self.drawdown < 0).astype(int)
        drawdown_groups = (in_drawdown.diff() != 0).cumsum()
        durations = []
        for group in drawdown_groups.unique():
            if in_drawdown[drawdown_groups == group].iloc[0] < 0:
                durations.append(len(drawdown_groups[drawdown_groups == group]))
        if len(durations) == 0:
            return 0
        return np.mean(durations)
    
    def calculate_ulcer_index(self):
        """Calculate Ulcer Index"""
        squared_drawdowns = (self.drawdown ** 2)
        ui = np.sqrt(squared_drawdowns.mean())
        return ui
    
    def calculate_var(self, confidence=0.95):
        """Calculate Value at Risk (VaR)"""
        return np.percentile(self.daily_returns, (1 - confidence) * 100)
    
    def calculate_cvar(self, confidence=0.95):
        """Calculate Conditional Value at Risk (CVaR)"""
        var = self.calculate_var(confidence)
        return self.daily_returns[self.daily_returns <= var].mean()
    
    def calculate_skewness(self):
        """Calculate Skewness of returns"""
        return stats.skew(self.daily_returns)
    
    def calculate_kurtosis(self):
        """Calculate Kurtosis of returns"""
        return stats.kurtosis(self.daily_returns)
    
    def calculate_tracking_error(self, benchmark_daily_return=None):
        """Calculate Tracking Error"""
        if benchmark_daily_return is None:
            benchmark_daily_return = self.daily_returns.mean()
        active_returns = self.daily_returns - benchmark_daily_return
        te = active_returns.std() * np.sqrt(252)
        return te
    
    def calculate_beta(self, market_returns=None):
        """Calculate Beta relative to market"""
        if market_returns is None:
            market_returns = pd.Series(
                [self.daily_returns.mean()] * len(self.daily_returns),
                index=self.daily_returns.index
            )
        common_index = self.daily_returns.index.intersection(market_returns.index)
        if len(common_index) < 2:
            return 0
        portfolio_ret = self.daily_returns.loc[common_index]
        market_ret = market_returns.loc[common_index]
        covariance = np.cov(portfolio_ret, market_ret)[0, 1]
        market_variance = np.var(market_ret)
        if market_variance == 0:
            return 0
        return covariance / market_variance
    
    def calculate_recovery_factor(self):
        """Calculate Recovery Factor"""
        total_profit = self.calculate_total_return()
        max_dd = abs(self.calculate_max_drawdown())
        if max_dd == 0:
            return 0 if total_profit == 0 else float('inf')
        return total_profit / max_dd
    
    def calculate_profit_factor(self):
        """Calculate Profit Factor"""
        gains = self.daily_returns[self.daily_returns > 0].sum()
        losses = abs(self.daily_returns[self.daily_returns < 0].sum())
        if losses == 0:
            return 0 if gains == 0 else float('inf')
        return gains / losses
    
    def calculate_win_rate(self):
        """Calculate Win Rate"""
        winning_days = (self.daily_returns > 0).sum()
        total_days = len(self.daily_returns)
        return winning_days / total_days if total_days > 0 else 0
