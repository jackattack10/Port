# 🔧 Troubleshooting Guide

## Common Issues and Solutions

---

## 📊 App-Related Issues

### Issue 1: "Rate Limited Error"

**Error Message:**
```
YFRateLimitError: Too Many Requests
429 Client Error
```

**Cause:**
- Yahoo Finance has rate limits (typically 2000 requests per hour)
- Too many stocks or requests in short time

**Solution:**
1. **Wait for auto-retry**
   - App automatically retries with exponential backoff
   - 1st retry: 10 seconds
   - 2nd retry: 20 seconds
   - 3rd retry: 40 seconds

2. **Reduce request load**
   - Use fewer stocks (start with 2-3)
   - Use shorter time period (1y instead of 5y)
   - Analyze one portfolio at a time

3. **Stagger requests**
   - Wait between analyses
   - Use off-peak hours

4. **Clear cache**
   - Hard refresh browser (Ctrl+F5)
   - Clear browser cache
   - Restart app

---

### Issue 2: "Weight Validation Error"

**Error Message:**
```
❌ Portfolio A: Total weight is 95.50%, must be exactly 100%
```

**Cause:**
- Weights don't sum to 100%
- Rounding errors

**Solution:**

1. **Check weights**
   ```
   Stock 1: 30% + Stock 2: 35% + Stock 3: 30% = 95%
   Need: 5% more
   ```

2. **Adjust manually**
   - Increase one stock by 5%
   - Or distribute changes

3. **Allow rounding**
   - System allows ±0.01% rounding error
   - So 99.99% to 100.01% is accepted

4. **Example correction**
   ```
   WRONG: 33.33, 33.33, 33.33 (= 99.99%)
   RIGHT: 33.34, 33.33, 33.33 (= 100.00%)
   ```

---

### Issue 3: "No Data Available"

**Error Message:**
```
Failed to fetch data for ['INFOSYS']: Error fetching data
```

**Causes:**
- Stock ticker is incorrect
- Stock has no data for that period
- Yahoo Finance missing data

**Solutions:**

1. **Verify stock ticker**
   - Use only verified Nifty 50 stocks
   - Check spelling
   - Ensure .NS suffix is included automatically

2. **Use different time period**
   - Try 1y instead of 5y
   - Try 3y instead of 10y
   - Different periods have different data availability

3. **Try alternative ticker**
   ```
   INFOSYS.NS → Not working?
   INFY.NS → Try this instead
   ```

4. **Choose different stock**
   - Pick from verified Nifty 50 list
   - RELIANCE, TCS, HDFCBANK, etc. always have data

---

### Issue 4: "Chart Not Displaying"

**Error Message:**
```
Invalid property specified for object of type plotly.graph_objs.Layout
Index error: index -1 is out of bounds
```

**Causes:**
- Empty data
- Single stock with insufficient data
- Chart rendering error

**Solutions:**

1. **Use multiple stocks**
   - Avoid single stock for portfolio analysis
   - Use at least 2 stocks

2. **Verify data exists**
   - Check metrics display first
   - If metrics exist, data is valid

3. **Refresh page**
   - Hard refresh (Ctrl+F5)
   - Wait 10 seconds
   - Try again

4. **Try different stocks**
   - Some stocks might have gaps
   - Switch to well-established stocks

5. **Change time period**
   - Try 1y or 3y
   - Some periods have better data

---

### Issue 5: "Slow Performance / App Hanging"

**Symptoms:**
- Takes >5 minutes to load
- App seems frozen
- Spinner keeps spinning

**Causes:**
- Rate limiting
- Too many stocks
- Poor network connection
- Server overload

**Solutions:**

1. **Reduce scope**
   - Use 2-3 stocks (not 50)
   - Use 1y period (not 10y)
   - Analyze one portfolio at a time

2. **Wait longer**
   - Initial analysis can take 2-5 minutes
   - Due to Yahoo Finance delays
   - Subsequent loads are faster (cached)

