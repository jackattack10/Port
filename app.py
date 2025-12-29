
"""
THE MOUNTAIN PATH - NIFTY PORTFOLIO ANALYZER
Advanced Portfolio Analysis Platform
Prof. V. Ravichandran | 28+ Years Finance Experience | 10+ Years Academic Excellence

Version: 3.0 (Professional Sidebar & Footer)
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
import sys
import os
warnings.filterwarnings('ignore')

# Add modules to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import required packages with error handling
try:
    import plotly.graph_objects as go
    import plotly.express as px
except ImportError:
    st.error("❌ plotly not installed")
    st.stop()

try:
    import yfinance as yf
except ImportError:
    st.error("❌ yfinance not installed")
    st.stop()

# Import custom modules
try:
    from modules.data_fetcher import NiftyDataFetcher
    from modules.portfolio_analyzer import PortfolioAnalyzer
    from modules.metrics_calculator import MetricsCalculator
    from modules.visualizations import PortfolioVisualizer
except ImportError as e:
    st.error(f"❌ Module import error: {str(e)}")
    st.stop()

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Nifty Portfolio Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - Enhanced Design
st.markdown("""
<style>
    * {
        font-family: 'Times New Roman', serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #003366 0%, #004d99 100%);
        padding: 30px;
        border-radius: 10px;
        color: white;
        margin-bottom: 30px;
        text-align: center;
    }
    
    .section-header {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# FOOTER FUNCTIONS
# ============================================================================

def render_professional_footer():
    """Render professional footer with disclaimer and buttons"""
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; padding: 30px 20px;">
    <h3 style="color: #003366; margin: 0 0 15px 0; font-size: 18px; font-weight: 700; letter-spacing: 1px;">
    THE MOUNTAIN PATH - WORLD OF FINANCE
    </h3>
    <p style="color: #555; margin: 0 0 15px 0; font-size: 14px;">
    Advanced Portfolio Analysis Platform with Financial Metrics
    </p>
    <p style="color: #003366; font-weight: 600; margin: 0 0 20px 0;">
    Prof. V. Ravichandran | 28+ Years Finance Experience
    </p>
    <div style="display: flex; justify-content: center; gap: 12px; margin-bottom: 25px; flex-wrap: wrap;">
        <a href="https://www.linkedin.com/in/trichyravis" target="_blank" style="
            background: #0077B5 !important;
            color: #FFFFFF !important;
            padding: 14px 28px !important;
            border-radius: 6px !important;
            text-decoration: none !important;
            font-weight: 900 !important;
            font-size: 15px !important;
            box-shadow: 0 4px 12px rgba(0, 119, 181, 0.7) !important;
            border: none !important;
            cursor: pointer !important;
            display: inline-block !important;
            line-height: 1.2 !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.3) !important;
        ">🔗 LinkedIn Profile</a>
        <a href="https://github.com/trichyravis/nifty-portfolio-analyzer" target="_blank" style="
            background: #333 !important;
            color: #FFFFFF !important;
            padding: 14px 28px !important;
            border-radius: 6px !important;
            text-decoration: none !important;
            font-weight: 900 !important;
            font-size: 15px !important;
            box-shadow: 0 4px 12px rgba(51, 51, 51, 0.7) !important;
            border: none !important;
            cursor: pointer !important;
            display: inline-block !important;
            line-height: 1.2 !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.3) !important;
        ">🐙 GitHub</a>
    </div>
    <p style="color: #666; font-size: 12px; margin: 0 0 10px 0; line-height: 1.6;">
    <strong>Disclaimer:</strong> This tool is for educational purposes. Not financial advice. 
    Always consult with a qualified financial advisor before making investment decisions.
    </p>
    <p style="color: #999; font-size: 11px; margin: 0;">
    📊 Last Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# SIDEBAR SETUP
# ============================================================================

