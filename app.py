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
                           'Breast Cancer Prediction'
                           ],
                          icons=['activity','heart','person', 'app'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies: 0 - 17')
        
    with col2:
        Glucose = st.text_input('Glucose Level: 0 - 199')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value: 0 - 122')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value: 0 - 99')
    
    with col2:
        Insulin = st.text_input('Insulin Level: 0 - 846')
    
    with col3:
        BMI = st.text_input('BMI value: 0 - 67.1')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value: 0.08 - 2.42')
    
    with col2:
        Age = st.text_input('Age of the Person: 20 - 90')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # page title
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age:29-77')

    with col2:
        sex = st.number_input('Sex: 1(male)-0(female)')

    with col3:
        cp = st.number_input('Chest Pain types: 0 - 3')

    with col1:
        trestbps = st.number_input('Resting Blood Pressure: 94 - 200')

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl: 126 - 564')

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl: 1(true) - 0(false)')

    with col1:
        restecg = st.number_input('Resting Electrocardiographic results(0 - 2)')

    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved: 71 - 202')

    with col3:
        exang = st.number_input('Exercise Induced Angina: 0 - 1')

    with col1:
        oldpeak = st.number_input('ST depression induced by exercise: 0 - 6.2')

    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # heart_disease_params = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    # heart_disease_int = [int(item) for item in heart_disease_params]

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
 # Breast Cancer prediction
if (selected == 'Breast Cancer Prediction'):
        
        # page title
        st.title('Breast Cancer Prediction using ML')
        col1, col2, col3 , col4 = st.columns(4)

        with col1:
            clump_thickness = st.text_input('Clump Thickness: 1 - 10')

        with col2:
            uniform_cell_size = st.text_input(' Uniformity of Cell Size: 1 - 10')
            
        with col3:
             uniform_cell_shape = st.text_input('Uniformity of Cell Shape: 1 - 10')

        with col4:
            marginal_adhesion = st.text_input('Marginal Adhesion: 1 - 10')

        with col1:
            single_epithelial_size = st.text_input('Single Epithelial Cell Size: 1 - 10')

        with col2:
            bare_nuclei = st.text_input('Bare Nuclei: 1 - 10')

        with col3:
            bland_chromatin = st.text_input('Bland Chromatin: 1 - 10')

        with col4:
            normal_nucleoli = st.text_input('normal_nucleoli: 1 - 10')

        with col1:
            mitoses = st.text_input("mitoses: 1-10")

      

      
        
        
        # code for Prfediction
        breastcancer_diagnosis = ''
        
        # creating a button for Prediction    
        if st.button("Breast Cancer Test Result"):
            breastcancer_prediction = breastcancer_model.predict([[clump_thickness, uniform_cell_size, uniform_cell_shape,
       marginal_adhesion, single_epithelial_size, bare_nuclei,
       bland_chromatin, normal_nucleoli, mitoses]])                          
            
            if (breastcancer_prediction[0] == 2):
              breastcancer_diagnosis = "The person has benign Breast Cancer"
            else:
              breastcancer_diagnosis = "The person have malignant Breast Cancer"
            
        st.success(breastcancer_diagnosis)
 

