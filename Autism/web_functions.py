"""This module contains necessary function needed"""

# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import joblib


@st.cache_data
def load_data():
    """This function returns the preprocessed data"""

    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('Autism/autism_dataset.csv')
    #drop null values from dataframe
    df.dropna(inplace=True)
    # drop duplicated rows
    df.drop_duplicates(keep='first',inplace=True) 
    le = LabelEncoder()
    # Encode the categorical features
    df['Gender'] = le.fit_transform(df['Gender'])
    df['Developmental Delay'] = le.fit_transform(df['Developmental Delay'])
    df['Family History of Autism'] = le.fit_transform(df['Family History of Autism'])
    df['Sensory Sensitivities'] = le.fit_transform(df['Sensory Sensitivities'])
    df['Language Development'] = le.fit_transform(df['Language Development'])
    df['Result'] = le.fit_transform(df['Result'])
    df['Motor Skills Delay'] = le.fit_transform(df['Motor Skills Delay'])
    df['Behavioral Regression'] = le.fit_transform(df['Behavioral Regression'])
    df['Sleep Problems'] = le.fit_transform(df['Sleep Problems'])
    df['Gastrointestinal Issues'] = le.fit_transform(df['Gastrointestinal Issues'])
    df['Sensitivity to Changes'] = le.fit_transform(df['Sensitivity to Changes'])


    # Perform feature and target split
    X = df.drop('Result', axis=1)  # Features (independent variables)
    y = df['Result']

    
    return df, X, y

def train_model(X, y):
    """This function trains the model and return the model and model score"""

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    # Create the model
    model = RandomForestClassifier(
            n_estimators=200,  
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=1
        )
    # Fit the data on model
    model.fit(X_train,y_train)
    # Get the model score


    # Serialize and deserialize the trained model using joblib
    model = joblib.dump(model,"autism.joblib")
    return X_test, y_test


@st.cache_data
def load_model():
    """This function loads the trained model"""
    # Deserialize the trained model using joblib
    model = joblib.load("autism.joblib")
    return model


def predict(model,X_test,y_test, features):
    # Predict the value
    prediction = model.predict(np.array(features).reshape(1, -1))
    score = model.score(X_test,y_test)
    return prediction,score
