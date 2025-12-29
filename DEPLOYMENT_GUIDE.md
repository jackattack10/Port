# 🚀 Deployment Guide

## Complete Setup and Deployment Instructions

This guide covers local development and cloud deployment.

---

## 📋 Prerequisites

### System Requirements

- **Python:** 3.8 or higher
- **OS:** Windows, macOS, or Linux
- **RAM:** 4GB minimum (8GB recommended)
- **Disk Space:** 500MB free

### Software Requirements

- Python package manager (pip)
- Git (for version control)
- Text editor or IDE

---

## 🔧 Local Setup

### Step 1: Clone Repository

```bash
# Navigate to desired directory
cd ~/projects

# Clone the repository
git clone https://github.com/trichydavis/nifty-portfolio-analyzer.git

# Enter directory
cd nifty-portfolio-analyzer
```

### Step 2: Create Virtual Environment (Optional but Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
# Check if packages are installed
pip list

# Should show:
# streamlit
# pandas
# numpy
# yfinance
# plotly
# scipy
# scikit-learn
```

### Step 5: Run Locally

```bash
# Run the Streamlit app
streamlit run app.py

# Should output something like:
# You can now view your Streamlit app in your browser.
# Local URL: http://localhost:8501
# Network URL: http://192.168.x.x:8501
```

### Step 6: Access the App

Open your browser and go to: **http://localhost:8501**

---

## 📦 Requirements.txt

The app requires these packages:

```
streamlit>=1.35.0
pandas>=2.2.0
numpy>=2.0.0
yfinance>=0.2.35
plotly>=5.20.0
scipy>=1.14.0
scikit-learn>=1.3.0
```

**What each does:**
- **streamlit:** Web app framework
- **pandas:** Data manipulation
- **numpy:** Numerical computing
- **yfinance:** Stock data API
- **plotly:** Interactive charts
- **scipy:** Scientific computing
- **scikit-learn:** ML/statistics

---

## 🌐 Cloud Deployment (Streamlit Cloud)

### Step 1: Set Up GitHub Repository

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit - Nifty Portfolio Analyzer"

# Add remote (replace username)
git remote add origin https://github.com/trichydavis/nifty-portfolio-analyzer.git

# Push to GitHub
git push -u origin main
```

### Step 2: Create Streamlit Cloud Account

1. Go to: https://streamlit.io/cloud
2. Click "Sign up"
3. Connect GitHub account
4. Authorize Streamlit

### Step 3: Deploy App

1. Click "New app"
2. Select repository: `nifty-portfolio-analyzer`
3. Select branch: `main`
4. Select file: `app.py`
5. Click "Deploy"

### Step 4: Wait for Deployment

- Takes 1-5 minutes
- See deployment logs
- App goes live automatically

### Step 5: Access Live App

- URL: `https://themountainpathportfolioanalyzer.streamlit.app`
- Share with users
- Monitor performance

---

## 🔄 Updating the App

### Local Development

```bash
# Make changes to files
# Test locally first

streamlit run app.py

# Verify everything works
```

### Push Updates to Cloud

```bash
# Add changes
git add .

# Commit with message
git commit -m "Add new feature or fix"

# Push to GitHub
git push origin main

# Streamlit Cloud auto-deploys (30 seconds)
```

---

## 📝 File Structure

```
nifty-portfolio-analyzer/
├── app.py                          # Main application
├── requirements.txt                # Python dependencies
├── README.md                       # Project readme
├── .gitignore                      # Git ignore file
│
├── modules/                        # Code modules
│   ├── __init__.py
│   ├── data_fetcher.py            # Data fetching
│   ├── portfolio_analyzer.py       # Analysis logic
│   ├── metrics_calculator.py       # Metrics computation
│   └── visualizations.py           # Chart generation
│
├── docs/                          # Documentation
│   ├── README.md                  # Main documentation
│   ├── LINKEDIN_INTEGRATION.md    # LinkedIn guide
│   ├── METRICS_EXPLAINED.md       # Metrics documentation
│   └── DEPLOYMENT_GUIDE.md        # This file
│
└── .streamlit/
    └── config.toml               # Streamlit configuration
```

---

## ⚙️ Configuration Files

### requirements.txt

```
streamlit>=1.35.0
pandas>=2.2.0
numpy>=2.0.0
yfinance>=0.2.35
plotly>=5.20.0
scipy>=1.14.0
scikit-learn>=1.3.0
```

### .gitignore

```
# Virtual environment
venv/
env/
.venv

# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Cache
.streamlit/
*.cache
```

### .streamlit/config.toml (Optional)

