import os
import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
from sklearn.model_selection import train_test_split
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
st.subheader ("N.B: Leaving all boxes unchecked will lead to no disease.")
dehydration = 1 if st.checkbox('Dehydration') else 0
vomiting = 1 if st.checkbox('Vomiting') else 0
legcramps = 1 if st.checkbox('Leg cramps') else 0
rapidheartrate = 1 if st.checkbox('Rapid heart rate?') else 0
drymouthskin = 1 if st.checkbox('Dry mouth/skin') else 0
coughsorethroat = 1 if st.checkbox('Cough/Sore throat') else 0
bloodcoughing = 1 if st.checkbox('Blood coughing') else 0
chestpain = 1 if st.checkbox('Chest pain') else 0
fatigueweakness = 1 if st.checkbox('Fatigue/ Weakness') else 0
fever = 1 if st.checkbox('Fever') else 0
lossofappetite = 1 if st.checkbox('Loss of appetite') else 0
shortnessofbreath = 1 if st.checkbox('Shortness of breath') else 0
skinrash = 1 if st.checkbox('Skin rash') else 0
headachebodyache = 1 if st.checkbox('headache/ bodyache') else 0
sneezingrunnynose = 1 if st.checkbox('Sneezing/ runnynose') else 0
burningstomachchestbackpain = 1 if st.checkbox('burning stomach, chest or backpain') else 0 
bloating = 1 if st.checkbox('bloating') else 0
weightloss = 1 if st.checkbox('weightloss') else 0
abdominalpaindiscomfort = 1 if st.checkbox('Abdominal pain/ discomfort') else 0
chillssweating = 1 if st.checkbox('chills/ sweating?') else 0 


# code for Prediction
commondiseasediagnosis = ''

# creating a button for Prediction

if st.button('Disease'):

        inputdata = [dehydration, vomiting, legcramps, rapidheartrate, drymouthskin, coughsorethroat, bloodcoughing, chestpain, fatigueweakness, fever, lossofappetite, shortnessofbreath, skinrash, headachebodyache, sneezingrunnynose, burningstomachchestbackpain, bloating, weightloss, abdominalpaindiscomfort, chillssweating]
        inputdata = [float(x) for x in inputdata]


        prediction = diseasemodel.predict([inputdata])

        st.caption('Result:')
        if prediction[0] == 0:
          commondiseasediagnosis = "**CHOLERA:** there is **possibility** that you have CHOLERA. However, It is advisable to seek **urgent** medical attention for proper diagnosis and treatment."
        elif prediction[0] == 1:
          commondiseasediagnosis = "**Common Cold:** There is a **high probability** that you have common cold. It is advisable to seek **urgent** medical attention for proper diagnosis and treatment."
        elif prediction[0] ==2:
          commondiseasediagnosis = "**Malaria/Typhoid:** Your symptoms **likely indicate** Malaria/Typhoid. Early treatment is recommended to prevent complications. Monitor your health and consult a doctor if symptoms persist."
        elif prediction[0] ==3: 
          commondiseasediagnosis = "**Measles/Chickenpox:** Your symptoms **likely indicate** Measles/Chicken pox. Early treatment is recommended to prevent complications. Monitor your health and consult a doctor if symptoms persist."
        elif prediction[0] ==4:
          commondiseasediagnosis = "**Peptic Ulcer Disease:** Your symptoms **likely indicate** Peptic Ulcer Disease. Early treatment is recommended to prevent complications. Monitor your health and consult a doctor if symptoms persist."
        else:
          commondiseasediagnosis = "**Tuberculosis:** Your symptoms **likely indicate** Tuberculosis. Early treatment is recommended to prevent complications. Monitor your health and consult a doctor if symptoms persist."

st.success(commondiseasediagnosis)

