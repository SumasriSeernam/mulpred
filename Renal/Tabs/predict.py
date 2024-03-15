"""This modules contains data about prediction page"""
from pathlib import Path
import streamlit as st
import pandas as pd
import sys
sys.path.append(str(Path(__file__).parent))

import streamlit.components.v1 as components
import pandas as pd

# Import necessary functions from web_functions
from Renal.web_functions import predict, load_model

hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.header("Prediction Page")
    # Take feature input from the user
    # Add a subheader
    st.write("Select Values:")

    # Take input of features from the user.
    Bp = st.slider("Blood Pressure", int(df["Bp"].min()), int(df["Bp"].max()))
    Al = st.slider("Albumin Level", int(df["Al"].min()), int(df["Al"].max()))
    Su = st.slider("Sugar Level", float(df["Su"].min()), float(df["Su"].max()))
    Bu = st.slider("Blood Urea Level", int(df["Bu"].min()), int(df["Bu"].max()))
    Sc = st.slider("Serum Creatinine Level", int(df["Sc"].min()), int(df["Sc"].max()))
    Sod = st.slider("Sodium Level", int(df["Sod"].min()), int(df["Sod"].max()))
    Pot = st.slider("Potassium Level", float(df["Pot"].min()), float(df["Pot"].max()))
    Hemo = st.slider("Hemoglobin Level", float(df["Hemo"].min()), float(df["Hemo"].max()))
    Wbcc = st.slider("White Blood Cell Count", int(df["Wbcc"].min()), int(df["Wbcc"].max()))
    Rbcc = st.slider("Red Blood Cell Count", int(df["Rbcc"].min()), int(df["Rbcc"].max()))

    
    # Create a list to store all the features
    features = [Bp,Al,Su,Bu,Sc,Sod,Pot,Hemo,Wbcc,Rbcc]

    st.header("The values entered by user")
    st.cache_data()
    df3 = pd.DataFrame(features).transpose()
    df3.columns=["Bp","Al","Su","Bu","Sc","Sod","Pot","Hemo","Wbcc","Rbcc"]
    st.dataframe(df3)

    # Create a button to predict
    if st.button("Predict"):
   
        # style the button
        st.markdown("""
        <style>
        .css-18rr30y.et6tpn80 {
            background-color: blue; /* Blue background color */
            color: white; /* text color */
            padding: 5px 10px; /* Some padding */
            border: none; /* No border */
            border-radius: 5px; /* Rounded corners */
            cursor: pointer; /* Pointer cursor on hover */
        }
        .css-18rr30y.et6tpn80:hover {
            background-color: lightblue; /* Light blue hover color */
        }
        </style>
        """, unsafe_allow_html=True)

        model = load_model()
        X = X[y.isin(model.classes_)]
        y = y[y.isin(model.classes_)]
        # Get prediction and model score
        prediction, score = predict(model,X, y, features) 
     

        if prediction == 1:
            if features[0] > 180 and features[2] > 150:  # Arbitrary conditions
                st.error("The person has an extremely high risk of Cardiac problems induced by kidney malfunctioning")
                st.warning("Please consult a Nephrologist and Cardiologist immediately")
            else:
                st.error("The person has high risk of Cardiac problems induced by kidney malfunctioning")
                st.warning("Please consult a Nephrologist")
        elif prediction == 0:
            if features[1] < 3.5 and features[3] < 40:  # Arbitrary conditions
                st.success("The person is extremely safe from Renal Diseases")
            else:
                st.success("The person is relatively safe from Renal Diseases")

            
        # Print teh score of the model 
        st.sidebar.write("Accuracy of the prediction:", (score*100),"%")