3. **Check connection**
   - Test internet speed
   - Try from different network
   - Disable VPN if using

4. **Restart app**
   - Press 'R' or restart browser
   - Clear browser cache
   - Hard refresh (Ctrl+F5)

5. **Try different stocks**
   - Some stocks are slower
   - RELIANCE, TCS usually fastest
   - Avoid lesser-known stocks

---

## 🖥️ Technical Issues

### Issue 6: "ModuleNotFoundError"

**Error Message:**
```
ModuleNotFoundError: No module named 'streamlit'
ModuleNotFoundError: No module named 'yfinance'
```

**Cause:**
- Python package not installed

**Solution (Local Setup):**

```bash
# Reinstall all dependencies
pip install -r requirements.txt

# Or specific package
pip install streamlit
pip install yfinance
```

**Solution (Cloud):**
- Ensure `requirements.txt` exists in repo
- Commit and push to GitHub
- Streamlit auto-installs

---

### Issue 7: "Port Already in Use"

**Error Message:**
```
Address already in use: ('127.0.0.1', 8501)
```

**Cause:**
- Another app already using port 8501

**Solution:**

```bash
# Option 1: Use different port
streamlit run app.py --server.port 8502

# Option 2: Kill existing process
# Windows:
netstat -ano | findstr :8501
taskkill /PID [PID] /F

# macOS/Linux:
lsof -i :8501
kill -9 [PID]
```

---

### Issue 8: "Python Version Issue"

**Error Message:**
```
SyntaxError: invalid syntax
Python 3.6 is not supported
```

**Cause:**
- Python version < 3.8

**Solution:**

```bash
# Check version
python --version

# If < 3.8, upgrade
# Download from https://www.python.org/downloads/

# Verify after upgrade
python --version  # Should be 3.8+
```

---

### Issue 9: "Import Error After Local Setup"

**Error Message:**
```
ModuleNotFoundError: No module named 'modules.data_fetcher'
```

**Cause:**
- Working directory wrong
- sys.path not configured

**Solution:**

```bash
# Navigate to correct directory
cd nifty-portfolio-analyzer

# Verify structure
ls  # Should show: app.py, modules/, docs/, requirements.txt

# Run from correct directory
streamlit run app.py
```

---

## 🌐 Web Browser Issues

### Issue 10: "Blank Page / Page Won't Load"

**Symptoms:**
- Browser shows blank page
- Loading spinner forever
- Error in console

**Solutions:**

1. **Hard refresh**
   - Ctrl+F5 (Windows)
   - Cmd+Shift+R (Mac)
   - Clears all cache

2. **Clear browser data**
   - Settings → Clear browsing data
   - Select all time
   - Clear cookies and cache

3. **Try different browser**
   - Chrome, Firefox, Safari, Edge
   - Some work better than others

4. **Check internet**
   - Test speed: speedtest.net
   - Try different WiFi
   - Disable VPN

5. **Check URL**
   - Local: http://localhost:8501
   - Cloud: https://themountainpathportfolioanalyzer.streamlit.app

---

### Issue 11: "Mobile View Issues"

**Symptoms:**
- Buttons too small
- Text unreadable
- Layout broken

**Solutions:**

1. **Zoom out**
   - Pinch zoom out (mobile)
   - Ctrl+- (desktop)
   - Browser zoom settings

2. **Rotate screen**
   - Try landscape orientation
   - More space for charts

3. **Update browser**
   - Mobile browsers need updates
   - Chrome, Safari latest versions

4. **Report issue**
   - App is responsive
   - If issues, might be specific case
   - Contact creator for help

---

## 📱 Data & Calculation Issues

### Issue 12: "Metrics Seem Wrong"

**Problem:**
- Sharpe ratio negative
- CAGR doesn't match expectation

