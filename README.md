# 📊 Nifty Portfolio Analyzer

**Advanced Portfolio Analysis Platform** using Streamlit and Financial Data from Yahoo Finance

Built by **Prof. V. Ravichandran** | 28+ Years Corporate Finance & Banking | 10+ Years Academic Excellence

---

## 🎯 Features

✅ **Dynamic Portfolio Creation**
- Create and compare Portfolio A & B
- Select from Nifty 50 stocks
- Custom weight allocation
- Real-time data updates

✅ **Comprehensive Analysis**
- 25+ Financial Metrics
- Performance analysis
- Risk evaluation
- Comparative analysis

✅ **Interactive Visualizations**
- Portfolio value charts
- Drawdown analysis
- Allocation pie charts
- Cumulative returns
- Distribution charts

✅ **Financial Metrics**
- CAGR (Compound Annual Growth Rate)
- Total Returns
- Sharpe Ratio
- Sortino Ratio
- Information Ratio
- Calmar Ratio
- Maximum Drawdown
- Ulcer Index
- Tracking Error
- Beta & Alpha
- And 15+ more!

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/nifty-portfolio-analyzer.git
cd nifty-portfolio-analyzer

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

Opens at: `http://localhost:8501`

---

## 📋 Requirements

Python 3.8+

### Key Dependencies
- **streamlit** - Web framework
- **plotly** - Interactive charts
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **yfinance** - Stock data
- **scipy** - Scientific computing
- **scikit-learn** - Machine learning

See `requirements.txt` for complete list.

---

## 📁 Project Structure

```
nifty-portfolio-analyzer/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .gitignore               # Git ignore rules
└── modules/
    ├── data_fetcher.py      # Yahoo Finance data fetching
    ├── portfolio_analyzer.py # Portfolio calculations
    ├── metrics_calculator.py # 25+ financial metrics
    └── visualizations.py    # Interactive Plotly charts
```

---

## 💡 Usage

### 1. Landing Page
Overview of features and framework

### 2. Portfolio Analysis
- Select stocks from Nifty 50
- Set portfolio weights
- View comprehensive metrics
- Compare Portfolio A & B

### 3. Single Stock Analysis
- Analyze individual stocks
- View historical performance
- Calculate metrics

---

## 📊 Key Metrics Explained

### Performance
- **CAGR** - Compound Annual Growth Rate (%)
- **Total Return** - Overall gain/loss (%)
- **Annual Return** - Yearly average return (%)

### Risk-Adjusted
- **Sharpe Ratio** - Return per unit of risk
- **Sortino Ratio** - Return per unit of downside risk
- **Information Ratio** - Active management skill
- **Calmar Ratio** - Return relative to max drawdown

### Risk
- **Volatility** - Standard deviation of returns (%)
- **Max Drawdown** - Worst peak-to-trough decline (%)
- **Ulcer Index** - Drawdown severity measure
- **Tracking Error** - Active return volatility (%)

### Market
- **Beta** - Market sensitivity (1.0 = market)
- **Alpha** - Excess return vs benchmark (%)

---

## 🌐 Live Demo

Deploy to Streamlit Cloud:

```bash
# Push to GitHub
git add .
git commit -m "Initial commit"
git push origin main

# Go to share.streamlit.io
# Connect GitHub account
# Select repository
# Deploy!
```

---

## 👨‍🏫 About Creator

**Prof. V. Ravichandran**
- 28+ Years Corporate Finance & Banking Experience
- 10+ Years Academic Excellence
- Expertise in Portfolio Management, Risk Management, Fixed Income, Investment Banking
- Creator of "The Mountain Path - World of Finance" educational platform

---

## 📝 License

MIT License - Feel free to use and modify

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📧 Support

For questions or issues, please create an issue on GitHub.

---

## 🎓 Educational Use

Perfect for:
- MBA Portfolio Management courses
- CFA/FRM candidate practice
- Finance professionals
- Individual investors
- Financial analysis projects

---

**Made with ❤️ by Prof. V. Ravichandran**

*"The Mountain Path to Financial Excellence"*
