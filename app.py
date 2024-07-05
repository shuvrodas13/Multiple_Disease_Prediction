Your Streamlit app code looks well-structured, but it needs a few corrections and enhancements for proper functioning and user experience improvement. Here are some suggestions:

1. **Correct Step Values for Number Inputs**: The `step` value should be consistent with the data type. For example, steps for floating-point numbers should be appropriate decimals.

2. **Fixing Breast Cancer Prediction Input and Logic**: The input limits for breast cancer features should start from 1 as mentioned in the input description.

3. **Enhance Prediction Message**: It's better to have more user-friendly and informative messages.

Here is the corrected and enhanced version of your code:

```python
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 13:27:27 2022

@author: HP
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
breastcancer_model = pickle.load(open('model.pkl', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Breast Cancer Prediction'],
                          icons=['activity','heart','person','man-health-worker'],
                          default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies:', min_value=0, max_value=17, step=1)
    with col2:
        Glucose = st.number_input('Glucose Level:', min_value=0, max_value=199, step=1)
    with col1:
        BloodPressure = st.number_input('Blood Pressure value:', min_value=0, max_value=122, step=1)
    with col2:
        SkinThickness = st.number_input('Skin Thickness value:', min_value=0, max_value=99, step=1)
    with col1:
        Insulin = st.number_input('Insulin Level:', min_value=0, max_value=846, step=1)
    with col2:
        BMI = st.number_input('BMI value:', min_value=0.0, max_value=67.1, step=0.1, format="%.1f")
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value:', min_value=0.08, max_value=2.42, step=0.01, format="%.2f")
    with col2:
        Age = st.number_input('Age of the Person:', min_value=20, max_value=90, step=1)

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'This person has a high chance of diabetes.'
        else:
            diab_diagnosis = 'This person is unlikely to have diabetes.'
        
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age:', min_value=29, max_value=77, step=1)
    with col2:
        sex = st.number_input('Sex (1=male, 0=female):', min_value=0, max_value=1, step=1)
    with col3:
        cp = st.number_input('Chest Pain types (0-3):', min_value=0, max_value=3, step=1)
    with col1:
        trestbps = st.number_input('Resting Blood Pressure:', min_value=90, max_value=200, step=1)
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl:', min_value=126, max_value=564, step=1)
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1=true, 0=false):', min_value=0, max_value=1, step=1)
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results (0-2):', min_value=0, max_value=2, step=1)
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved:', min_value=71, max_value=202, step=1)
    with col3:
        exang = st.number_input('Exercise Induced Angina (1=yes, 0=no):', min_value=0, max_value=1, step=1)
    with col1:
        oldpeak = st.number_input('ST depression by exercise:', min_value=0.0, max_value=6.2, step=0.1, format="%.1f")
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment:', min_value=0, max_value=2, step=1)
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy (0-3):', min_value=0, max_value=3, step=1)
    with col1:
        thal = st.number_input('Thalassemia (1=normal, 2=fixed defect, 3=reversable defect):', min_value=0, max_value=3, step=1)

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'This person has a high chance of heart disease.'
        else:
            heart_diagnosis = 'This person is unlikely to have heart disease.'
        
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', step=1e-5, format="%.5f")
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', step=1e-5, format="%.5f")
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', step=1e-5, format="%.5f")
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)', step=1e-5, format="%.5f")
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', step=1e-5, format="%.5f")
    with col1:
        RAP = st.number_input('MDVP:RAP', step=1e-5, format="%.5f")
    with col2:
        PPQ = st.number_input('MDVP:PPQ', step=1e-5, format="%.5f")
    with col3:
        DDP = st.number_input('Jitter:DDP', step=1e-5, format="%.5f")
    with col4:
        Shimmer = st.number_input('MDVP:Shimmer', step=1e-5, format="%.5f")
    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', step=1e-5, format="%.5f")
    with col1:
        APQ3 = st.number_input('Shimmer:APQ3', step=1e-5, format="%.5f")
    with col2:
        APQ5 = st.number_input('Shimmer:APQ5', step=1e-5, format="%.5f")
    with col3:
        APQ = st.number_input('MDVP:APQ', step=1e-5, format="%.5f")
    with col4:
        DDA = st.number_input('Shimmer:DDA', step=1e-5, format="%.5f")
    with col5:
        NHR = st.number_input('NHR', step=1e-5, format="%.5f")
    with col1:
        HNR = st.number_input('HNR', step=1e-5, format="%.5f")
    with col2:
        RPDE = st.number_input('RPDE', step=1e-5, format="%.5f")
    with col3:
        DFA = st.number_input('DFA', step=1e-5, format="%.5f")
    with col4:
        spread1 = st.number_input('spread1', step=1e-5