```toml
[client]
showErrorDetails = false

[logger]
level = "info"

[server]
headless = true
runOnSave = true

[theme]
primaryColor = "#003366"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

---

## 🐛 Troubleshooting Deployment

### Issue 1: Import Errors

**Error:** `ModuleNotFoundError: No module named 'streamlit'`

**Solution:**
```bash
# Reinstall packages
pip install -r requirements.txt

# Or install specific package
pip install streamlit
```

### Issue 2: Port Already in Use

**Error:** `Address already in use: ('127.0.0.1', 8501)`

**Solution:**
```bash
# Use different port
streamlit run app.py --server.port 8502

# Or kill existing process
# Windows: netstat -ano | findstr :8501
# macOS/Linux: lsof -i :8501
```

### Issue 3: Memory Error

**Error:** `MemoryError` or app crashes

**Solution:**
- Use shorter time period (1y instead of 10y)
- Analyze fewer stocks
- Clear browser cache
- Restart app

### Issue 4: Slow Performance

**Causes:**
- Yahoo Finance rate limiting
- Too many stocks
- Too much historical data

**Solutions:**
```bash
# Use cache
@st.cache_data
def fetch_data():
    # Data fetching code

# Limit stocks
# Use shorter periods
# Clear cache: Ctrl+F5
```

### Issue 5: Deployment Fails

**Causes:**
- Missing requirements.txt
- Syntax errors in code
- Incompatible Python version

**Solutions:**
```bash
# Verify requirements.txt exists
ls requirements.txt

# Check Python version
python --version  # Should be 3.8+

# Verify code syntax
python -m py_compile app.py

# Check module imports
python -c "import streamlit; import yfinance"
```

---

## 📊 Performance Optimization

### Caching Strategy

```python
@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_stock_data(stocks, period):
    # Expensive operation
    return data
```

### Data Fetching

```python
# Limit concurrent requests
max_workers = 5
timeout = 60  # seconds

# Retry logic for rate limiting
max_retries = 3
base_wait = 10  # seconds
```

### Chart Rendering

```python
# Use Plotly (already optimized)
# Limit number of data points
# Use responsive design
```

---

## 🔐 Security Best Practices

### Secrets Management

If you add sensitive data, use Streamlit secrets:

```bash
# Create .streamlit/secrets.toml
# Add secrets (not committed to GitHub)

# Access in app:
api_key = st.secrets["API_KEY"]
```

### Environment Variables

```bash
# Set environment variables
export STREAMLIT_LOGGER_LEVEL=info
export PYTHONDONTWRITEBYTECODE=1
```

### Data Privacy

- No user data collection
- No authentication required
- Public API (Yahoo Finance)
- No sensitive data stored

---

## 📈 Monitoring

### Check Deployment Status

```bash
# Streamlit Cloud dashboard
https://share.streamlit.io

# Check logs
# View in Streamlit Cloud console
```

### Performance Metrics

- Page load time
- Data fetch time
- Chart rendering time
- Memory usage

---

## 🔄 Continuous Integration (Optional)

### GitHub Actions

Create `.github/workflows/python-app.yml`:

```yaml
name: Python application

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Verify imports
      run: |
        python -c "import streamlit; import yfinance"
```

---

## 📱 Mobile Deployment

### Responsive Design

The app is already responsive due to Streamlit's default behavior.

**Test on Mobile:**
1. Deploy to Streamlit Cloud
2. Access from mobile device
3. Verify layout
4. Check touch targets

### Progressive Web App (Optional)

Could add PWA support for offline access (not currently implemented).

---

## 🆘 Getting Help

### Resources

- **Streamlit Docs:** https://docs.streamlit.io
- **GitHub Issues:** https://github.com/trichydavis/nifty-portfolio-analyzer/issues
- **Yahoo Finance:** https://finance.yahoo.com

### Creator Contact

**Prof. V. Ravichandran**
- **LinkedIn:** https://www.linkedin.com/in/trichyravis
- **Email:** Check LinkedIn profile

---

## ✅ Deployment Checklist

- [ ] Python 3.8+ installed
- [ ] Repository cloned
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] App runs locally
- [ ] No errors in console
- [ ] GitHub repository ready
- [ ] Streamlit Cloud connected
- [ ] Deployment successful
- [ ] App accessible online
- [ ] All features working
- [ ] Links are correct
- [ ] LinkedIn integration works
- [ ] Charts display properly
- [ ] No performance issues

---

## 🎉 You're Ready!

Your app is now:
- ✅ Running locally
- ✅ Deployed on Streamlit Cloud
- ✅ Accessible worldwide
- ✅ Ready for users

---

**Last Updated:** December 29, 2024
**Version:** 1.0
