
# 📊 The Mountain Path - Nifty Portfolio Analyzer

## 📚 Documentation

Welcome to the comprehensive documentation for the **Nifty Portfolio Analyzer**, a professional financial analysis platform for portfolio and stock analysis.

---

## 📖 Quick Navigation

1. **[Getting Started](#getting-started)** - Setup and installation
2. **[Features](#features)** - What the app can do
3. **[User Guide](#user-guide)** - How to use the app
4. **[Technical Details](#technical-details)** - Architecture and implementation
5. **[Metrics Explained](#metrics-explained)** - Understanding the calculations
6. **[Mode Selector Design](#mode-selector-design)** - UI/UX details
7. **[LinkedIn Integration](#linkedin-integration)** - Profile information
8. **[Troubleshooting](#troubleshooting)** - Common issues and solutions

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Streamlit
- Dependencies: pandas, numpy, yfinance, plotly, scipy, scikit-learn

### Installation

```bash
# Clone the repository
git clone https://github.com/trichydavis/nifty-portfolio-analyzer.git
cd nifty-portfolio-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Live Deployment

Access the live app at: **https://themountainpathportfolioanalyzer.streamlit.app**

---

## ✨ Features

### Core Functionality

#### 1️⃣ **Portfolio Analysis (A & B Comparison)**
- Select up to 50 Nifty stocks for each portfolio
- Allocate weights (must sum to 100%)
- Real-time weight validation
- Compare performance metrics side-by-side
- Interactive visualizations

#### 2️⃣ **Single Stock Analysis**
- Analyze individual stock performance
- Historical price trends
- Risk metrics
- Performance indicators
- Volatility analysis

#### 3️⃣ **25+ Financial Metrics**
Calculate comprehensive metrics including:
- **Returns:** CAGR, Total Return, Annual Return, Monthly Return
- **Risk:** Volatility (Daily, Monthly, Annual), Max Drawdown, Sharpe Ratio, Sortino Ratio
- **Advanced:** Beta, Alpha, Information Ratio, Calmar Ratio
- **Statistical:** Skewness, Kurtosis, Value at Risk (VaR), Conditional VaR
- **Portfolio:** Ulcer Index, Tracking Error, Profit Factor, Win Rate

#### 4️⃣ **Interactive Charts**
- Portfolio Value Over Time (with annotations)
- Cumulative Returns
- Drawdown Analysis
- Rolling Volatility
- Portfolio Allocation (Pie Chart)
- Correlation Matrix Heatmap

#### 5️⃣ **Data Accuracy**
- Real-time data from Yahoo Finance
- Historical data support (1y, 3y, 5y, 10y)
- NSE stocks (.NS suffix)
- Rate limit handling with automatic retries

---

## 📖 User Guide

### Landing Page
- Overview of features
- Creator information
- LinkedIn profile link
- Direct access to analysis modes

### Portfolio Analysis Mode

#### Step 1: Select Stocks
1. Click "Portfolio Analysis" in the sidebar
2. Choose data period (1y, 3y, 5y, 10y)
3. Set risk-free rate (default 6.5%)
4. Select stocks from Nifty 50 list

#### Step 2: Allocate Weights
- Enter weights for each stock
- Weights automatically displayed as percentage
- **Real-time validation:** Total weight must = 100%
- Visual feedback: ✅ Green (100%) or ⚠️ Yellow (not 100%)

#### Step 3: Analyze
1. Click "🔍 Analyze Portfolios" button
2. Wait for data fetch (may take 30 seconds if rate limited)
3. View comprehensive metrics
4. Interactive charts and visualizations

#### Step 4: Interpret Results
- Compare Sharpe Ratio between portfolios
- Analyze max drawdown and volatility
- Review cumulative returns
- Examine portfolio allocation

### Single Stock Analysis Mode
1. Select a single stock
2. Choose time period
3. View performance metrics
4. Analyze price trends and volatility

---

## 🔧 Technical Details

### Architecture

```
app.py (Main Application)
├── LinkedIn Integration Functions
├── Sidebar Setup
├── Landing Page
├── Portfolio Analysis
├── Single Stock Analysis
└── Main Entry Point

modules/
├── data_fetcher.py (Yahoo Finance API)
├── portfolio_analyzer.py (Calculations)
├── metrics_calculator.py (Metrics)
└── visualizations.py (Charts)
```

### Data Flow

```
User Input → Data Fetcher (yfinance) → Portfolio Analyzer 
→ Metrics Calculator → Visualizations → Display Results
```

### Stock List (Nifty 50)

50 verified NSE stocks including:
- RELIANCE, TCS, HDFCBANK, ICICIBANK
- HINDUNILVR, SBIN, BHARTIARTL, ITC
- WIPRO, INFY, TECHM, AXISBANK
- And 38+ more...

---

## 📊 Metrics Explained

### Returns Metrics

**CAGR (Compound Annual Growth Rate)**
```
CAGR = (Ending Value / Beginning Value)^(1/Years) - 1
```
- Shows average annual growth
- Accounts for compounding

**Total Return**
```
Total Return = (Ending Value - Beginning Value) / Beginning Value
```
- Simple percentage gain/loss

**Sharpe Ratio**
```
Sharpe Ratio = (Portfolio Return - Risk-Free Rate) / Volatility
```
- Risk-adjusted return
- Higher is better (> 1.0 is good)

### Risk Metrics

**Volatility (Standard Deviation)**
```
Annualized Volatility = Daily Volatility × √252
```
- 252 = trading days per year
- Higher = more risky

**Maximum Drawdown**
```
Max DD = (Peak Value - Trough Value) / Peak Value
```
- Worst loss from peak
- Negative value

**Sortino Ratio**
```
Sortino Ratio = (Return - Risk-Free Rate) / Downside Deviation
```
- Like Sharpe but only penalizes downside
- Better risk-reward indicator

### Advanced Metrics

**Beta**
- Volatility relative to market
- Beta = 1.0 means moves with market
- Beta > 1.0 means more volatile

**Alpha**
- Excess return above market
- Positive alpha = outperformance

**Value at Risk (VaR)**
- Worst expected loss at confidence level
- e.g., 95% VaR = worst loss in 95% of days

**Calmar Ratio**
```
Calmar Ratio = Annual Return / Max Drawdown
```
- Return per unit of risk
- Higher is better

---

## 🎨 Mode Selector Design

### Design Specifications

**Color Palette:**
- Primary: `#003366` (Dark Blue)
- Secondary: `#004d99` (Medium Blue)
- Accent: `#FFD700` (Gold)

**Typography:**
- Title: 18px, Font-weight 600, White
- Options: 15px, Font-weight 500, White

**Spacing:**
- Container: 25px padding, 15px border-radius
- Options: 12px padding, 8px gap
- Margins: 20px top/bottom

**Animations:**
- Hover: Background opacity +10%, gold border, 5px translate
- Active: Gold glow effect, 0.1 alpha overlay

### Implementation

The mode selector is implemented in `app.py` using:
- Streamlit radio buttons
- Custom CSS styling
- HTML/markdown rendering
- Professional gradient backgrounds

---

## 🔗 LinkedIn Integration

### Creator Information

**Name:** Prof. V. Ravichandran
- **LinkedIn:** https://www.linkedin.com/in/trichyravis
- **Experience:** 28+ Years Corporate Finance & Banking
- **Academic:** 10+ Years Academic Excellence

### LinkedIn Components

The app includes three LinkedIn integration options:

1. **Sidebar Component** (Always Visible)
   - Compact profile card
   - LinkedIn button
   - Available in sidebar

2. **Footer Component** (Landing Page)
   - Professional footer with details
   - Direct LinkedIn connection button
   - Styling matches app theme

3. **Simple Button**
   - Minimal LinkedIn button
   - Can be used anywhere in app
   - Flexible placement

### Styling

- Gradient blue background (#0077B5 → #005885)
- White text
- Smooth hover animations
- Professional appearance
- Mobile responsive

---

## 🎯 How to Use the App

### For MBA/CFA Students

1. **Learn Portfolio Management**
   - Create two different portfolios
   - Compare metrics
   - Understand risk-adjusted returns

2. **Analyze Individual Stocks**
   - Study single stock performance
   - Calculate financial metrics
   - Understand volatility and drawdowns

3. **Practice Allocation**
   - Allocate weights to stocks
   - Validate your portfolio weights
   - Analyze the impact on returns

### For Financial Professionals

1. **Portfolio Benchmarking**
   - Compare your portfolio vs alternatives
   - Analyze Sharpe and Sortino ratios
   - Review maximum drawdown

2. **Risk Assessment**
   - Calculate VaR and CVaR
   - Analyze correlation between stocks
   - Understand portfolio concentration

3. **Performance Analysis**
   - CAGR vs market benchmarks
   - Alpha and Beta calculations
   - Tracking error analysis

---

## ⚙️ Configuration

### Settings Available

**Data Period**
- 1y, 3y, 5y, 10y
- Select from sidebar

**Risk-Free Rate**
- Default: 6.5%
- Adjustable from 1% to 8%
- Affects Sharpe and Sortino calculations

**Stocks**
- Choose from 50 Nifty stocks
- Multi-select for portfolios
- Real-time data from Yahoo Finance

---

## 🐛 Troubleshooting

### Common Issues

#### Issue 1: "Rate Limited Error"
**Problem:** Yahoo Finance rate limiting
**Solution:** 
- Wait 1-2 minutes
- App auto-retries with exponential backoff
- Try again with different stocks

#### Issue 2: "Weight Validation Error"
**Problem:** Portfolio weights don't sum to 100%
**Solution:**
- Check weight values
- Adjust manually to reach 100%
- Visual indicator shows current total

#### Issue 3: "No Data Available"
**Problem:** Stock has no data for period
**Solution:**
- Choose different time period
- Try another stock
- Use stocks from Nifty 50 list

#### Issue 4: "Chart Not Displaying"
**Problem:** Visualization error
**Solution:**
- Ensure 2+ stocks selected
- Wait for data to load
- Refresh the page

### Performance Tips

1. **Start with Shorter Periods**
   - 1y before 5y
   - Faster data fetch

2. **Use Fewer Stocks**
   - 2-3 stocks first
   - Then expand

3. **Avoid Peak Times**
   - Market closing times can be slow
   - Use during off-market hours

4. **Clear Cache**
   - Hard refresh (Ctrl+F5)
   - Clear browser cache

---

## 📞 Support & Contact

### For Questions About:

**App Usage:** Check this documentation
**Features:** Review the Features section above
**Financial Metrics:** See Metrics Explained section
**Technical Issues:** Check Troubleshooting section

### Creator Contact

**Prof. V. Ravichandran**
- **LinkedIn:** https://www.linkedin.com/in/trichyravis
- **Experience:** 28+ Years Finance & Banking
- **Academic:** 10+ Years Excellence

### Repository

- **GitHub:** https://github.com/trichydavis/nifty-portfolio-analyzer
- **Live App:** https://themountainpathportfolioanalyzer.streamlit.app

---

## 📝 Version History

### Version 1.0 (Current)
- ✅ Portfolio Analysis (A & B)
- ✅ Single Stock Analysis
- ✅ 25+ Financial Metrics
- ✅ Interactive Charts
- ✅ Nifty 50 Stock Support
- ✅ Weight Validation
- ✅ Rate Limiting Handling
- ✅ LinkedIn Integration
- ✅ Professional UI/UX

---

## 📜 License & Credits

**Created By:** Prof. V. Ravichandran
**The Mountain Path - World of Finance**
**© 2024**

---

## 🔐 Data Privacy

- Uses Yahoo Finance public data
- No personal data stored
- No authentication required
- Real-time market data only

---

## 🙏 Acknowledgments

- **Yahoo Finance** for stock data
- **Streamlit** for the web framework
- **Plotly** for interactive visualizations
- **NumPy & Pandas** for calculations
- **SciPy** for statistical functions

---

**Last Updated:** December 29, 2024
**Status:** Production Ready ✅
