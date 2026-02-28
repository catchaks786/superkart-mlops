# app.py
import streamlit as st
import joblib
import pandas as pd

# Load trained Decision Tree model
model = joblib.load("model_building/decision_tree_model.pkl")

st.title("SuperKart Sales Prediction")

st.write("Enter input features to predict Product Store Sales Total:")

# Example: dynamically create inputs for numeric columns
# Update these based on your dataset columns
feature_cols = ['feature1', 'feature2']  # Replace with actual feature names

input_data = {}
for col in feature_cols:
    input_data[col] = st.number_input(f"Enter {col}")

if st.button("Predict"):
    df_input = pd.DataFrame([input_data])
    prediction = model.predict(df_input)
    st.success(f"Predicted Sales Total: {prediction[0]:.2f}")