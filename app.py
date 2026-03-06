import streamlit as st
import joblib
import numpy as np

# 1. Load the pre-trained 'brains'
try:
    model = joblib.load('poly_model.pkl')
    transformer = joblib.load('poly_transformer.pkl')
except:
    st.error("Missing files! Make sure 'poly_model.pkl' is in the same folder.")

st.title("🎓 Student Score Predictor")

# 2. User Input
hours = st.number_input("How many hours did you study?", min_value=0, max_value=100, value=20)

if st.button("Predict My Score"):
    # 3. Transform input to Polynomial (This matches your Degree 2 math)
    input_array = np.array([[hours]])
    transformed_input = transformer.transform(input_array)
    
    # 4. Predict
    prediction = model.predict(transformed_input)
    st.success(f"Your predicted Exam Score is: {prediction[0]:.2f}")
