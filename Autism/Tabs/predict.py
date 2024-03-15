"""This modules contains data about prediction page"""
from pathlib import Path
import streamlit as st
import sys
sys.path.append(str(Path(__file__).parent))

# Import necessary functions from web_functions
#from web_functions import predict
from Autism.web_functions import predict,load_model, train_model



def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.subheader("Prediction Page")

    # Take feature input from the user
    # Add a subheader
    st.write("Select Values:")

    col1,col2,col3 = st.columns(3)

    with col1:
        # Take input of features from the user.
        Age = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))
        Social_Communication_Abilities = st.slider("Social Communication Abilities", int(df["Social Communication Abilities"].min()), int(df["Social Communication Abilities"].max()))
        Repetitive_Behaviors = st.slider("Repetitive Behaviors", int(df["Repetitive Behaviors"].min()), int(df["Repetitive Behaviors"].max()))
        Eye_Contact_Rating = st.slider("Eye Contact Rating", int(df["Eye Contact Rating"].min()), int(df["Eye Contact Rating"].max()))
        Social_Skills = st.slider("Social Skills", int(df["Social Skills"].min()), int(df["Social Skills"].max()))
        IQ_Score = st.slider("IQ Score", int(df["IQ Score"].min()), int(df["IQ Score"].max()))

    with col2:

        Gender = st.radio("Gender", ["Male", "Female"])
        if Gender == "Male":
            Gender = 1
        else:
            Gender = 0

        Developmental_Delay = st.radio("Developmental Delay", ["Yes", "No"])
        if Developmental_Delay == "Yes":
            Developmental_Delay = 1
        else:
            Developmental_Delay = 0

        Family_History_of_Autism = st.radio("Family History of Autism", ["Yes", "No"])
        if Family_History_of_Autism == "Yes":
            Family_History_of_Autism = 1
        else:
            Family_History_of_Autism = 0

        Sensory_Sensitivities = st.radio("Sensory Sensitivities", ["Yes", "No"])
        if Sensory_Sensitivities == "Yes":
            Sensory_Sensitivities = 1
        else:
            Sensory_Sensitivities = 0

        Language_Development = st.radio("Language Development", ["Normal", "Delayed"])
        if Language_Development == "Normal":
            Language_Development = 1
        else:
            Language_Development = 0


    with col3:

        Motor_Skills_Delay = st.radio("Motor Skills Delay", ["Yes", "No"])
        if Motor_Skills_Delay == "Yes":
            Motor_Skills_Delay = 1
        else:
            Motor_Skills_Delay = 0

        Behavioral_Regression = st.radio("Behavioral Regression", ["Yes", "No"])
        if Behavioral_Regression == "Yes":
            Behavioral_Regression = 1
        else:
            Behavioral_Regression =0

        Sleep_Problems = st.radio("Sleep Problems", ["Yes", "No"])
        if Sleep_Problems == "Yes":
            Sleep_Problems = 1
        else:
            Sleep_Problems = 0

        Gastrointestinal_Issues = st.radio("Gastrointestinal Issues", ["Yes", "No"])
        if Gastrointestinal_Issues == "Yes":
            Gastrointestinal_Issues = 1
        else:
            Gastrointestinal_Issues = 0

        Sensitivity_to_Changes = st.radio("Sensitivity to Changes", ["Yes", "No"])
        if Sensitivity_to_Changes == "Yes":
            Sensitivity_to_Changes = 1
        else:
            Sensitivity_to_Changes = 0


    # Create a list to store all the features
    features = [Age,Gender,Developmental_Delay,Family_History_of_Autism,Social_Communication_Abilities,Repetitive_Behaviors,Sensory_Sensitivities,Eye_Contact_Rating,Language_Development,Social_Skills,IQ_Score,Motor_Skills_Delay,Behavioral_Regression,Sleep_Problems,Gastrointestinal_Issues,Sensitivity_to_Changes]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score

        model = load_model()
        # Filter out any rows with unknown target values
        X = X[y.isin(model.classes_)]
        y = y[y.isin(model.classes_)]
        prediction, score = predict(model, X, y, features)
        st.info("Autism level detected...")

        # Print the output according to the prediction
        if (prediction == 1):
            if Developmental_Delay==1 and Family_History_of_Autism==1 and IQ_Score<95:
                st.error("The person has Autism")
            elif IQ_Score<100 and Social_Communication_Abilities<5 and Social_Skills<5:
                st.warning("The person has a possibility of getting Autism")
            else:
                st.success("The person no autism")

        elif (prediction == 2):
            st.warning("The person has a possibility of getting Autism")
        elif (prediction == 0):
            st.error("The person has Autism")
        
        # Print teh score of the model 
        st.sidebar.write("Accuracy of the prediction:", (score*100),"%")

