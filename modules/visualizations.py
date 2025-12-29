
"""
VISUALIZATIONS MODULE
Creates interactive charts using Plotly
"""

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

class PortfolioVisualizer:
    """
    Creates interactive visualizations for portfolio analysis
    """
    
    def __init__(self, price_data, portfolio_analyzer, metrics):
        """
        Initialize visualizer
        
        Args:
            price_data (pd.DataFrame): Historical price data
            portfolio_analyzer (PortfolioAnalyzer): Portfolio analyzer instance
            metrics (dict): Calculated metrics
        """
        self.price_data = price_data
        self.analyzer = portfolio_analyzer
        self.metrics = metrics
        self.portfolio_value = portfolio_analyzer.get_portfolio_value()
    
    def plot_portfolio_value(self, initial_investment=100000, chart_id="portfolio_value"):
        """Plot portfolio value over time"""
        fig = go.Figure()
        
        if len(self.portfolio_value) == 0:
            fig.add_annotation(
                text="No data available",
                showarrow=False,
                x=0.5,
                y=0.5
            )
            return fig
        
        fig.add_trace(go.Scatter(
            x=self.portfolio_value.index,
            y=self.portfolio_value['Portfolio Value'],
            mode='lines',
            name='Portfolio Value',
            line=dict(color='#003366', width=3),
            fill='tozeroy',
            fillcolor='rgba(0, 51, 102, 0.1)',
            uid=f'{chart_id}_trace_1'
        ))
        
        # Add annotations only if data exists
        if len(self.portfolio_value) > 0:
            fig.add_annotation(
                x=self.portfolio_value.index[0],
                y=self.portfolio_value['Portfolio Value'].iloc[0],
                text=f"Start: ₹{self.portfolio_value['Portfolio Value'].iloc[0]:,.0f}",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor='#003366'
            )
            
            fig.add_annotation(
                x=self.portfolio_value.index[-1],
                y=self.portfolio_value['Portfolio Value'].iloc[-1],
                text=f"End: ₹{self.portfolio_value['Portfolio Value'].iloc[-1]:,.0f}",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor='#003366'
            )
        
        fig.update_layout(
            title="Portfolio Value Over Time",
            xaxis_title="Date",
            yaxis_title="Portfolio Value (₹)",
            hovermode='x unified',
            template='plotly_white',
            height=500,
            font=dict(family="Times New Roman"),
            plot_bgcolor='rgba(173, 216, 230, 0.1)',
            uirevision=chart_id
        )
        
        return fig
    
    def plot_cumulative_returns(self, chart_id="cumulative_returns"):
        """Plot cumulative returns over time"""
        cumulative_returns = self.analyzer.get_cumulative_returns()
        
        fig = go.Figure()
        
        if len(cumulative_returns) == 0:
            fig.add_annotation(
                text="No data available",
                showarrow=False,
                x=0.5,
                y=0.5
            )
            return fig
        
        fig.add_trace(go.Scatter(
            x=cumulative_returns.index,
            y=cumulative_returns * 100,
            mode='lines',
            name='Cumulative Return',
            line=dict(color='#90EE90', width=3),
            fill='tozeroy',
            fillcolor='rgba(144, 238, 144, 0.2)',
            uid=f'{chart_id}_trace_1'
        ))
        
        fig.add_hline(
            y=0,
            line_dash="dash",
            line_color="#FF6B6B",
            annotation_text="Break-even"
        )
        
        fig.update_layout(
            title="Cumulative Returns Over Time",
            xaxis_title="Date",
            yaxis_title="Cumulative Return (%)",
            hovermode='x unified',
            template='plotly_white',
            height=500,
            font=dict(family="Times New Roman"),
            plot_bgcolor='rgba(173, 216, 230, 0.1)',
            uirevision=chart_id
        )
        
        return fig
    
    def plot_drawdown(self):
        """Plot drawdown from peak"""
        drawdown = self.analyzer.get_drawdown()
        
        fig = go.Figure()
        
        if len(drawdown) == 0:
            fig.add_annotation(
                text="No data available",
                showarrow=False,
                x=0.5,
                y=0.5
            )
            return fig
        
        fig.add_trace(go.Scatter(
            x=drawdown.index,
            y=drawdown * 100,
            mode='lines',
            name='Drawdown',
            line=dict(color='#FF6B6B', width=2),
            fill='tozeroy',
            fillcolor='rgba(255, 107, 107, 0.2)'
        ))
        
        # Add annotation for max drawdown only if data exists
        if len(drawdown) > 0:
            max_dd_idx = drawdown.idxmin()
            max_dd_value = drawdown.min()
            
            fig.add_annotation(
                x=max_dd_idx,
                y=max_dd_value * 100,
                text=f"Max DD: {max_dd_value*100:.2f}%",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor='#FF6B6B'
            )
        
        fig.update_layout(
            title="Drawdown from Peak",
            xaxis_title="Date",
            yaxis_title="Drawdown (%)",
            hovermode='x unified',
            template='plotly_white',
            height=500,
            font=dict(family="Times New Roman"),
            plot_bgcolor='rgba(173, 216, 230, 0.1)',
            yaxis=dict(tickformat='.2%')
        )
        
        return fig
    
    def plot_allocation(self, chart_id="allocation"):
        """Plot portfolio allocation pie chart"""
        composition = self.analyzer.get_composition()
        
        # Extended color palette for any number of stocks
        colors = [
            '#003366', '#004d99', '#0066cc', '#0080ff', '#ADD8E6',
            '#B0E0E6', '#87CEEB', '#6495ED', '#4169E1', '#1E90FF',
            '#1873CC', '#0047AB', '#003D7A', '#002E5F', '#001A3E'
        ]
        
        # Ensure we have enough colors for all stocks
        while len(colors) < len(composition):
            colors.append(f'hsl({len(colors) * 24}, 70%, 50%)')
        
        fig = go.Figure(data=[go.Pie(
            labels=composition['Stock'],
            values=composition['Weight (%)'],
            hovertemplate='<b>%{label}</b><br>Weight: %{value:.2f}%<extra></extra>',
            marker=dict(
                colors=colors[:len(composition)],
                line=dict(color='white', width=2)
            ),
            textposition='inside',
            textinfo='label+percent',
            uid=f'{chart_id}_pie_1'
        )])
        
        fig.update_layout(
            title="Portfolio Allocation",
            height=500,
            font=dict(family="Times New Roman"),
            uirevision=chart_id
        )
        
        return fig
    
    def plot_daily_returns_distribution(self):
        """Plot distribution of daily returns"""
        daily_returns = self.analyzer.get_daily_returns()
        
        fig = go.Figure()
        
        fig.add_trace(go.Histogram(
            x=daily_returns * 100,
            nbinsx=50,
            name='Daily Returns',
            marker=dict(color='#003366', line=dict(color='white', width=1))
        ))
        
        mean_ret = daily_returns.mean() * 100
        fig.add_vline(
            x=mean_ret,
            line_dash="dash",
            line_color="#FFD700",
            annotation_text=f"Mean: {mean_ret:.2f}%"
        )
        
        fig.update_layout(
            title="Daily Returns Distribution",
            xaxis_title="Daily Return (%)",
            yaxis_title="Frequency",
            hovermode='x unified',
            template='plotly_white',
            height=500,
            font=dict(family="Times New Roman")
        )
        
        return fig
    
    def plot_rolling_volatility(self, window=30):
        """Plot rolling volatility"""
        daily_returns = self.analyzer.get_daily_returns()
        rolling_vol = daily_returns.rolling(window).std() * np.sqrt(252) * 100
        
        fig = go.Figure()
        
        if len(rolling_vol) == 0:
            fig.add_annotation(
                text="No data available",
                showarrow=False,
                x=0.5,
                y=0.5
            )
            return fig
        
        fig.add_trace(go.Scatter(
            x=rolling_vol.index,
            y=rolling_vol,
            mode='lines',
            name='Rolling Volatility',
            line=dict(color='#FFD700', width=2),
            fill='tozeroy',
            fillcolor='rgba(255, 215, 0, 0.2)'
        ))
        
        fig.update_layout(
            title=f"{window}-Day Rolling Volatility",
            xaxis_title="Date",
            yaxis_title="Annualized Volatility (%)",
            hovermode='x unified',
            template='plotly_white',
            height=500,
            font=dict(family="Times New Roman"),
            plot_bgcolor='rgba(173, 216, 230, 0.1)'
        )
        
        return fig
    
    def plot_metrics_comparison(self):
        """Plot comparison of key metrics"""
        key_metrics = {
            'Sharpe': self.metrics.get('Sharpe Ratio', 0),
            'Sortino': self.metrics.get('Sortino Ratio', 0),
            'Calmar': self.metrics.get('Calmar Ratio', 0),
            'Info': self.metrics.get('Information Ratio', 0)
        }
        
        fig = go.Figure(data=[
            go.Bar(
                x=list(key_metrics.keys()),
                y=list(key_metrics.values()),
                marker=dict(color='#003366', line=dict(color='white', width=2)),
                text=[f"{v:.3f}" for v in key_metrics.values()],
                textposition='outside',
                hovertemplate='<b>%{x}</b><br>Value: %{y:.3f}<extra></extra>'
            )
        ])
        
        fig.update_layout(
            title="Key Risk-Adjusted Metrics",
            xaxis_title="Metric",
            yaxis_title="Value",
            template='plotly_white',
            height=500,
            font=dict(family="Times New Roman"),
            showlegend=False
        )
        
        return fig
    
    def plot_stock_correlation_heatmap(self):
        """Plot correlation heatmap of portfolio stocks"""
        correlation = self.analyzer.get_correlation_matrix()
        
        fig = go.Figure(data=go.Heatmap(
            z=correlation.values,
            x=correlation.columns,
            y=correlation.columns,
            colorscale='RdYlGn',
            zmid=0,
            text=np.round(correlation.values, 2),
            texttemplate='%{text:.2f}',
            textfont={"size": 10},
            colorbar=dict(title="Correlation")
        ))
        
        fig.update_layout(
            title="Stock Correlation Matrix",
            height=600,
            width=700,
            font=dict(family="Times New Roman")
        )
        
        return fig
    
    def plot_comparison(self, metrics_a, metrics_b):
        """Compare two portfolios side by side"""
        key_metrics = [
            'CAGR', 'Annual Volatility', 'Sharpe Ratio', 
            'Information Ratio', 'Sortino Ratio', 'Max Drawdown'
        ]
        
        values_a = [metrics_a.get(m, 0) for m in key_metrics]
        values_b = [metrics_b.get(m, 0) for m in key_metrics]
        
        fig = make_subplots(
            rows=1, cols=1,
            specs=[[{'type': 'bar'}]]
        )
        
        x = np.arange(len(key_metrics))
        width = 0.35
        
        fig.add_trace(go.Bar(
            x=x,
            y=values_a,
            name='Portfolio A',
            marker=dict(color='#003366'),
            offset=-width/2
        ))
        
        fig.add_trace(go.Bar(
            x=x,
            y=values_b,
            name='Portfolio B',
            marker=dict(color='#FFD700'),
            offset=width/2
        ))
        
        fig.update_layout(
            title="Portfolio A vs Portfolio B",
            xaxis=dict(tickvals=x, ticktext=key_metrics, tickangle=45),
            barmode='group',
            template='plotly_white',
            height=500,
            font=dict(family="Times New Roman"),
            hovermode='x unified'
        )
        
        return fig
