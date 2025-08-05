# 🏦 Revolut Financial Crime Dashboard

A modern and elegant dashboard for financial crime monitoring and analysis.

## 📊 Overview

This Streamlit dashboard provides an intuitive interface for analyzing financial transaction data and detecting fraudulent activities. It combines key metrics, interactive visualizations, and modern design for an optimal user experience.

<img width="1632" height="2671" alt="image" src="https://github.com/user-attachments/assets/9d1f1aaf-cecc-460c-8636-ebeb5e91daaa" />
<img width="514" height="1468" alt="image" src="https://github.com/user-attachments/assets/6c99cd71-bb3f-43de-a496-f4f9a7953e12" />


###  Key Features

- ** Real-time KPIs** : Active users, transactions, volume, fraud rate
- ** Advanced filters** : Week selection, countries, transaction types with All/Clear buttons
- ** Interactive visualizations** : Plotly charts with dark design
- ** User-centric interface** : clear design with soft color palette
- ** Optimized performance** : Data caching and fast loading

##  Installation

### Prerequisites
- Python 3.10+
- pip or conda

### Install dependencies

```bash
# Install dependencies
pip install -r requirements.txt
```

## 📁 Project Structure

```
FInCrime/
├── data/
│   ├── users.csv                        # Users dataset
│   ├── transactions.csv                 # Transactions dataset
│   ├── fraudsters.csv                   # Fraudsters dataset
│   └── base_2_202508041440.csv         # Processed data
├── scripts/
│   ├── dashboard_senior.py              # Main dashboard
│   ├── query_eda.sql                   # SQL query for data extraction
│   ├── db_setup.py                     # SQLite database setup
│   └── dl_data_script.py               # Data download script
├── requirements.txt                     # Python dependencies
├── README.md                           # Main documentation
└── docs/
    └── TECHNICAL_DOCUMENTATION.md      # Technical documentation
```

##  Design and UX

### Color Palette
- **Main background** : `#0F0F0F` (dark anthracite)
- **Cards/panels** : `#1C1C1C` (very dark gray)
- **Main text** : `#EDEDED` (soft white)
- **Accent** : `#698EB8` (soft blue)
- **Success** : `#10B981` (soft green)
- **Alert** : `#EF4444` (soft red)

### Design characteristics
- Elegant dark interface
- Rounded cards with soft shadows
- Modern Inter typography
- Generous spacing and fluid layout
- Styled components (buttons, filters, charts)

## Detailed Features

### Main KPIs
- **Active users** : Total number of unique users
- **Transactions** : Total transaction volume
- **Financial volume** : Total transaction amount
- **Fraud rate** : Percentage of fraudulent transactions

### Interactive filters
- **Week selection** : Multiple choice with "All/Clear" buttons for quick selection
- **Country selection** : Country filtering with search functionality
- **Transaction types** : ATM, CARD_PAYMENT, EXCHANGE, etc.

### Visualizations
- **Fraud evolution** : Temporal chart of fraudulent amounts (full-width)
- **Transaction types** : Overview and fraudulent transactions (split view)
- **Top 5 by country** : Ranking by fraud amount and volume (horizontal bars)

## 🔧 Configuration

### Environment variables
Create a `.env` file at the project root:

```env
# Database configuration
DATABASE_URL=sqlite:///fincrime.db

# Data configuration
DATA_FILE_PATH=data/base_2_202508041440.csv
```

### Customization
The dashboard can be customized via:
- Modifying the color palette in `COLORS`
- Adding new KPIs in the calculations section
- Integrating new visualizations

## 📈 Usage

### Navigation
1. **Filters** : Use the sidebar to select your criteria with All/Clear buttons
2. **KPIs** : Check the main metrics at the top (no trend percentages)
3. **Charts** : Explore the interactive visualizations
4. **Export** : Use the export buttons (feature coming soon)

### Data interpretation
- Data is aggregated by week (ISO format)
- Amounts are in GBP (British pounds)
- Fraud percentages are calculated on total volume
- Weekly granularity with fallback to daily data
