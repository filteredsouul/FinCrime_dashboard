import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import plotly.colors as pc

# Page configuration
st.set_page_config(
    page_title="Revolut Financial Crime Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern design
st.markdown("""
<style>
    /* Base styles */
    .main {
        background-color: #0F0F0F !important;
        font-family: 'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #EDEDED;
    }
    
    /* Header */
    .header {
        background: linear-gradient(135deg, #1C1C1C 0%, #0F0F0F 100%);
        color: #EDEDED;
        padding: 2rem 2.5rem;
        margin: -1rem -1rem 2.5rem -1rem;
        display: flex;
        align-items: center;
        gap: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        position: relative;
        overflow: hidden;
        border-radius: 0 0 20px 20px;
    }
    
    .header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, transparent 50%, rgba(255,255,255,0.05) 100%);
        pointer-events: none;
    }
    
    .header-logo {
        width: 48px;
        height: 48px;
        background: #698EB8;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        color: #EDEDED;
        font-size: 1.5rem;
        box-shadow: 0 4px 20px rgba(105, 142, 184, 0.3);
        position: relative;
        z-index: 1;
    }
    
    .header-title {
        font-size: 2rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
        position: relative;
        z-index: 1;
    }
    
    .header-subtitle {
        font-size: 1rem;
        opacity: 0.9;
        margin-top: 0.5rem;
        font-weight: 500;
        position: relative;
        z-index: 1;
    }
    
    /* KPI Cards */
    .kpi-card {
        background-color: #1C1C1C !important;
        border-radius: 20px !important;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25) !important;
        border: none !important;
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        color: #EDEDED;
    }
    
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #698EB8 0%, #3B82F6 100%);
        border-radius: 20px 20px 0 0;
    }
    
    .kpi-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.12);
    }
    
    .kpi-title {
        font-size: 0.875rem;
        color: #9CA3AF;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.75rem;
    }
    
    .kpi-value {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0.75rem 0;
        color: #EDEDED;
        line-height: 1;
    }
    
    .kpi-trend {
        font-size: 0.875rem;
        display: flex;
        align-items: center;
        gap: 0.25rem;
        font-weight: 600;
    }
    
    .trend-up {
        color: #059669;
    }
    
    .trend-down {
        color: #dc2626;
    }
    
    /* Status cards */
    .status-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
        border: 1px solid rgba(226, 232, 240, 0.8);
        height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .status-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        border-radius: 16px 16px 0 0;
    }
    
    .status-card.completed::before {
        background: linear-gradient(90deg, #10b981 0%, #059669 100%);
    }
    
    .status-card.failed::before {
        background: linear-gradient(90deg, #dc2626 0%, #b91c1c 100%);
    }
    
    .status-card.cancelled::before {
        background: linear-gradient(90deg, #d97706 0%, #b45309 100%);
    }
    
    .status-card.refunded::before {
        background: linear-gradient(90deg, #0891b2 0%, #0e7490 100%);
    }
    
    .status-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
    }
    
    .status-title {
        font-size: 0.875rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    
    .status-value {
        font-size: 2rem;
        font-weight: 800;
        color: #1e293b;
        line-height: 1;
    }
    
    /* Filter buttons */
    .stButton > button {
        border-radius: 12px !important;
        font-weight: 600;
        font-size: 0.875rem;
        padding: 0.5rem 1rem;
        transition: all 0.2s ease;
        background-color: #2D2D2D !important;
        color: #EDEDED !important;
        border: 1px solid #3D3D3D !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        background-color: #3D3D3D !important;
    }
    
    /* Streamlit components styling */
    .stSelectbox, .stMultiselect, .stDateInput {
        background-color: #2D2D2D !important;
        color: #EDEDED !important;
        border-radius: 12px !important;
        border: 1px solid #3D3D3D !important;
    }
    
    .stSelectbox > div, .stMultiselect > div {
        background-color: #2D2D2D !important;
        color: #EDEDED !important;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #1C1C1C !important;
    }
    
    /* Main content area */
    .main .block-container {
        background-color: #0F0F0F !important;
        color: #EDEDED !important;
    }
    
    /* Chart containers */
    .chart-container {
        background-color: #1C1C1C !important;
        border-radius: 20px !important;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25) !important;
        border: none !important;
        margin: 1.5rem 0;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        color: #EDEDED;
    }
    
    .chart-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #10B981 0%, #059669 100%);
        border-radius: 20px 20px 0 0;
    }
    
    .chart-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
    }
    
    .chart-title {
        font-size: 1.375rem;
        font-weight: 600;
        color: #EDEDED;
        margin-bottom: 2rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        position: relative;
    }
    
    .chart-title::before {
        content: '';
        width: 3px;
        height: 24px;
        background: linear-gradient(180deg, #698EB8 0%, #3B82F6 100%);
        border-radius: 2px;
    }
    
    /* Sidebar */
    .sidebar .sidebar-content {
        background-color: #1C1C1C !important;
        border-right: 1px solid #2D2D2D;
        padding: 1.5rem;
        color: #EDEDED;
    }
    
    .filter-section {
        background-color: #2D2D2D !important;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: none !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
        transition: all 0.2s ease;
        color: #EDEDED;
    }
    
    .filter-section:hover {
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
    }
    
    .filter-title {
        font-size: 1.125rem;
        font-weight: 600;
        color: #EDEDED;
        margin-bottom: 1.25rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .filter-icon {
        font-size: 1.1rem;
    }
    
    /* Export buttons */
    .export-section {
        background-color: #2D2D2D !important;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        border: none !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
        color: #EDEDED;
    }
    
    .export-button {
        background: linear-gradient(135deg, #698EB8 0%, #3B82F6 100%);
        color: #EDEDED;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(105, 142, 184, 0.3);
    }
    
    .export-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(58, 101, 150, 0.4);
    }
    
    /* Status banner */
    .status-banner {
        background: linear-gradient(135deg, #1C1C1C 0%, #2D2D2D 100%);
        color: #EDEDED;
        padding: 1rem 2rem;
        border-radius: 12px;
        margin: 2rem 0;
        font-size: 0.95rem;
        font-weight: 600;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
        position: relative;
        overflow: hidden;
        border: 1px solid #2D2D2D;
    }
    
    .status-banner::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, transparent 50%, rgba(255,255,255,0.05) 100%);
        pointer-events: none;
    }
    
    /* Section titles */
    .section-title {
        font-size: 1.75rem;
        font-weight: 700;
        color: #EDEDED;
        margin: 2.5rem 0 1.5rem 0;
        position: relative;
        padding-left: 1rem;
    }
    
    .section-title::before {
        content: '';
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 6px;
        height: 32px;
        background: linear-gradient(180deg, #3A6596 0%, #0F307D 100%);
        border-radius: 3px;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .kpi-value {
            font-size: 2rem;
        }
        
        .header-title {
            font-size: 1.5rem;
        }
        
        .chart-container {
            padding: 1.5rem;
        }
        
        .header {
            padding: 1.5rem 2rem;
        }
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f5f9;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #cbd5e1;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #94a3b8;
    }
</style>
""", unsafe_allow_html=True)

# Color palette
COLORS = {
    'primary': '#698EB8',      # Soft Blue (Finary style)
    'secondary': '#3B82F6',    # Bright Blue
    'success': '#10B981',      # Soft Green
    'danger': '#EF4444',       # Soft Red
    'warning': '#F59E0B',      # Soft Orange
    'info': '#3B82F6',         # Blue info
    'light': '#EDEDED',        # Soft White text
    'dark': '#0F0F0F',         # Dark background
    'dark_blue': '#1C1C1C',    # Card background
    'accent': '#698EB8'        # Soft Blue for accents
}

# Data loading function
@st.cache_data
def load_data():
    """Load and prepare data"""
    try:
        # Try to load the new weekly data file first
        df = pd.read_csv("data/base_2_202508041440.csv")
        
        # Check if the file has the new weekly structure
        if 'iso_week' in df.columns:
            # New weekly structure
            df["day_date"] = pd.to_datetime(df["day_date"])
            df["week_date"] = pd.to_datetime(df["week_date"])
            return df
        else:
            # Fallback to old structure
            df["day_date"] = pd.to_datetime(df["day_date"])
            return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Load data
with st.spinner("Loading data..."):
    df = load_data()

if df is None:
    st.error("Unable to load data. Please check if the data file exists and has the correct format.")
    st.info("Expected columns: iso_week, day_date, week_date, country, transaction_type, state, nb_users, nb_fraudsters, nb_transaction, nb_transaction_fraud, total_amount_fraud, total_amount_transactions")
    st.stop()

# Display data info for debugging
st.sidebar.markdown("### Data Info")
st.sidebar.info(f"Rows: {len(df)} | Columns: {len(df.columns)}")
if 'iso_week' in df.columns:
    st.sidebar.success("✅ Weekly data structure detected")
else:
    st.sidebar.warning("⚠️ Daily data structure detected")

# Sidebar with filters
with st.sidebar:
    st.markdown("### Filters")
    
    # Collapsible filter sections
    if 'iso_week' in df.columns:
        # Weekly data structure
        with st.expander("Week Selection", expanded=True):
            # Get unique weeks sorted
            unique_weeks = sorted(df["iso_week"].unique(), reverse=True)
            
            # All/None buttons for weeks
            col1, col2 = st.columns(2)
            with col1:
                if st.button("All Weeks", key="all_weeks", help="Select all weeks"):
                    st.session_state.selected_weeks = unique_weeks
                    st.rerun()
            with col2:
                if st.button("Clear Weeks", key="clear_weeks", help="Clear all week selections"):
                    st.session_state.selected_weeks = []
                    st.rerun()
            
            # Initialize session state for weeks
            if "selected_weeks" not in st.session_state:
                default_weeks = unique_weeks[:4] if len(unique_weeks) >= 4 else unique_weeks
                st.session_state.selected_weeks = default_weeks
            
            selected_weeks = st.multiselect(
                "Select Weeks",
                options=unique_weeks,
                default=st.session_state.selected_weeks,
                key="weeks_multiselect",
                help="Choose weeks to analyze (ISO format: YYYY-WNN)"
            )
            
            # Update session state
            st.session_state.selected_weeks = selected_weeks
            
            if not selected_weeks:
                selected_weeks = unique_weeks[:4] if len(unique_weeks) >= 4 else unique_weeks
    else:
        # Daily data structure - fallback
        with st.expander("Date Range", expanded=True):
            min_date, max_date = df["day_date"].min(), df["day_date"].max()
            date_range = st.date_input(
                "Select Date Range",
                value=(max_date - timedelta(days=30), max_date),
                min_value=min_date,
                max_value=max_date,
                help="Choose the date range for analysis"
            )
            
            if len(date_range) == 2:
                start_date, end_date = date_range
            else:
                start_date = end_date = date_range
    
    with st.expander("Countries", expanded=True):
        countries = sorted(df["country"].unique())
        
        # All/None buttons for countries
        col1, col2 = st.columns(2)
        with col1:
            if st.button("All Countries", key="all_countries", help="Select all countries"):
                st.session_state.selected_countries = countries
                st.rerun()
        with col2:
            if st.button("Clear Countries", key="clear_countries", help="Clear all country selections"):
                st.session_state.selected_countries = []
                st.rerun()
        
        # Initialize session state for countries
        if "selected_countries" not in st.session_state:
            st.session_state.selected_countries = countries[:5] if len(countries) > 5 else countries
        
        selected_countries = st.multiselect(
            "Select Countries",
            options=countries,
            default=st.session_state.selected_countries,
            key="countries_multiselect",
            help="Choose countries to analyze"
        )
        
        # Update session state
        st.session_state.selected_countries = selected_countries
    
    with st.expander("Transaction Types", expanded=True):
        transaction_types = sorted(df["transaction_type"].unique())
        
        # All/None buttons for transaction types
        col1, col2 = st.columns(2)
        with col1:
            if st.button("All Types", key="all_types", help="Select all transaction types"):
                st.session_state.selected_types = transaction_types
                st.rerun()
        with col2:
            if st.button("Clear Types", key="clear_types", help="Clear all transaction type selections"):
                st.session_state.selected_types = []
                st.rerun()
        
        # Initialize session state for transaction types
        if "selected_types" not in st.session_state:
            st.session_state.selected_types = transaction_types
        
        selected_types = st.multiselect(
            "Select Transaction Types",
            options=transaction_types,
            default=st.session_state.selected_types,
            key="types_multiselect",
            help="Choose transaction types to include"
        )
        
        # Update session state
        st.session_state.selected_types = selected_types
    
    # Transaction States section removed as 'state' column is not available in the dataset
    
    # Export section
    st.markdown("### Export")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Export PDF", help="Export dashboard as PDF"):
            st.info("PDF export feature coming soon!")
    with col2:
        if st.button("Export CSV", help="Export data as CSV"):
            st.info("CSV export feature coming soon!")

# Filter data based on selections
if 'iso_week' in df.columns:
    # Weekly data structure
    filtered_df = df[
        (df["iso_week"].isin(selected_weeks)) &
        (df["country"].isin(selected_countries)) &
        (df["transaction_type"].isin(selected_types))
    ]
else:
    # Daily data structure - fallback
    filtered_df = df[
        (df["day_date"] >= pd.to_datetime(start_date)) &
        (df["day_date"] <= pd.to_datetime(end_date)) &
        (df["country"].isin(selected_countries)) &
        (df["transaction_type"].isin(selected_types))
    ]

# Header
st.markdown(f"""
<div class="header">
    <div class="header-logo">R</div>
    <div>
    <h1 class="header-title">Revolut Financial Crime Dashboard</h1>
        <div class="header-subtitle">Real-time monitoring & analytics</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Status banner
if 'iso_week' in df.columns:
    week_range = f"{min(selected_weeks)} to {max(selected_weeks)}" if len(selected_weeks) > 1 else selected_weeks[0]
    st.markdown(f"""
    <div class="status-banner">
        Data for weeks: {week_range} | 
        Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div class="status-banner">
        Data from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')} | 
        Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
</div>
""", unsafe_allow_html=True)

# KPI Section
st.markdown('<div class="section-title">Key Performance Indicators</div>', unsafe_allow_html=True)

# Calculate KPIs
total_users = filtered_df["nb_users"].sum()
total_transactions = filtered_df["nb_transaction"].sum()
total_amount_transaction = filtered_df["total_amount_transactions"].sum()
fraud_rate = (filtered_df["nb_transaction_fraud"].sum() / total_transactions * 100) if total_transactions > 0 else 0

# Previous period for trend calculation
if 'iso_week' in df.columns:
    # Weekly data structure
    sorted_weeks = sorted(selected_weeks)
    current_week = sorted_weeks[-1] if sorted_weeks else selected_weeks[0]

    # Find the previous week
    all_weeks = sorted(df["iso_week"].unique())
    current_week_index = all_weeks.index(current_week) if current_week in all_weeks else -1
    prev_week = all_weeks[current_week_index + 1] if current_week_index + 1 < len(all_weeks) else current_week

    prev_df = df[
        (df["iso_week"] == prev_week) &
        (df["country"].isin(selected_countries)) &
        (df["transaction_type"].isin(selected_types))
    ]
else:
    # Daily data structure - fallback
    prev_start = start_date - timedelta(days=(end_date - start_date).days)
    prev_end = start_date
    prev_df = df[
        (df["day_date"] >= pd.to_datetime(prev_start)) &
        (df["day_date"] <= pd.to_datetime(prev_end)) &
        (df["country"].isin(selected_countries)) &
        (df["transaction_type"].isin(selected_types))
    ]

prev_users = prev_df["nb_users"].sum()
prev_transactions = prev_df["nb_transaction"].sum()
prev_amount = prev_df["total_amount_transactions"].sum()
prev_fraud_rate = (prev_df["nb_transaction_fraud"].sum() / prev_transactions * 100) if prev_transactions > 0 else 0

# Calculate trends
user_trend = ((total_users - prev_users) / prev_users * 100) if prev_users > 0 else 0
transaction_trend = ((total_transactions - prev_transactions) / prev_transactions * 100) if prev_transactions > 0 else 0
amount_trend = ((total_amount_transaction - prev_amount) / prev_amount * 100) if prev_amount > 0 else 0
fraud_trend = fraud_rate - prev_fraud_rate

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Active Users</div>
        <div class="kpi-value">{total_users:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Transactions</div>
        <div class="kpi-value">{total_transactions:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Volume</div>
        <div class="kpi-value">£{total_amount_transaction:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Fraud Rate</div>
        <div class="kpi-value">{fraud_rate:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

# Transaction Status Overview section removed

# Charts Section
st.markdown('<div class="section-title">Analytics Dashboard</div>', unsafe_allow_html=True)

# First row - Weekly Fraud Amount Evolution (full width)
st.markdown('<div class="chart-container">', unsafe_allow_html=True)
st.markdown('<div class="chart-title">Weekly Fraud Amount Evolution</div>', unsafe_allow_html=True)

# Fraud amount evolution
if 'iso_week' in filtered_df.columns:
    # Weekly data structure
    fraud_evolution = filtered_df.groupby("iso_week")["total_amount_fraud"].sum().reset_index()
    x_col = "iso_week"
    x_title = "Week (ISO)"
    hover_template = '<b>Week:</b> %{x}<br><b>Fraud Amount:</b> £%{y:,.2f}<extra></extra>'
else:
    # Daily data structure
    fraud_evolution = filtered_df.groupby("day_date")["total_amount_fraud"].sum().reset_index()
    x_col = "day_date"
    x_title = "Date"
    hover_template = '<b>Date:</b> %{x}<br><b>Fraud Amount:</b> £%{y:,.2f}<extra></extra>'

if not fraud_evolution.empty and fraud_evolution["total_amount_fraud"].sum() > 0:
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=fraud_evolution[x_col],
        y=fraud_evolution["total_amount_fraud"],
        mode='lines+markers',
        name='Fraud Amount',
        line=dict(color=COLORS['danger'], width=3),
        marker=dict(size=8, color=COLORS['danger']),
        hovertemplate=hover_template
    ))
    
    fig.update_layout(
        xaxis_title=x_title,
        yaxis_title="Fraud Amount (£)",
        template="plotly_white",
        height=350,
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=50, r=50, t=50, b=50),
        font=dict(size=12)
    )
    
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No fraud data available for the selected period")

st.markdown('</div>', unsafe_allow_html=True)

# Second row - Transaction Types (2 columns)
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Transaction Types Overview</div>', unsafe_allow_html=True)
    
    # All transaction types (fraudulent and non-fraudulent)
    transaction_by_type = filtered_df.groupby("transaction_type")["nb_transaction"].sum().reset_index()
    
    if not transaction_by_type.empty:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=transaction_by_type["transaction_type"],
            y=transaction_by_type["nb_transaction"],
            marker_color=COLORS['secondary'],
            hovertemplate='<b>Type:</b> %{x}<br><b>Transactions:</b> %{y:,.0f}<extra></extra>'
        ))
        
        fig.update_layout(
            xaxis_title="Transaction Type",
            yaxis_title="Number of Transactions",
            template="plotly_white",
            height=350,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=50, r=50, t=50, b=50),
            font=dict(size=12)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No transaction data available")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Fraudulent Transaction Types</div>', unsafe_allow_html=True)
    
    # Only fraudulent transactions by type
    fraud_by_type = filtered_df.groupby("transaction_type")["nb_transaction_fraud"].sum().reset_index()
    fraud_by_type = fraud_by_type[fraud_by_type["nb_transaction_fraud"] > 0]
    
    if not fraud_by_type.empty:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=fraud_by_type["transaction_type"],
            y=fraud_by_type["nb_transaction_fraud"],
            marker_color=COLORS['danger'],
            hovertemplate='<b>Type:</b> %{x}<br><b>Fraudulent Transactions:</b> %{y:,.0f}<extra></extra>'
        ))
        
        fig.update_layout(
            xaxis_title="Transaction Type",
            yaxis_title="Number of Fraudulent Transactions",
            template="plotly_white",
            height=350,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=50, r=50, t=50, b=50),
            font=dict(size=12)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No fraudulent transaction data available")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Second row of charts
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Top 5 Fraud Amount by Country</div>', unsafe_allow_html=True)
    
    # Top 5 fraud amount by country
    fraud_by_country = filtered_df.groupby("country")["total_amount_fraud"].sum().reset_index()
    fraud_by_country = fraud_by_country[fraud_by_country["total_amount_fraud"] > 0].sort_values("total_amount_fraud", ascending=True).head(5)
    
    if not fraud_by_country.empty:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=fraud_by_country["total_amount_fraud"],
            y=fraud_by_country["country"],
            orientation='h',
            marker_color=COLORS['danger'],
            hovertemplate='<b>Country:</b> %{y}<br><b>Fraud Amount:</b> £%{x:,.2f}<extra></extra>'
        ))
        
        fig.update_layout(
            xaxis_title="Fraud Amount (£)",
            yaxis_title="Country",
            template="plotly_white",
            height=350,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=50, r=50, t=50, b=50),
            font=dict(size=12)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No fraud data by country available")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Top 5 Fraud by Country (Volume)</div>', unsafe_allow_html=True)
    
    # Top 5 fraud volume by country
    fraud_volume_by_country = filtered_df.groupby("country")["nb_transaction_fraud"].sum().reset_index()
    fraud_volume_by_country = fraud_volume_by_country[fraud_volume_by_country["nb_transaction_fraud"] > 0].sort_values("nb_transaction_fraud", ascending=True).head(5)
    
    if not fraud_volume_by_country.empty:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=fraud_volume_by_country["nb_transaction_fraud"],
            y=fraud_volume_by_country["country"],
            orientation='h',
            marker_color=COLORS['primary'],
            hovertemplate='<b>Country:</b> %{y}<br><b>Fraud Volume:</b> %{x:,.0f} transactions<extra></extra>'
        ))
        
        fig.update_layout(
            xaxis_title="Number of Fraudulent Transactions",
            yaxis_title="Country",
            template="plotly_white",
            height=350,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=50, r=50, t=50, b=50),
            font=dict(size=12)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No fraud volume data by country available")
    
    st.markdown('</div>', unsafe_allow_html=True)



# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #64748b; padding: 1.5rem; font-size: 0.875rem;">
        Revolut Financial Crime Dashboard - Real-time monitoring & analytics platform
    </div>
    """,
    unsafe_allow_html=True
) 