def setup_sidebar():
    """Setup professional sidebar navigation with dark blue background"""
    
    # Professional Dark Blue Sidebar Header
    st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; padding: 20px 15px; border-radius: 8px; margin-bottom: 20px; text-align: left;">
        <h1 style="margin: 0; font-size: 18px; font-weight: 700;">📊 PORTFOLIO ANALYZER</h1>
        <p style="margin: 8px 0 0 0; font-size: 12px; color: #E0E0E0; font-weight: 500;">Advanced Financial Analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Mode Selection Section
    st.sidebar.markdown("<h4 style='color: white; background: #003366; padding: 10px; margin: 0 -16px 10px -16px; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;'>Select Mode:</h4>", unsafe_allow_html=True)
    
    mode = st.sidebar.radio(
        "Mode",
        ["Landing Page", "Portfolio Analysis", "Single Stock Analysis"],
        label_visibility="collapsed"
    )
    
    # Settings Section
    st.sidebar.markdown("<h4 style='color: white; background: #003366; padding: 10px; margin: 10px -16px 10px -16px; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;'>Settings:</h4>", unsafe_allow_html=True)
    
    period = st.sidebar.selectbox(
        "Data Period",
        ["1y", "3y", "5y", "10y"],
        label_visibility="collapsed"
    )
    
    risk_free_rate = st.sidebar.slider(
        "Risk-Free Rate (%)",
        min_value=1.0,
        max_value=8.0,
        value=6.5,
        step=0.1
    )
    
    st.sidebar.markdown("---")
    
    # Creator Section
    st.sidebar.markdown("""
    <div style="background: #003366; color: white; padding: 15px; border-radius: 6px; text-align: center;">
        <h4 style="color: white; margin: 0 0 8px 0; font-size: 13px; font-weight: 600;">Prof. V. Ravichandran</h4>
        <p style="color: #E0E0E0; font-size: 11px; margin: 4px 0; line-height: 1.5;">28+ Years Finance Experience</p>
        <p style="color: #E0E0E0; font-size: 11px; margin: 4px 0 12px 0; line-height: 1.5;">10+ Years Academic Excellence</p>
        <a href="https://www.linkedin.com/in/trichyravis" target="_blank" style="display: inline-block; background: #0077B5; color: #FFFFFF !important; padding: 12px 20px; border-radius: 5px; text-decoration: none !important; font-weight: 900 !important; font-size: 14px !important; box-shadow: 0 4px 12px rgba(0, 119, 181, 0.7); line-height: 1.2; border: none; cursor: pointer; text-shadow: 0 1px 2px rgba(0,0,0,0.3);">🔗 LinkedIn Profile</a>
    </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    st.sidebar.caption("© 2024 Prof. V. Ravichandran")
    
    return mode, period, risk_free_rate / 100

# ============================================================================
# LANDING PAGE
# ============================================================================

def show_landing_page():
    """Professional Landing Page"""
    
    # Main Header
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #003366 0%, #004d99 100%);
        padding: 50px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 40px;
    ">
    <h1 style="margin: 0; font-size: 40px; font-weight: 700;">📊 THE MOUNTAIN PATH</h1>
    <h2 style="margin: 10px 0 0 0; font-size: 28px; font-weight: 600;">Nifty Portfolio Analyzer</h2>
    <p style="margin: 15px 0 0 0; font-size: 16px; color: #E0E0E0;">
    Advanced Financial Analysis Platform
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Features Section
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✨ Core Features
        
        - 📊 **Portfolio Analysis** (A & B Comparison)
        - 📈 **Single Stock Analysis** 
        - 💰 **25+ Financial Metrics**
        - 📊 **Interactive Charts & Visualizations**
        - ⚖️ **Portfolio Comparison & Risk Assessment**
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 Key Metrics
        
        - **Returns:** CAGR, Total Return, Annual/Monthly Return
        - **Risk:** Volatility, Max Drawdown, VaR
        - **Risk-Adjusted:** Sharpe Ratio, Sortino Ratio
        - **Advanced:** Beta, Alpha, Calmar Ratio
        - **And 15+ More Metrics!**
        """)
    
    st.markdown("---")
    
    # Professional Footer
    render_professional_footer()

# ============================================================================
# PORTFOLIO ANALYSIS
# ============================================================================

