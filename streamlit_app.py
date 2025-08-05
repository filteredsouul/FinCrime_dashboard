"""
Revolut Financial Crime Dashboard
Streamlit Cloud Entry Point
"""

import sys
import os

# Add the scripts directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

# Import and run the dashboard
from scripts.dashboard_senior import *

# The dashboard will run automatically when this file is executed 