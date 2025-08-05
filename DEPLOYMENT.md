# 🚀 Streamlit Cloud Deployment Guide

## 📋 Prerequisites

1. **GitHub Account** : Your code must be on GitHub
2. **Streamlit Cloud Account** : Sign up at [share.streamlit.io](https://share.streamlit.io)

## 🔧 Deployment Steps

### 1. Prepare Your Repository

Ensure your repository has this structure:
```
FInCrime/
├── streamlit_app.py          # Main entry point
├── requirements.txt          # Dependencies
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── data/
│   └── base_2_202508041440.csv
├── scripts/
│   └── dashboard_senior.py
└── README.md
```

### 2. Deploy on Streamlit Cloud

1. **Go to [share.streamlit.io](https://share.streamlit.io)**
2. **Sign in with GitHub**
3. **Click "New app"**
4. **Configure your app:**
   - **Repository**: `your-username/revolut-financial-crime-dashboard`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
   - **App URL**: `revolut-financial-crime-dashboard`

### 3. Advanced Settings (Optional)

- **Python version**: 3.10
- **Memory**: 1GB (default)
- **Timeout**: 60 seconds

## 🔍 Troubleshooting

### Common Issues:

1. **Import Errors**: Make sure all dependencies are in `requirements.txt`
2. **File Path Errors**: Use relative paths in your code
3. **Memory Issues**: Optimize data loading with `@st.cache_data`

### Debug Commands:

```bash
# Test locally first
streamlit run streamlit_app.py

# Check requirements
pip install -r requirements.txt
```

## 📊 Monitoring

- **Logs**: Available in Streamlit Cloud dashboard
- **Performance**: Monitor memory usage and load times
- **Updates**: Automatic deployment on git push

## 🌐 Your App URL

Once deployed, your app will be available at:
`https://revolut-financial-crime-dashboard.streamlit.app`

## 📝 Update README

Add this to your README.md:

```markdown
## 🚀 Live Demo

**Try the dashboard live:** [https://revolut-financial-crime-dashboard.streamlit.app](https://revolut-financial-crime-dashboard.streamlit.app)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://revolut-financial-crime-dashboard.streamlit.app)
```

---

**Deployment Guide v1.0.0** 