def show_portfolio_analysis(period, risk_free_rate):
    """Portfolio analysis page"""
    
    st.markdown("""
    <div class="main-header">
        <h1 style="margin: 0;">📊 Portfolio Analysis</h1>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        fetcher = NiftyDataFetcher()
        nifty_stocks = fetcher.get_nifty_50_stocks()
        
        # Initialize tracking for portfolio A
        if 'last_stocks_a_count' not in st.session_state:
            st.session_state.last_stocks_a_count = 0
        if 'last_stocks_b_count' not in st.session_state:
            st.session_state.last_stocks_b_count = 0
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h3 class='section-header'>Portfolio A</h3>", unsafe_allow_html=True)
            stocks_a = st.multiselect(
                "Select stocks for Portfolio A",
                options=nifty_stocks,
                key="stocks_a"
            )
            
            weights_a = {}
            if stocks_a:
                num_stocks_a = len(stocks_a)
                equal_weight_a = 100.0 / num_stocks_a
                
                # Reset weights if number of stocks changed
                if num_stocks_a != st.session_state.last_stocks_a_count:
                    # Clear old weights
                    keys_to_delete = [k for k in st.session_state.keys() if k.startswith("weight_a_")]
                    for k in keys_to_delete:
                        del st.session_state[k]
                    
                    # Initialize new weights
                    for stock in stocks_a:
                        st.session_state[f"weight_a_{stock}"] = equal_weight_a
                    
                    st.session_state.last_stocks_a_count = num_stocks_a
                
                # Display info
                st.info(f"📊 {num_stocks_a} stocks selected → Equal weight: {equal_weight_a:.2f}% each")
                
                # Display weight inputs
                cols = st.columns(num_stocks_a)
                for idx, stock in enumerate(stocks_a):
                    with cols[idx]:
                        weight_key = f"weight_a_{stock}"
                        # Get value from session state
                        current_value = st.session_state.get(weight_key, equal_weight_a)
                        weights_a[stock] = st.number_input(
                            f"{stock}",
                            min_value=0.0,
                            max_value=100.0,
                            value=current_value,
                            step=0.1,
                            key=weight_key,
                            format="%.2f"
                        )
        
        with col2:
            st.markdown("<h3 class='section-header'>Portfolio B</h3>", unsafe_allow_html=True)
            stocks_b = st.multiselect(
                "Select stocks for Portfolio B",
                options=nifty_stocks,
                key="stocks_b"
            )
            
            weights_b = {}
            if stocks_b:
                num_stocks_b = len(stocks_b)
                equal_weight_b = 100.0 / num_stocks_b
                
                # Reset weights if number of stocks changed
                if num_stocks_b != st.session_state.last_stocks_b_count:
                    # Clear old weights
                    keys_to_delete = [k for k in st.session_state.keys() if k.startswith("weight_b_")]
                    for k in keys_to_delete:
                        del st.session_state[k]
                    
                    # Initialize new weights
                    for stock in stocks_b:
                        st.session_state[f"weight_b_{stock}"] = equal_weight_b
                    
                    st.session_state.last_stocks_b_count = num_stocks_b
                
                # Display info
                st.info(f"📊 {num_stocks_b} stocks selected → Equal weight: {equal_weight_b:.2f}% each")
                
                # Display weight inputs
                cols = st.columns(num_stocks_b)
                for idx, stock in enumerate(stocks_b):
                    with cols[idx]:
                        weight_key = f"weight_b_{stock}"
                        # Get value from session state
                        current_value = st.session_state.get(weight_key, equal_weight_b)
                        weights_b[stock] = st.number_input(
                            f"{stock}",
                            min_value=0.0,
                            max_value=100.0,
                            value=current_value,
                            step=0.1,
                            key=weight_key,
                            format="%.2f"
                        )
        
        st.markdown("---")
        
        # Validation function
        def validate_weights(weights, portfolio_name):
            if not weights:
                return True, None
            total = sum(weights.values())
            if abs(total - 100) > 0.01:
                return False, f"❌ {portfolio_name}: Total weight is {total:.2f}%, must be exactly 100%"
            return True, None
        
        # Show weight validation in real-time
        val_col1, val_col2 = st.columns(2)
        
        with val_col1:
            if stocks_a:
                total_a = sum(weights_a.values())
                if abs(total_a - 100) > 0.01:
                    st.warning(f"⚠️ Portfolio A weight: {total_a:.2f}% (should be 100%)")
                else:
                    st.success(f"✅ Portfolio A weight: {total_a:.2f}%")
        
        with val_col2:
            if stocks_b:
                total_b = sum(weights_b.values())
                if abs(total_b - 100) > 0.01:
                    st.warning(f"⚠️ Portfolio B weight: {total_b:.2f}% (should be 100%)")
                else:
                    st.success(f"✅ Portfolio B weight: {total_b:.2f}%")
        
        st.markdown("---")
        
        if st.button("🔍 Analyze Portfolios", use_container_width=True):
            valid_a, error_a = validate_weights(weights_a, "Portfolio A")
            valid_b, error_b = validate_weights(weights_b, "Portfolio B")
            
            if stocks_a and not valid_a:
                st.error(error_a)
                st.stop()
            if stocks_b and not valid_b:
                st.error(error_b)
                st.stop()
            
            with st.spinner("📊 Analyzing portfolios...\n⏳ If rate limited, will auto-retry\n(This may take 2-5 minutes)"):
                try:
                    if stocks_a and weights_a:
                        st.markdown("<h2 class='section-header'>Portfolio A</h2>", unsafe_allow_html=True)
                        try:
                            data_a = fetcher.fetch_stock_data(stocks_a, period)
                            
                            if data_a.empty:
                                st.error(f"❌ No data available for {', '.join(stocks_a)}")
                            else:
                                analyzer_a = PortfolioAnalyzer(stocks_a, weights_a, data_a)
                                metrics_a = MetricsCalculator(data_a, analyzer_a, risk_free_rate).calculate_all_metrics()
                                
                                display_metrics(metrics_a)
                                
                                visualizer = PortfolioVisualizer(data_a, analyzer_a, metrics_a)
                                col1, col2 = st.columns(2)
                                with col1:
                                    try:
                                        st.plotly_chart(visualizer.plot_portfolio_value(chart_id="portfolio_a_value"), use_container_width=True, key="portfolio_a_value")
                                    except Exception as e:
                                        st.warning(f"⚠️ Chart error: {str(e)}")
                                
                                with col2:
                                    try:
                                        st.plotly_chart(visualizer.plot_allocation(chart_id="portfolio_a_allocation"), use_container_width=True, key="portfolio_a_allocation")
                                    except Exception as e:
                                        st.warning(f"⚠️ Chart error: {str(e)}")
                                
                                st.success("✅ Portfolio A analysis complete!")
                        except Exception as e:
                            st.error(f"❌ Error: {str(e)}")
                    
                    if stocks_b and weights_b:
                        st.markdown("<h2 class='section-header'>Portfolio B</h2>", unsafe_allow_html=True)
                        try:
                            data_b = fetcher.fetch_stock_data(stocks_b, period)
                            
                            if data_b.empty:
                                st.error(f"❌ No data available for {', '.join(stocks_b)}")
                            else:
                                analyzer_b = PortfolioAnalyzer(stocks_b, weights_b, data_b)
                                metrics_b = MetricsCalculator(data_b, analyzer_b, risk_free_rate).calculate_all_metrics()
                                
                                display_metrics(metrics_b)
                                
                                visualizer = PortfolioVisualizer(data_b, analyzer_b, metrics_b)
                                col1, col2 = st.columns(2)
                                with col1:
                                    try:
                                        st.plotly_chart(visualizer.plot_portfolio_value(chart_id="portfolio_b_value"), use_container_width=True, key="portfolio_b_value")
                                    except Exception as e:
                                        st.warning(f"⚠️ Chart error: {str(e)}")
                                
                                with col2:
                                    try:
                                        st.plotly_chart(visualizer.plot_allocation(chart_id="portfolio_b_allocation"), use_container_width=True, key="portfolio_b_allocation")
                                    except Exception as e:
                                        st.warning(f"⚠️ Chart error: {str(e)}")
                                
                                # Portfolio Comparison Analysis
        st.markdown("---")
        st.markdown("<h2 class='section-header'>📊 Portfolio Comparison Analysis</h2>", unsafe_allow_html=True)
        
        # Create comparison dataframe
        comparison_data = {
            'Metric': [
                'CAGR',
                'Total Return',
                'Annual Volatility',
                'Sharpe Ratio',
                'Sortino Ratio',
                'Information Ratio',
                'Calmar Ratio',
                'Max Drawdown',
                'Value at Risk (VaR)',
                'Skewness'
            ],
            'Portfolio A': [
                f"{metrics_a.get('CAGR', 0)*100:.2f}%",
                f"{metrics_a.get('Total Return', 0)*100:.2f}%",
                f"{metrics_a.get('Annual Volatility', 0)*100:.2f}%",
                f"{metrics_a.get('Sharpe Ratio', 0):.3f}",
                f"{metrics_a.get('Sortino Ratio', 0):.3f}",
                f"{metrics_a.get('Information Ratio', 0):.3f}",
                f"{metrics_a.get('Calmar Ratio', 0):.3f}",
                f"{metrics_a.get('Max Drawdown', 0)*100:.2f}%",
                f"{metrics_a.get('Value at Risk', 0)*100:.2f}%",
                f"{metrics_a.get('Skewness', 0):.3f}"
            ],
            'Portfolio B': [
                f"{metrics_b.get('CAGR', 0)*100:.2f}%",
                f"{metrics_b.get('Total Return', 0)*100:.2f}%",
                f"{metrics_b.get('Annual Volatility', 0)*100:.2f}%",
                f"{metrics_b.get('Sharpe Ratio', 0):.3f}",
                f"{metrics_b.get('Sortino Ratio', 0):.3f}",
                f"{metrics_b.get('Information Ratio', 0):.3f}",
                f"{metrics_b.get('Calmar Ratio', 0):.3f}",
                f"{metrics_b.get('Max Drawdown', 0)*100:.2f}%",
                f"{metrics_b.get('Value at Risk', 0)*100:.2f}%",
                f"{metrics_b.get('Skewness', 0):.3f}"
            ]
        }
        
        comparison_df = pd.DataFrame(comparison_data)
        
        # Display comparison table
        st.subheader("📈 Metrics Comparison")
        st.dataframe(comparison_df, use_container_width=True)
        
        # Generate Analysis Summary
        st.subheader("📋 Analysis Summary")
        
        # Compare CAGR
        cagr_a = metrics_a.get('CAGR', 0)
        cagr_b = metrics_b.get('CAGR', 0)
        cagr_winner = "Portfolio A" if cagr_a > cagr_b else "Portfolio B" if cagr_b > cagr_a else "Equal"
        cagr_diff = abs(cagr_a - cagr_b) * 100
        
        # Compare Volatility
        vol_a = metrics_a.get('Annual Volatility', 0)
        vol_b = metrics_b.get('Annual Volatility', 0)
        vol_lower = "Portfolio A" if vol_a < vol_b else "Portfolio B" if vol_b < vol_a else "Equal"
        vol_diff = abs(vol_a - vol_b) * 100
        
        # Compare Sharpe Ratio
        sharpe_a = metrics_a.get('Sharpe Ratio', 0)
        sharpe_b = metrics_b.get('Sharpe Ratio', 0)
        sharpe_winner = "Portfolio A" if sharpe_a > sharpe_b else "Portfolio B" if sharpe_b > sharpe_a else "Equal"
        
        # Compare Max Drawdown
        dd_a = metrics_a.get('Max Drawdown', 0)
        dd_b = metrics_b.get('Max Drawdown', 0)
        dd_better = "Portfolio A" if dd_a > dd_b else "Portfolio B" if dd_b > dd_a else "Equal"
        dd_diff = abs(dd_a - dd_b) * 100
        
        # Create summary columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📊 Return Analysis")
            st.markdown(f"""
            **CAGR Winner:** {cagr_winner}
            - Difference: {cagr_diff:.2f}%
            - Portfolio A: {cagr_a*100:.2f}%
            - Portfolio B: {cagr_b*100:.2f}%
            
            **Interpretation:** CAGR (Compound Annual Growth Rate) shows average yearly returns.
            Higher CAGR means better long-term growth.
            """)
        
        with col2:
            st.markdown("#### 📈 Risk Analysis")
            st.markdown(f"""
            **Lower Volatility:** {vol_lower}
            - Difference: {vol_diff:.2f}%
            - Portfolio A: {vol_a*100:.2f}%
            - Portfolio B: {vol_b*100:.2f}%
            
            **Interpretation:** Volatility measures price fluctuations.
            Lower volatility means more stable returns.
            """)
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown("#### ⚖️ Risk-Adjusted Returns")
            st.markdown(f"""
            **Better Sharpe Ratio:** {sharpe_winner}
            - Portfolio A: {sharpe_a:.3f}
            - Portfolio B: {sharpe_b:.3f}
            
            **Interpretation:** Sharpe Ratio measures returns per unit of risk.
            Higher is better. >1 is excellent, >2 is exceptional.
            """)
        
        with col4:
            st.markdown("#### 📉 Drawdown Analysis")
            st.markdown(f"""
            **Better Max Drawdown:** {dd_better}
            - Difference: {dd_diff:.2f}%
            - Portfolio A: {dd_a*100:.2f}%
            - Portfolio B: {dd_b*100:.2f}%
            
            **Interpretation:** Max Drawdown is peak-to-trough decline.
            Less negative (closer to 0) is better. Shows worst-case loss.
            """)
        
        # Overall Recommendation
        st.markdown("---")
        st.subheader("🎯 Overall Assessment")
        
        # Scoring system
        score_a = 0
        score_b = 0
        
        if cagr_a > cagr_b:
            score_a += 1
        elif cagr_b > cagr_a:
            score_b += 1
        
        if vol_a < vol_b:
            score_a += 1
        elif vol_b < vol_a:
            score_b += 1
        
        if sharpe_a > sharpe_b:
            score_a += 1
        elif sharpe_b > sharpe_a:
            score_b += 1
        
        if dd_a > dd_b:
            score_a += 1
        elif dd_b > dd_a:
            score_b += 1
        
        total_score = max(score_a, score_b)
        
        if score_a > score_b:
            winner = "Portfolio A"
            winner_score = score_a
            loser_score = score_b
        elif score_b > score_a:
            winner = "Portfolio B"
            winner_score = score_b
            loser_score = score_a
        else:
            winner = "Both"
            winner_score = score_a
            loser_score = score_b
        
        st.markdown(f"""
        ### {winner} Wins! ({winner_score}/{total_score} metrics)
        
        **Metric Scores:**
        - Portfolio A: {score_a}/{total_score}
        - Portfolio B: {score_b}/{total_score}
        
        **Key Strengths:**
        """)
        
        if score_a > score_b:
            st.success(f"✅ Portfolio A is stronger across more metrics")
            st.markdown(f"""
            - Better return potential (CAGR: {cagr_a*100:.2f}%)
            - Risk-adjusted returns favorable
            - Use when: You prioritize growth with acceptable risk
            """)
        elif score_b > score_a:
            st.success(f"✅ Portfolio B is stronger across more metrics")
            st.markdown(f"""
            - Better return potential (CAGR: {cagr_b*100:.2f}%)
            - Risk-adjusted returns favorable
            - Use when: You prioritize growth with acceptable risk
            """)
        else:
            st.info(f"✅ Both portfolios are balanced")
            st.markdown(f"""
            - Choose based on your specific goals
            - Portfolio A: Focus on specific metrics
            - Portfolio B: Alternative approach
            """)
        
        # Detailed Insights
        st.markdown("---")
        st.subheader("💡 Detailed Insights")
        
        insight_col1, insight_col2 = st.columns(2)
        
        with insight_col1:
            st.markdown("#### Portfolio A Details")
            st.markdown(f"""
            **Growth Profile:**
            - Annual Return: {metrics_a.get('Annual Return', 0)*100:.2f}%
            - Total Return: {metrics_a.get('Total Return', 0)*100:.2f}%
            
            **Risk Metrics:**
            - Volatility: {metrics_a.get('Annual Volatility', 0)*100:.2f}%
            - Max Drawdown: {metrics_a.get('Max Drawdown', 0)*100:.2f}%
            - Value at Risk: {metrics_a.get('Value at Risk', 0)*100:.2f}%
            
            **Quality Scores:**
            - Sharpe Ratio: {metrics_a.get('Sharpe Ratio', 0):.3f}
            - Sortino Ratio: {metrics_a.get('Sortino Ratio', 0):.3f}
            - Information Ratio: {metrics_a.get('Information Ratio', 0):.3f}
            - Calmar Ratio: {metrics_a.get('Calmar Ratio', 0):.3f}
            """)
        
        with insight_col2:
            st.markdown("#### Portfolio B Details")
            st.markdown(f"""
            **Growth Profile:**
            - Annual Return: {metrics_b.get('Annual Return', 0)*100:.2f}%
            - Total Return: {metrics_b.get('Total Return', 0)*100:.2f}%
            
            **Risk Metrics:**
            - Volatility: {metrics_b.get('Annual Volatility', 0)*100:.2f}%
            - Max Drawdown: {metrics_b.get('Max Drawdown', 0)*100:.2f}%
            - Value at Risk: {metrics_b.get('Value at Risk', 0)*100:.2f}%
            
            **Quality Scores:**
            - Sharpe Ratio: {metrics_b.get('Sharpe Ratio', 0):.3f}
            - Sortino Ratio: {metrics_b.get('Sortino Ratio', 0):.3f}
            - Information Ratio: {metrics_b.get('Information Ratio', 0):.3f}
            - Calmar Ratio: {metrics_b.get('Calmar Ratio', 0):.3f}
            """)
        
        # Recommendation
        st.markdown("---")
        st.subheader("📌 Recommendation")
        
        if cagr_a >= cagr_b and sharpe_a >= sharpe_b:
            st.success("✅ Portfolio A: Better for Growth + Risk-Adjusted Returns")
        elif cagr_b >= cagr_a and sharpe_b >= sharpe_a:
            st.success("✅ Portfolio B: Better for Growth + Risk-Adjusted Returns")
        elif cagr_a > cagr_b:
            st.info("📊 Portfolio A: Higher Growth (but check risk metrics)")
        elif cagr_b > cagr_a:
            st.info("📊 Portfolio B: Higher Growth (but check risk metrics)")
        else:
            st.info("⚖️ Comparable Performance: Choose based on your preference")
                        except Exception as e:
                            st.error(f"❌ Error: {str(e)}")
                
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    except Exception as e:
        st.error(f"Error: {str(e)}")

def display_metrics(metrics):
    """Display metrics"""
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("CAGR", f"{metrics.get('CAGR', 0)*100:.2f}%")
    with col2:
        st.metric("Total Return", f"{metrics.get('Total Return', 0)*100:.2f}%")
    with col3:
        st.metric("Volatility", f"{metrics.get('Annual Volatility', 0)*100:.2f}%")
    with col4:
        st.metric("Max Drawdown", f"{metrics.get('Max Drawdown', 0)*100:.2f}%")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Sharpe Ratio", f"{metrics.get('Sharpe Ratio', 0):.3f}")
    with col2:
        st.metric("Sortino Ratio", f"{metrics.get('Sortino Ratio', 0):.3f}")
    with col3:
        st.metric("Information Ratio", f"{metrics.get('Information Ratio', 0):.3f}")
    with col4:
        st.metric("Calmar Ratio", f"{metrics.get('Calmar Ratio', 0):.3f}")

# ============================================================================
# SINGLE STOCK ANALYSIS
# ============================================================================

def show_single_stock_analysis(period, risk_free_rate):
    """Single stock analysis"""
    
    st.markdown("""
    <div class="main-header">
        <h1 style="margin: 0;">📈 Single Stock Analysis</h1>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        fetcher = NiftyDataFetcher()
        nifty_stocks = fetcher.get_nifty_50_stocks()
        
        selected_stock = st.selectbox("Select Stock", options=nifty_stocks)
        
        if st.button("🔍 Analyze", use_container_width=True):
            with st.spinner(f"Analyzing {selected_stock}..."):
                data = fetcher.fetch_stock_data([selected_stock], period)
                analyzer = PortfolioAnalyzer([selected_stock], {selected_stock: 100}, data)
                metrics = MetricsCalculator(data, analyzer, risk_free_rate).calculate_all_metrics()
                
                display_metrics(metrics)
                
                visualizer = PortfolioVisualizer(data, analyzer, metrics)
                col1, col2 = st.columns(2)
                with col1:
                    st.plotly_chart(visualizer.plot_portfolio_value(chart_id=f"single_stock_{selected_stock}_value"), use_container_width=True, key=f"single_stock_{selected_stock}_value")
                with col2:
                    st.plotly_chart(visualizer.plot_cumulative_returns(chart_id=f"single_stock_{selected_stock}_returns"), use_container_width=True, key=f"single_stock_{selected_stock}_returns")
                
                st.success("✅ Analysis complete!")
    
    except Exception as e:
        st.error(f"Error: {str(e)}")

# ============================================================================
# MAIN
# ============================================================================

def main():
    mode, period, risk_free_rate = setup_sidebar()
    
    if mode == "Landing Page":
        show_landing_page()
    elif mode == "Portfolio Analysis":
        show_portfolio_analysis(period, risk_free_rate)
    elif mode == "Single Stock Analysis":
        show_single_stock_analysis(period, risk_free_rate)

if __name__ == "__main__":
    main()
