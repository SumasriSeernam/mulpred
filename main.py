import streamlit as st
from pathlib import Path
import time
from Autism.main import autism_detector_app
from BrainTumorDetector.main import  braintumor_main_app
from Diabetes.main import diabetes_prediction_app
from Hepatitis.main import hepatitis_main_app
from Renal.main import renal_detector_app



def header():
    # Set the background color of the header
    st.title("Multiple Disease Prediction System")
    st.markdown("---")  # Add a horizontal line for separation


def main():
    
    header()

    options = ["Choose a disease","Autism", "Brain Tumour", "Diabetes", "Hepatitis", "Renal"]
    label= "Please select a disease to proceed:"
    selected_disease = st.selectbox(
        label,
        options=options,
        
    )

    # Map disease names to corresponding app folders and file names
    disease_configs = {
        "Autism": {"folder": "Autism", "file": "main.py"},
        "Brain Tumour": {"folder": "BrainTumorDetector", "file": "main.py"},
        "Diabetes": {"folder": "Diabetes", "file": "main.py"},
        "Hepatitis": {"folder": "Hepatitis", "file": "main.py"},
        "Renal": {"folder": "Renal", "file": "main.py"},
    }

    disease_apps = {
        "Autism": autism_detector_app,
        "Brain Tumour" : braintumor_main_app,
        "Diabetes": diabetes_prediction_app,
        "Hepatitis": hepatitis_main_app, 
        "Renal": renal_detector_app,


        # Add other diseases here with corresponding app functions
    }

    # Based on the selected disease, navigate to the corresponding prediction system
    if selected_disease=='Choose a disease':
        st.write('Please make a selection')
    else:
        if selected_disease in disease_configs:
            with st.spinner("Wait a sec..."):
                time.sleep(1)
                config = disease_configs[selected_disease]
                disease_folder = config["folder"]
                disease_file = config["file"]
                disease_app_path = Path(__file__).parent / disease_folder / disease_file

                if disease_app_path.exists():
                    disease_apps[selected_disease]()  # Call the corresponding app function
                else:
                    st.error(f"Error: {selected_disease} prediction system not found.")
        else:
            st.error("Error: Selected disease not recognized.")

if __name__ == "__main__":
    main()
