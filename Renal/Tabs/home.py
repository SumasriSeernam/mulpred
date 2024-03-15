"""This modules contains data about home page"""

from pathlib import Path
import streamlit as st
import sys
sys.path.append(str(Path(__file__).parent))


def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.header("Renal Disease Predictor")

    # Add image to the home page
    st.image("Renal/images/home.jpeg")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
             Kidney disease means your kidneys are damaged and can’t filter blood the way they should. You are at greater risk for kidney disease if you have diabetes or high blood pressure. If you experience kidney failure, treatments include kidney transplant or dialysis. Other kidney problems include acute kidney injury, kidney cysts, kidney stones, and kidney infections.
        </p>
    """, unsafe_allow_html=True)