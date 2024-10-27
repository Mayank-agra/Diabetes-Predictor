import streamlit as st
import numpy as np
import pickle  # Use pickle to load the model and scaler

# Load the model and scaler using pickle
with open('diabetes_model.pkl', 'rb') as model_file:
    classifier = pickle.load(model_file)   

with open('diabetes_scaler.pkl', 'rb') as scaler_file:
    scalar = pickle.load(scaler_file)

# Streamlit app layout
st.title("Diabetes Prediction System")

# Get input from the user
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose", min_value=0, max_value=200, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=150, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=30.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age", min_value=0, max_value=120, value=25)

# Predict button
if st.button("Predict"):
    try:
        # Prepare input data
        input_data = np.asarray([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age])
        input_data_reshaped = input_data.reshape(1, -1)
        
        # Standardize the data
        std_data = scalar.transform(input_data_reshaped)
        
        # Make prediction
        prediction = classifier.predict(std_data)
        
        # Display the prediction result
        if prediction[0] == 1:
            st.success("The person is predicted to have diabetes.")
        else:
            st.success("The person is predicted not to have diabetes.")
    except Exception as e:
        st.error(f"Error: {e}")
