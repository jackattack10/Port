# 📊 Financial Metrics Explained

## Complete Guide to All Metrics in the Nifty Portfolio Analyzer

This document explains each metric calculated by the app in detail.

---

## 📈 Returns & Performance Metrics

### CAGR (Compound Annual Growth Rate)

**Formula:**
```
CAGR = (Ending Value / Beginning Value)^(1/Years) - 1
```

**Interpretation:**
- Average annual growth rate
- Accounts for compounding
- Better than simple average for multi-year periods

**Example:**
- Investment: ₹100,000
- After 5 years: ₹150,000
- CAGR = (150,000/100,000)^(1/5) - 1 = 8.45%

**Good Range:** 10-15% annually is excellent

---

### Total Return

**Formula:**
```
Total Return = (Ending Value - Beginning Value) / Beginning Value
```

**Interpretation:**
- Simple percentage gain/loss
- Not annualized
- Total return over the period

**Example:**
- Buy at ₹100
- Sell at ₹130
- Total Return = (130-100)/100 = 30%

**Good Range:** Depends on holding period

---

### Annual Return

**Formula:**
```
Annual Return = (Cumulative Daily Returns)^(252) - 1
```

**Interpretation:**
- Average annual return
- Based on daily returns
- Annualized from daily data

**Note:** 252 = trading days per year

---

### Monthly Return

**Formula:**
```
Monthly Return = (Cumulative Daily Returns)^(21) - 1
```

**Interpretation:**
- Average monthly return
- Based on daily returns
- Annualized to monthly scale

**Note:** 21 = trading days per month (approximately)

---

## 📉 Risk Metrics

### Volatility (Standard Deviation)

**Formula:**
```
Daily Volatility = Standard Deviation of daily returns
Annualized Volatility = Daily Volatility × √252
```

**Interpretation:**
- Measures price fluctuation
- Higher = more risky
- Standard measure of risk

**Ranges:**
- < 10%: Low volatility
- 10-20%: Moderate volatility
- > 20%: High volatility

**Example:**
- Daily volatility: 1.1%
- Annualized: 1.1% × √252 = 17.5%

---

### Maximum Drawdown

**Formula:**
```
Max Drawdown = (Peak Price - Lowest Price) / Peak Price
```

**Interpretation:**
- Worst loss from peak
- Negative percentage
- Important for risk assessment

**Example:**
- Peak: ₹100
- Lowest: ₹75
- Max DD = (100-75)/100 = -25%

**Interpretation:** Lost 25% from peak

---

### Average Drawdown

**Formula:**
```
Average DD = Average of all peak-to-trough declines
```

**Interpretation:**
- Average magnitude of declines
- Less extreme than max drawdown
- Better for understanding typical losses

---

### Drawdown Duration

**Interpretation:**
- Number of days from peak to recovery
- Time to recover from losses
- Measure of recovery speed

**Example:**
- If max drawdown lasted 120 days
- Took 4 months to recover

---

## 📊 Risk-Adjusted Performance Metrics

### Sharpe Ratio

**Formula:**
```
Sharpe Ratio = (Portfolio Return - Risk-Free Rate) / Standard Deviation
```

**Interpretation:**
- Risk-adjusted return
- How much return per unit of risk
- Higher is better

**Benchmarks:**
- < 0.5: Poor
- 0.5 - 1.0: Average
- 1.0 - 2.0: Good
- > 2.0: Excellent

**Example:**
- Return: 12%, Risk-Free: 6.5%, Volatility: 15%
- Sharpe = (12-6.5)/15 = 0.367

---

### Sortino Ratio

**Formula:**
```
Sortino Ratio = (Portfolio Return - Risk-Free Rate) / Downside Deviation
```

**Interpretation:**
- Like Sharpe but only penalizes downside
- Better risk-reward indicator
- Ignores upside volatility

**Advantage over Sharpe:**
- Only counts negative volatility
- More realistic for investors
- Better for strategy evaluation

