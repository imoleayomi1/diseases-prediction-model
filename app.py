import os
import pickle
import streamlit as st
import numpy as np
# from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# Set page configuration
st.set_page_config(page_title="Common Disease Prediction",
                   layout="wide",
                   page_icon="🤰")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diseasemodel = pickle.load(open(f'{working_dir}/saved_models/diseasespredictionmodel.sav', 'rb'))


# page title
st.title('Prediction of Common Disease using Machine Learning Technique')
st.caption("Developed by Oyebiyi Iyanuoluwa Elizabeth | Matric No: 2023000798")

# getting the input data from the user
st.subheader("Check all symptoms that apply. Leaving unchecked means you do not have the symptom.")
fever = 1 if st.checkbox('Fever?') else 0











st.success(malariadiagnosis)
