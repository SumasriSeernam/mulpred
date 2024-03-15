"""This is the main module to run the app"""
from pathlib import Path

import warnings
warnings.filterwarnings("ignore")


# Importing the necessary Python modules.
import streamlit as st
import sys
import os

# Add the project root directory to the Python path
sys.path.append(str(Path(__file__).parent))

# Set PYTHONPATH to include the parent folder
os.environ["PYTHONPATH"] = str(Path(__file__).parent.parent)


#import web_functions
#from Autism.web_functions 
from web_functions import load_data

from Autism.Tabs import home, predict
#from Autism.Tabs.home import app as home_app




def autism_detector_app():

    # Dictionary for pages
    Tabs = {
        "Home": home,
        "Prediction": predict,
    }
    
    with st.sidebar.expander("Navigation"):
        page = st.sidebar.radio("Go to", list(Tabs.keys()))

    # Create radio option to select the page
    #page = st.sidebar.radio("",list(Tabs.keys()))

    # Loading the dataset.
    df, X, y = load_data()

# Call the app funciton of selected page to run
    if page in ["Prediction"]:
        Tabs[page].app(df, X, y)
    else:
        Tabs[page].app()

if __name__ == "__main__":
    autism_detector_app()