**Benchmarks:**
- > 1.0: Good
- > 2.0: Very good
- > 3.0: Excellent

---

### Calmar Ratio

**Formula:**
```
Calmar Ratio = Annual Return / Max Drawdown (absolute value)
```

**Interpretation:**
- Return relative to risk
- Higher return per unit of drawdown
- Good for comparing strategies

**Example:**
- Annual Return: 15%
- Max Drawdown: 20%
- Calmar = 15/20 = 0.75

---

### Information Ratio

**Formula:**
```
Information Ratio = (Portfolio Return - Benchmark Return) / Tracking Error
```

**Interpretation:**
- Excess return relative to benchmark
- Adjusted for tracking error
- Measures alpha generation

**Note:** In this app, calculated against mean returns

---

## 📈 Market Metrics

### Beta

**Formula:**
```
Beta = Covariance(Portfolio Returns, Market Returns) / Variance(Market Returns)
```

**Interpretation:**
- Volatility relative to market
- Systematic risk measure

**Ranges:**
- Beta = 1.0: Moves with market
- Beta > 1.0: More volatile than market
- Beta < 1.0: Less volatile than market
- Beta = 0: No market correlation

**Example:**
- Beta = 1.2
- If market up 10%, stock likely up 12%

---

### Alpha

**Formula:**
```
Alpha = Portfolio Return - (Risk-Free Rate + Beta × Market Return)
```

**Interpretation:**
- Excess return above expectation
- Positive = outperformance
- Negative = underperformance

**Example:**
- Expected return: 10%
- Actual return: 12%
- Alpha = 12% - 10% = 2%

---

## 📊 Statistical Metrics

### Skewness

**Interpretation:**
- Asymmetry of return distribution
- Skewness = 0: Symmetric distribution
- Positive: Longer tail to right (good)
- Negative: Longer tail to left (bad)

**Ranges:**
- -0.5 to 0.5: Approximately symmetric
- 0.5 to 1.0: Moderately positively skewed
- > 1.0: Highly positively skewed

---

### Kurtosis

**Interpretation:**
- Tail heaviness
- Kurtosis = 3: Normal distribution
- Excess Kurtosis = 0: Normal
- > 0: Fat tails (more extreme events)
- < 0: Thin tails (fewer extreme events)

---

### Value at Risk (VaR)

**Formula:**
```
VaR = Percentile of returns at confidence level
```

**Interpretation:**
- Worst expected loss
- At given confidence level (e.g., 95%)
- 95% VaR: In 95% of days, loss won't exceed this

**Example:**
- 95% VaR = -2.5%
- 95 out of 100 days, loss ≤ 2.5%
- 5 out of 100 days, loss > 2.5%

---

### Conditional Value at Risk (CVaR)

**Formula:**
```
CVaR = Average of returns worse than VaR
```

**Interpretation:**
- Average loss in worst scenarios
- More extreme than VaR
- Accounts for tail risk

**Example:**
- If VaR is -2.5%
- CVaR might be -3.5%
- Average loss when worst happens

---

## 🎯 Volatility Metrics

### Daily Volatility

**Formula:**
```
Daily Volatility = Standard Deviation of daily percentage returns
```

**Interpretation:**
- Daily price fluctuation
- Used to annualize volatility

---

### Monthly Volatility

**Formula:**
```
Monthly Volatility = Daily Volatility × √21
```

**Interpretation:**
- Monthly price fluctuation
- 21 = trading days per month

---

### Annual Volatility

**Formula:**
```
Annual Volatility = Daily Volatility × √252
```

**Interpretation:**
- Yearly price fluctuation
- Standard risk measure
- 252 = trading days per year

---

## 📊 Portfolio-Specific Metrics

### Tracking Error

**Formula:**
```
Tracking Error = Standard Deviation of (Portfolio Return - Benchmark Return)
```

**Interpretation:**
- How much portfolio differs from benchmark
- Active risk taken
- Higher = more active management

---

### Ulcer Index

**Formula:**
```
Ulcer Index = √(Average of (Drawdown%)²)
```