**Causes:**
- Misunderstanding metric
- Period too short
- Risk-free rate not correct

**Solutions:**

1. **Understand metrics**
   - Read METRICS_EXPLAINED.md
   - Learn what each metric means
   - Compare with benchmarks

2. **Check settings**
   - Verify time period
   - Confirm risk-free rate
   - Check stock selection

3. **Recalculate manually**
   - Use formula from docs
   - Cross-check calculation
   - Report if discrepancy

---

### Issue 13: "Missing Data Points"

**Problem:**
- Chart has gaps
- Some metrics are zero
- Incomplete calculations

**Causes:**
- Stock delisted during period
- Market holidays
- Data gaps from source

**Solutions:**

1. **Use different period**
   - Shorter time frame
   - More recent data
   - Different stocks

2. **Check calendar**
   - Market closed on holidays
   - Normal gaps expected
   - Use trading days (252/year)

3. **Verify data source**
   - Yahoo Finance provides data
   - Trust their timestamps
   - Some gaps are real

---

### Issue 14: "Correlation Matrix Empty"

**Problem:**
- No correlation data shown
- Heatmap not displaying

**Cause:**
- Single stock portfolio

**Solution:**
- Use multiple stocks (2+)
- Correlation requires multiple assets
- Not applicable for single stock

---

## 🔗 LinkedIn Integration Issues

### Issue 15: "LinkedIn Button Not Working"

**Problem:**
- Link doesn't open
- Opens wrong page

**Solution:**

1. **Check URL**
   - Should be: https://www.linkedin.com/in/trichyravis
   - Verify in browser directly

2. **Try right-click open**
   - Right-click button
   - "Open link in new tab"
   - Copy link address

3. **Manual navigation**
   - Type URL directly
   - Search for profile name
   - Contact creator for verification

---

## 🎯 Performance Issues

### Issue 16: "App is Slow / Laggy"

**Optimize Performance:**

1. **Reduce data**
   ```
   Instead of: 5 years, 50 stocks
   Use: 1 year, 5 stocks
   ```

2. **Clear cache**
   - Browser: Ctrl+Shift+Delete
   - App: Streamlit always clears

3. **Use off-peak**
   - Avoid market hours
   - Yahoo Finance slower during trading
   - Use before 9:30 AM EST

4. **Upgrade internet**
   - Faster WiFi
   - Wired connection
   - Lower latency

5. **Close tabs**
   - Other heavy apps
   - Many browser tabs
   - Video streaming

---

## 📞 When to Contact Creator

**Contact if:**
- Error persists after all solutions
- Something clearly broken
- Security/data issue
- Feature request
- Bug report

**Where to Contact:**
- **LinkedIn:** https://www.linkedin.com/in/trichyravis
- **GitHub:** https://github.com/trichydavis/nifty-portfolio-analyzer

---

## ✅ Quick Troubleshooting Checklist

When app has issue:

- [ ] Hard refresh browser (Ctrl+F5)
- [ ] Clear browser cache
- [ ] Restart app
- [ ] Try different stocks
- [ ] Use shorter time period
- [ ] Check internet connection
- [ ] Try different browser
- [ ] Restart your computer
- [ ] Update Python packages
- [ ] Read error message carefully
- [ ] Check documentation
- [ ] Try again after few minutes
- [ ] Contact creator if persistent

---

## 🆘 Error Message Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Rate Limited Error | Too many requests | Wait, retry auto |
| Weight Validation | Weights ≠ 100% | Adjust weights |
| No Data Available | Invalid ticker | Use Nifty 50 stock |
| Chart Error | Empty data | Use 2+ stocks |
| Slow Performance | Too much data | Reduce scope |
| Module Not Found | Package missing | `pip install -r requirements.txt` |
| Port In Use | Conflict | Use different port |
| Python Error | Version issue | Update Python 3.8+ |

---

**Last Updated:** December 29, 2024
**Version:** 1.0
