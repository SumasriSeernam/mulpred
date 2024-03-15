"""This is the main module to run the app"""

from pathlib import Path

# Importing the necessary Python modules.
import streamlit as st
import sys
import os

# Add the project root directory to the Python path
sys.path.append(str(Path(__file__).parent))

# Set PYTHONPATH to include the parent folder
os.environ["PYTHONPATH"] = str(Path(__file__).parent.parent)
# Import necessary functions from web_functions
from Hepatitis.web_functions import load_data

from Hepatitis.Tabs import home, predict
def hepatitis_main_app():
    # Dictionary for pages
    Tabs = {
        "Home": home,
        "Prediction": predict
    
    }

# Create a sidebar
# Add title to sidear
    st.sidebar.title("Navigation")

# Create radio option to select the page
    page = st.sidebar.radio("", list(Tabs.keys()))

# Loading the dataset.
    df, X, y = load_data()

# Call the app funciton of selected page to run
    if page in ["Prediction"]:
        Tabs[page].app(df, X, y)
    else:
        Tabs[page].app()

if __name__ == "__main__":
    hepatitis_main_app()