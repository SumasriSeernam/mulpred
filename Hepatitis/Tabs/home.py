"""This modules contains data about home page"""
from pathlib import Path
import streamlit as st
import sys
sys.path.append(str(Path(__file__).parent))


def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.subheader("Hepatic Disease Predictor")

    # Add image to the home page
    st.image("Hepatitis/images/home.jpeg")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            What is the main cause of liver disease?
There are many types of liver disease, which can be caused by infections, inherited conditions, obesity and misuse of alcohol. Over time, liver disease may lead to scarring and more serious complications. Early treatment can help heal the damage and prevent liver failure.""", unsafe_allow_html=True)