**Interpretation:**
- Painful volatility
- Penalizes drawdowns more
- Better measure for investors

---

### Profit Factor

**Formula:**
```
Profit Factor = Sum of Gains / Sum of Losses
```

**Interpretation:**
- Return per unit of loss
- > 1.0: More gains than losses
- > 2.0: Excellent
- Example: 2.0 means earn twice losses

---

### Win Rate

**Formula:**
```
Win Rate = Number of Winning Days / Total Trading Days
```

**Interpretation:**
- Percentage of profitable days
- Higher is better
- 50% = as often up as down

**Example:**
- 250 trading days
- 140 profitable days
- Win Rate = 140/250 = 56%

---

### Recovery Factor

**Formula:**
```
Recovery Factor = Total Return / Max Drawdown
```

**Interpretation:**
- How quickly recovers from losses
- Higher = faster recovery
- Useful for strategy evaluation

---

## 🎓 How to Use These Metrics

### For Portfolio Selection

**Primary Metrics:**
1. CAGR - Overall performance
2. Max Drawdown - Risk
3. Sharpe Ratio - Risk-adjusted return

**Secondary Metrics:**
1. Sortino Ratio - Downside risk focus
2. Calmar Ratio - Return vs drawdown
3. Information Ratio - Excess return

### For Risk Assessment

**Key Metrics:**
1. Volatility - Daily price movement
2. Max Drawdown - Worst-case loss
3. Beta - Market correlation
4. VaR - Expected loss threshold
5. CVaR - Tail risk

### For Comparing Portfolios

**Ranking by:**
1. Sharpe Ratio (risk-adjusted return)
2. Sortino Ratio (downside focus)
3. Calmar Ratio (return per drawdown)
4. CAGR (absolute return)
5. Max Drawdown (risk)

### For Understanding Distribution

**Shape Metrics:**
1. Skewness - Distribution asymmetry
2. Kurtosis - Tail heaviness
3. VaR - Percentile analysis
4. Win Rate - Frequency analysis

---

## 📈 Interpretation Guide

### Excellent Portfolio

- CAGR: > 15%
- Sharpe: > 1.5
- Sortino: > 2.0
- Max DD: < -15%
- Win Rate: > 55%

### Good Portfolio

- CAGR: 10-15%
- Sharpe: 1.0-1.5
- Sortino: 1.0-2.0
- Max DD: -15% to -25%
- Win Rate: 50-55%

### Average Portfolio

- CAGR: 5-10%
- Sharpe: 0.5-1.0
- Sortino: 0.5-1.0
- Max DD: -25% to -40%
- Win Rate: 45-50%

### Poor Portfolio

- CAGR: < 5%
- Sharpe: < 0.5
- Sortino: < 0.5
- Max DD: < -40%
- Win Rate: < 45%

---

## 💡 Quick Reference

| Metric | What It Measures | Good Value | Formula Complexity |
|--------|-----------------|------------|-------------------|
| CAGR | Annual growth | 10-15% | Medium |
| Total Return | Overall gain | Depends | Simple |
| Volatility | Risk | 15-20% | Medium |
| Sharpe Ratio | Risk-adjusted return | > 1.0 | Medium |
| Sortino Ratio | Downside risk | > 1.0 | Complex |
| Max Drawdown | Worst loss | > -20% | Simple |
| Beta | Market sensitivity | 0.8-1.2 | Medium |
| Alpha | Outperformance | > 0% | Complex |
| Skewness | Distribution shape | > 0 | Medium |
| Kurtosis | Tail risk | ≈ 3 | Medium |
| VaR | Loss threshold | Depends | Complex |
| CVaR | Extreme loss avg | Higher worse | Complex |

---

## 🔗 Related Resources

- See main [README.md](./README.md) for app overview
- See [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for setup
- See [LINKEDIN_INTEGRATION.md](./LINKEDIN_INTEGRATION.md) for profile info

---

**Last Updated:** December 29, 2024
**Version:** 1.0
