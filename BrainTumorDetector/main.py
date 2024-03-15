"""This is the main module to run the app"""
from pathlib import Path

# Importing the necessary Python modules.
import streamlit as st
import sys
import os
import warnings
warnings.filterwarnings("ignore")



# Add the project root directory to the Python path
sys.path.append(str(Path(__file__).parent))

# Set PYTHONPATH to include the parent folder
os.environ["PYTHONPATH"] = str(Path(__file__).parent.parent)

# Import necessary functions from web_functions
from BrainTumorDetector.web_functions import load_data

# Import pages
from BrainTumorDetector.Tabs import home, predict, BT



def braintumor_main_app():
    # Dictionary for pages
    Tabs = {
        "Home": home,
        "Prediction": predict,
        "Brain Tumor":BT
   
    
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
    braintumor_main_app()